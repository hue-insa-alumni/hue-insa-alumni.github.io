---
authors:
  - name: "Hué-INSA Alumni"
    github: "hue-insa-alumni"
date: 2026-07-23 00:00 +0200
---

# Hướng dẫn sử dụng

## Hướng dẫn chung

HUE INSA WIKI được xây dựng bằng [Zensical](https://zensical.org) và sử dụng Markdown để viết nội dung. Đây là hướng dẫn đóng góp nội dung cho wiki.

## Tạo trang mới

Để tạo một trang mới, bạn cần:

1. Tạo file `.md` mới trong thư mục tương ứng dưới `contents/`
2. Thêm front matter ở đầu file với thông tin tác giả và ngày:

```yaml
---
authors:
  - name: "Tên của bạn"
    github: "username-github"
date: YYYY-MM-DD HH:MM +0100
---
```

3. Viết nội dung bằng Markdown
4. Đăng ký trang trong phần `nav` của file `zensical.toml`
5. Commit và push lên repository

## Cấu trúc thư mục

```
contents/
├── wiki/                          # Nội dung wiki sinh viên
│   ├── gioi-thieu-chuong-trinh/
│   ├── gioi-thieu-truong-hoc/
│   ├── chuan-bi-sang-phap/
│   ├── thu-tuc-hanh-chinh/
│   ├── gioi-thieu-cuoc-song/
│   ├── tips-cuoc-song/
│   ├── huong-dan-duong-di/
│   ├── dinh-huong/
│   ├── xin-thuc-tap-xin-viec/
│   ├── tu-van-nganh-hoc/
│   ├── thanh-tich-cuu-sinh-vien/
│   └── 2-nam-hoc-o-viet-nam/
└── scholarship/                  # Quỹ học bổng hội
```

## Hướng dẫn Markdown

### Tiêu đề

```markdown
# Tiêu đề cấp 1

## Tiêu đề cấp 2

### Tiêu đề cấp 3
```

### Danh sách có thứ tự

```markdown
1. Mục thứ nhất
2. Mục thứ hai
   1. Mục con 2.1
   2. Mục con 2.2
3. Mục thứ ba
```

### Danh sách không thứ tự

```markdown
- Mục thứ nhất
- Mục thứ hai
  - Mục con 2.1
  - Mục con 2.2
- Mục thứ ba
```

### Bảng

```markdown
| Cột 1  | Cột 2   | Cột 3   |
| ------ | ------- | ------- |
| Dòng 1 | Dữ liệu | Dữ liệu |
| Dòng 2 | Dữ liệu | Dữ liệu |
```

### Trích dẫn

```markdown
> Đây là một đoạn trích dẫn
```

### Code

````markdown
`inline code`

```python
# code block
def hello():
    print("Hello, World!")
```
````

### Liên kết

```markdown
[Văn bản liên kết](https://example.com)
```

### Hình ảnh

```markdown
![Mô tả hình ảnh](assets/ten-hinh.jpg)
```

### Định dạng văn bản

```markdown
_in nghiêng_
**in đậm**
~~gạch ngang~~
```

### Ghi chú

```markdown
> ⚠️ Đây là một ghi chú quan trọng
```

## Quy ước viết bài

1. Luôn thêm frontmatter với thông tin tác giả và ngày
2. Sử dụng tiêu đề cấp 1 (`#`) cho tiêu đề chính của trang
3. Sử dụng tiêu đề cấp 2 (`##`) cho các phần chính
4. Sử dụng danh sách có thứ tự cho các bước thực hiện
5. Sử dụng danh sách không thứ tự cho các mục liệt kê
6. Đặt tên file: viết thường, dùng dấu gạch ngang (`-`) thay dấu cách
