---
authors:
  - name: "Hué-INSA Alumni"
    github: "hue-insa-alumni"
date: 2026-07-23 00:00 +0200
---

# Hướng dẫn sử dụng

## Đóng góp nội dung

Bất kỳ thành viên nào cũng có thể đóng góp hoặc chỉnh sửa nội dung wiki. Quy trình đóng góp được thực hiện qua GitHub để đảm bảo mọi thay đổi đều được kiểm duyệt trước khi xuất bản.

### Bình luận qua Giscus

Mỗi trang wiki có phần **bình luận ở cuối trang** được cung cấp bởi [Giscus](https://giscus.app). Bạn có thể đặt câu hỏi, góp ý hoặc chia sẻ kinh nghiệm trực tiếp trên từng trang mà không cần tạo PR.

Yêu cầu: **tài khoản GitHub** để đăng nhập và bình luận.

### 1. Tạo tài khoản GitHub

Truy cập [github.com](https://github.com) và tạo tài khoản miễn phí nếu chưa có.

### 2. Chỉnh sửa nội dung

#### Chỉnh sửa nhanh trên trình duyệt

Đây là cách đơn giản nhất, không cần cài đặt gì:

1. Mở trang wiki muốn chỉnh sửa
2. Nhấn nút **✏️ Edit** ở góc trên bên phải trang
3. GitHub sẽ tự động **fork** (tạo bản sao) repository về tài khoản của bạn
4. Chỉnh sửa nội dung trực tiếp trên trình duyệt
5. Kéo xuống cuối trang, điền mô tả ngắn về thay đổi, nhấn **Propose changes**

#### Chỉnh sửa nội dung phức tạp (local)

Dùng cách này khi cần thêm nhiều trang hoặc thay đổi cấu trúc:

1. Fork repository tại [github.com/hue-insa-alumni/hue-insa-alumni.github.io](https://github.com/hue-insa-alumni/hue-insa-alumni.github.io)
2. Clone fork về máy:
   ```bash
   git clone https://github.com/<username>/hue-insa-alumni.github.io
   cd hue-insa-alumni.github.io
   ```
3. Cài đặt môi trường (nếu chưa có `uv`, chạy `make install-uv` trước):
   ```bash
   make setup
   ```
4. Chạy server để xem trước:
   ```bash
   make run
   ```
   Mở trình duyệt tại `http://localhost:8000` để kiểm tra thay đổi.
5. Commit và push lên fork của bạn.

### 3. Tạo Pull Request

Sau khi hoàn tất chỉnh sửa (dù qua trình duyệt hay local), GitHub sẽ đề nghị tạo **Pull Request (PR)**:

1. Nhấn **Compare & pull request**
2. Điền tiêu đề mô tả rõ nội dung thay đổi, ví dụ: `Cập nhật thông tin làm visa`
3. Mô tả chi tiết hơn trong phần body nếu cần
4. Nhấn **Create pull request**

### 4. Kiểm tra tự động (CI)

Sau khi tạo PR, hệ thống sẽ tự động chạy kiểm tra để đảm bảo nội dung không gây lỗi khi build.

✅ **Nếu kiểm tra qua** — PR sẵn sàng để được review.

❌ **Nếu kiểm tra thất bại** — nhấn vào **Details** cạnh thông báo lỗi để xem chi tiết. Các lỗi thường gặp:

| Lỗi            | Nguyên nhân                          | Cách sửa                                           |
| -------------- | ------------------------------------ | -------------------------------------------------- |
| File not found | Đường dẫn trong nav hoặc link bị sai | Kiểm tra lại tên file và đường dẫn                 |
| Build error    | Cú pháp Markdown không hợp lệ        | Xem lại phần có lỗi, chạy `make run` để test local |

Sau khi sửa lỗi, commit và push lại — CI sẽ tự động chạy lại.

### 5. Review và phê duyệt

PR cần được **ít nhất một thành viên ban quản trị** phê duyệt trước khi merge. Thành viên ban quản trị sẽ:

- Kiểm tra nội dung chính xác và phù hợp
- Đề xuất chỉnh sửa nếu cần (bạn sẽ nhận được thông báo qua email)
- Phê duyệt (Approve) khi nội dung đã ổn

Nếu có góp ý, bạn có thể trả lời trực tiếp trên PR hoặc tiếp tục chỉnh sửa file và push lại.

### 6. Merge

Sau khi PR được phê duyệt và CI qua, thành viên ban quản trị sẽ **merge** PR. Nội dung sẽ tự động được xuất bản lên wiki trong vòng vài phút.

> **Cần hỗ trợ?** Để lại bình luận trên PR hoặc liên hệ ban quản trị qua [GitHub](https://github.com/hue-insa-alumni).

### Trở thành Collaborator

Nếu bạn muốn đóng góp thường xuyên và lâu dài, hãy liên hệ ban quản trị để được thêm vào danh sách **Collaborator** của repository. Collaborator có thể tạo branch trực tiếp trên repo mà không cần fork, giúp quy trình đóng góp nhanh hơn.

---

## Tạo trang mới

Để tạo một trang mới, bạn cần:

1. Tạo file `.md` mới trong thư mục tương ứng dưới `contents/`
2. Thêm frontmatter ở đầu file với thông tin tác giả và ngày cập nhật:

```yaml
---
authors:
  - name: "Tên của bạn"
    github: "username-github"
date: YYYY-MM-DD HH:MM +0100
---
```

3. Viết nội dung bằng Markdown. Để tắt bình luận Giscus trên trang đó:
   ```yaml
   ---
   comments: false
   ---
   ```
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
