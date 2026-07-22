# Hué-INSA Alumni Wiki

Cổng thông tin chung của hội Hué-INSA Alumni, xây dựng bằng [Zensical](https://github.com/zensical/zensical).

## Yêu cầu

- [uv](https://docs.astral.sh/uv/) — Python package manager

## Cài đặt

```bash
make setup        # cài đặt Zensical qua uv tool
```

Nếu chưa có `uv`:

```bash
make install-uv   # cài đặt uv
make setup        # cài đặt Zensical
```

## Chạy local

```bash
make run          # khởi động dev server tại http://localhost:8000
```

## Đóng góp nội dung

Nội dung wiki nằm trong thư mục [`contents/`](contents/). Mỗi trang là một file Markdown (`.md`).

### Chỉnh sửa trực tiếp trên GitHub

Nhấn nút ✏️ **Edit** ở góc trên bên phải mỗi trang — GitHub sẽ tự tạo fork và mở Pull Request để review.

### Chỉnh sửa local

1. Fork repo và clone về máy
2. Chạy `make run` để xem trước thay đổi
3. Tạo Pull Request khi hoàn tất

### Cấu trúc thư mục

```
contents/
├── index.md                        # Trang chủ
├── wiki/                           # Nội dung wiki sinh viên
│   ├── gioi-thieu-chuong-trinh/
│   ├── chuan-bi-sang-phap/
│   └── ...
└── scholarship/               # Quỹ học bổng hội
```

### Frontmatter

Mỗi file bắt đầu bằng frontmatter YAML:

```yaml
---
authors:
  - name: "Tên của bạn"
    github: "username-github"
date: YYYY-MM-DD
---

# Tiêu đề trang
```

Để tắt phần bình luận trên một trang cụ thể:

```yaml
---
comments: false
---
```

### Cú pháp Markdown

Xem hướng dẫn đầy đủ tại trang [Hướng dẫn sử dụng](contents/huong-dan.md) trong wiki.
