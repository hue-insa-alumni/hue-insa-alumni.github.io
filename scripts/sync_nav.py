#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["tomlkit"]
# ///
"""Sync the `nav` table of contents in zensical.toml with contents/*.md.

For every markdown file already referenced in `nav`:
  - remove its nav entry if the file no longer exists
  (existing nav titles are curated by hand and are never overwritten)

For every markdown file NOT referenced in `nav`:
  - append it (title = H1 heading) to the same nav group as its
    sibling pages, if that group can be determined unambiguously
  - otherwise print a warning so it can be placed manually

Run with: uv run scripts/sync_nav.py [--check]
"""

import argparse
import re
import sys
from pathlib import Path

import tomlkit
from tomlkit.items import Array, InlineTable, Item

ROOT: Path = Path(__file__).resolve().parent.parent
TOML_PATH: Path = ROOT / "zensical.toml"
DOCS_DIR: Path = ROOT / "contents"

H1_RE: re.Pattern[str] = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

# A leaf nav record: (array it lives in, its single-key table, its markdown path).
Leaf = tuple[Array, InlineTable, str]


def extract_title(md_path: Path) -> str | None:
    text = md_path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]
    match = H1_RE.search(text)
    return match.group(1).strip() if match else None


def entry_key_value(item: InlineTable) -> tuple[str, Item]:
    key = next(iter(item))
    return key, item[key]


def collect_leaves(array: Array, leaves: list[Leaf]) -> None:
    """Recursively collect (containing_array, item, relative_path) for every leaf entry."""
    for item in array:
        _, value = entry_key_value(item)
        if isinstance(value, str):
            leaves.append((array, item, value))
        else:
            collect_leaves(value, leaves)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="exit 1 if the file would change, without writing"
    )
    args: argparse.Namespace = parser.parse_args()

    doc = tomlkit.parse(TOML_PATH.read_text(encoding="utf-8"))
    nav: Array = doc["project"]["nav"]

    leaves: list[Leaf] = []
    collect_leaves(nav, leaves)

    added = 0
    removed = 0
    skipped = 0

    # Remove nav entries for files that no longer exist.
    for array, item, rel_path in list(leaves):
        if not (DOCS_DIR / rel_path).exists():
            array.remove(item)
            leaves.remove((array, item, rel_path))
            print(f"  \033[31m-\033[0m Removed: {rel_path}  (file no longer exists)")
            removed += 1

    # Determine, per directory, which nav array already holds its pages.
    dir_to_arrays: dict[str, set[int]] = {}
    dir_to_array_obj: dict[str, Array] = {}
    for array, _, rel_path in leaves:
        parent = Path(rel_path).parent.as_posix()
        dir_to_arrays.setdefault(parent, set()).add(id(array))
        dir_to_array_obj[parent] = array

    known_paths: set[str] = {rel_path for _, _, rel_path in leaves}

    # Add nav entries for markdown files not yet referenced.
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        rel_path = md_file.relative_to(DOCS_DIR).as_posix()
        if rel_path in known_paths:
            continue
        parent = Path(rel_path).parent.as_posix()
        if len(dir_to_arrays.get(parent, ())) != 1:
            print(f"  \033[33m?\033[0m {rel_path}  (ambiguous group, add manually)")
            skipped += 1
            continue
        title: str = extract_title(md_file) or md_file.stem
        escaped_title: str = title.replace("\\", "\\\\").replace('"', '\\"')
        new_item: Item = tomlkit.parse(f'x = {{ "{escaped_title}" = "{rel_path}" }}\n')["x"]
        dir_to_array_obj[parent].append(new_item)
        print(f"  \033[32m+\033[0m ADDED: {rel_path}  -> {title!r}")
        added += 1

    if not added and not removed:
        print(f"nav is already in sync ({len(leaves)} pages, {skipped} skipped)")
        return 0

    summary = f"{added} added, {removed} removed, {skipped} skipped"

    if args.check:
        print(f"nav is out of sync: {summary} (--check, not writing)")
        return 1

    TOML_PATH.write_text(tomlkit.dumps(doc), encoding="utf-8")
    print(f"wrote {TOML_PATH}: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
