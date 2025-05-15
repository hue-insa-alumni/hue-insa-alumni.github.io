---
authors:
  - name: "Hué-INSA Alumni"
    github: "hue-insa-alumni"
date: 2025-05-15 01:04 +0100
---

# Hướng dẫn sử dụng

## Hướng dẫn chung

HUE INSA WIKI được phát triển dựa trên Jekyll và sử dụng Markdown để viết nội dung. Đây là hướng dẫn sử dụng Markdown cơ bản để giúp bạn đóng góp nội dung cho wiki.

## Hướng dẫn sử dụng cơ bản

Dưới đây là hướng dẫn cụ thể và một số quy ước khi sử dụng HUE INSA WIKI.

## Tạo trang mới

Để tạo một trang mới, bạn cần:

1. Tạo file `.md` mới trong thư mục tương ứng
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
4. Commit và push lên repository

## Cấu trúc thư mục

Wiki được tổ chức theo các thư mục chính:

- `gioi-thieu-truong-hoc/`: Thông tin về trường học
- `chuan-bi-sang-phap/`: Hướng dẫn chuẩn bị
- `gioi-thieu-cuoc-song/`: Thông tin về cuộc sống
- `thu-tuc-hanh-chinh/`: Các thủ tục hành chính
- `xin-thuc-tap-xin-viec/`: Hướng dẫn xin việc
- `tips-cuoc-song/`: Các tips hữu ích

## Hướng dẫn Markdown

### Tiêu đề

```markdown
# Tiêu đề cấp 1

## Tiêu đề cấp 2

### Tiêu đề cấp 3

#### Tiêu đề cấp 4

##### Tiêu đề cấp 5
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
>
> > Đây là trích dẫn lồng nhau
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

````

### Liên kết

```markdown
[Văn bản liên kết](https://example.com)
````

### Hình ảnh

```markdown
![Mô tả hình ảnh](/đường/dẫn/đến/hình/ảnh.jpg)
```

### Định dạng văn bản

```markdown
_in nghiêng_
**in đậm**
**_in đậm và nghiêng_**
~~gạch ngang~~
```

### Ghi chú

```markdown
> ⚠️ Đây là một ghi chú quan trọng
```

## Quy ước viết bài

1. Luôn thêm front matter với thông tin tác giả và ngày
2. Sử dụng tiêu đề cấp 1 (#) cho tiêu đề chính của trang
3. Sử dụng tiêu đề cấp 2 (##) cho các phần chính
4. Sử dụng tiêu đề cấp 3 (###) cho các phần con
5. Thêm ghi chú quan trọng bằng blockquote với emoji ⚠️
6. Sử dụng danh sách có thứ tự cho các bước thực hiện
7. Sử dụng danh sách không thứ tự cho các mục liệt kê
8. Thêm hình ảnh minh họa khi cần thiết
9. Đặt tên file theo quy ước: viết thường, dùng dấu gạch ngang (-) thay dấu cách
