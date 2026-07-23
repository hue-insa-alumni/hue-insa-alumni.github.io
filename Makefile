#!make

.PHONY: help install-uv setup run build

.DEFAULT_GOAL := help

help: ## show help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% 0-9a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install-uv: ## install uv if not already installed
	@command -v uv >/dev/null 2>&1 || curl -LsSf https://astral.sh/uv/install.sh | sh

setup: install-uv ## install zensical globally via uv tool
	uv tool install zensical

build: ## build site with zensical
	uvx zensical build --clean --strict --config-file zensical.toml

run: ## start local dev server with live reload
	zensical serve --config-file zensical.toml


%:
	@true
