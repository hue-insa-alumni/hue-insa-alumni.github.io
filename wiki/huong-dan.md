# 00 - Hướng dẫn sử dụng

---

## Hướng dẫn chung

HUE INSA WIKI được phát triển dựa trên phần mềm mã nguồn mở DokuWiki. Đây là hướng dẫn sử dụng của doku wiki trên trang chủ của nhà phát hành: [https://www.dokuwiki.org/manual](https://www.dokuwiki.org/manual).

## Hướng dẫn sử dụng cơ bản

Dưới đây là hướng dẫn cụ thể và một số quy ước khi sử dụng HUE INSA WIKI.

## Tạo trang mới

Nhập URL theo quy ước sau:

> doku.php?id={namespace1}:{namespace2}:{tên page}

Ví dụ, để tạo 1 trang mới về "Chương trình học INSA CVL" trong namespace "Chương trình học", ta cần sử dụng URL sau:

> doku.php?id=chuong-trinh-hoc:chuong-trinh-hoc-insa-cvl

Sau đó, vui lòng thay đổi nội dung của trang và lưu để hoàn tất quá trình tạo trang.

⚠️ Để tránh nhầm lẫn và xảy ra lỗi, vui lòng nhập tên trang và namespace theo quy ước: viết liền, không dấu và dùng dấu gạch "-" để phân chia từ nếu cần thiết.

## Namespaces

Để dễ dàng quản lý nội dung của wiki, khuyến khích sử dụng namespace để phân chia nội dung theo chủ đề lớn nhỏ. Cách tạo mới namespace tương tự như tạo 1 page mới ở trên, namespace sẽ tự động được tạo.

## Chỉnh sửa nội dung

### Viết bài

Để bắt đầu viết bài hoặc chỉnh sửa nội dung của một trang bất kỳ, vui lòng nhấn vào icon bút chì như hình dưới đây:

![Edit Icon](1.png)

### Sơ lược về Markdown

#### Giới thiệu

Markdown là ngôn ngữ đánh dấu văn bản được tạo ra bởi John Gruber, sử dụng cú pháp khá đơn giản và dễ hiểu, dễ nhớ. Nếu nắm vững các cú pháp của Markdown bạn có thể trình bày bài viết của mình một cách mạch lạc, ấn tượng mà không mất nhiều thời gian. Trình editor của WIKI sử dụng hoàn toàn với cú pháp của Markdown, dưới đây là một số hướng dẫn cơ bản để làm quen với ngôn ngữ này. Để biết thêm những cú pháp nâng cao khác, vui lòng tham khảo tại [đây](https://www.dokuwiki.org/wiki:syntax).

#### Tạo đề mục

**Cú pháp:**

```
# Đề mục cấp 1
## Đề mục cấp 2
### Đề mục cấp 3
#### Đề mục cấp 4
##### Đề mục cấp 5
```

**Kết quả:**

![Headings](22.png)

#### Danh sách đánh số

**Cú pháp:**

```
1. Phần tử 1
   1. Phần tử 1.1
   2. Phần tử 1.2
2. Phần tử 2
3. Phần tử 3
```

**Kết quả:**

1. Phần tử 1
   1. Phần tử 1.1
   2. Phần tử 1.2
2. Phần tử 2
3. Phần tử 3

#### Danh sách không đánh số

**Cú pháp:**

```
* Phần tử 1
  * Phần tử 1.1
  * Phần tử 1.2
* Phần tử 2
  * Phần tử 2.1
* Phần tử 3
```

**Kết quả:**

- Phần tử 1
  - Phần tử 1.1
  - Phần tử 1.2
- Phần tử 2
  - Phần tử 2.1
- Phần tử 3

#### Bảng

**Cú pháp:**

```
| Heading 1 | Heading 2 | Heading 3 |
|-----------|-----------|-----------|
| Row 1 Col 1 | Row 1 Col 2 | Row 1 Col 3 |
| Row 2 Col 1 | Row 1 Col 2 | Row 2 Col 3 |
| Row 3 Col 1 | Row 3 Col 2 | Row 3 Col 3 |
```

**Kết quả:**
| Heading 1 | Heading 2 | Heading 3 |
|-----------|-----------|-----------|
| Row 1 Col 1 | Row 1 Col 2 | Row 1 Col 3 |
| Row 2 Col 1 | Row 1 Col 2 | Row 2 Col 3 |
| Row 3 Col 1 | Row 3 Col 2 | Row 3 Col 3 |

#### Quoting

**Cú pháp:**

```
I think we should do it

> No we shouldn't

>> Well, I say we should

> Really?

>> Yes!

>>> Then lets do it!
```

**Kết quả:**

> I think we should do it

> No we shouldn't

> > Well, I say we should

> Really?

> > Yes!

> > > Then lets do it!

#### CodeBlock

**Cú pháp:**

```
This is preformatted code all spaces are preserved: like              <-this
```

**Kết quả:**

```
This is preformatted code all spaces are preserved: like              <-this
```

#### Chèn hình ảnh

Để bắt đầu chèn hình ảnh, vui lòng nhấn vào icon chèn hình ảnh như hình dưới đây để mở ra cửa sổ tải hình ảnh:

![Insert Image](33.png)

Tiếp đến, chọn 1 thư mục bất kỳ để bắt đầu tải ảnh lên (ví dụ: thư mục gốc hoặc wiki), sau đó chọn hình ảnh vừa tải lên để chèn vào bài viết.
