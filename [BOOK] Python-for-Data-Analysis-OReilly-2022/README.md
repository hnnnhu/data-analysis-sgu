# Python for Data Analysis (Wes McKinney, ấn bản 3, 2022) — Ghi chú học tập & Thực hành

## Tóm tắt (Abstract)
Thư mục này lưu trữ ghi chú học tập và bài thực hành được xây dựng trong quá trình tự học từ sách *Python for Data Analysis* (ấn bản 3, 2022). Mục tiêu là củng cố kiến thức về phân tích dữ liệu bằng Python, luyện kỹ năng tái lập (reproducible) và tạo ra sản phẩm học tập có thể kiểm chứng: ghi chú, notebook, bài tập và mini-project.

## Từ khóa
Python; Phân tích dữ liệu; NumPy; pandas; Làm sạch dữ liệu; EDA; Tái lập nghiên cứu

## Phạm vi và mục tiêu
### Phạm vi
- Ghi chú theo chương: khái niệm, công thức/logic, lỗi thường gặp, điểm cần nhớ.
- Notebook/script tự viết để luyện tập các kỹ thuật trong sách.
- Bài tập tự đặt và lời giải kèm giải thích.
- Chỉ sử dụng dữ liệu công khai/mở hoặc dữ liệu được phép chia sẻ.

### Mục tiêu
- Nắm vững quy trình phân tích dữ liệu cơ bản với NumPy/pandas.
- Hình thành thói quen làm việc tái lập: môi trường, nguồn dữ liệu, phiên bản, kết quả.
- Viết ghi chú ngắn gọn nhưng có kiểm chứng (kèm code và kiểm tra hợp lý).

## Cấu trúc thư mục
- `notes/` — ghi chú theo chương (tóm tắt + ví dụ tối thiểu).
- `code/` — notebook/script luyện tập (tự viết lại).
- `exercises/` — bài tập và lời giải (có giải thích).
- `datasets/` — dữ liệu **chỉ** từ nguồn công khai/được phép chia sẻ.
- `references/` — tài liệu tham khảo (trích dẫn, liên kết hợp pháp; **không** chứa PDF trả phí).

## Phương pháp học (Quy trình tái lập)
1. **Đọc**: xác định ý chính, API quan trọng, giả định ngầm.
2. **Tự triển khai lại**: viết code từ đầu (không copy mù).
3. **Kiểm chứng**: thêm kiểm tra hợp lý (shape, thống kê mô tả, sanity plot).
4. **Ghi chú**: mỗi chương/tópic phải có:
   - khái niệm cốt lõi,
   - lỗi thường gặp,
   - ví dụ tối thiểu chạy được,
   - kết luận/điểm rút ra.

## Chuẩn mực học thuật & bản quyền
- Thư mục này **không** dùng để chia sẻ lại nội dung sách có bản quyền (PDF scan, bản chụp, file trả phí).
- Ghi chú được viết theo cách diễn đạt và cấu trúc của cá nhân; code do cá nhân tự viết.
- Nếu có trích dẫn trực tiếp (nếu cần), phải ngắn gọn và ghi rõ nguồn.

Khuyến nghị: nếu repo đang public, **không** upload sách/PDF trả phí. Nếu cần lưu riêng, hãy để repo private hoặc lưu offline.

## Trích dẫn (Citation)
### Tài liệu chính
Wes McKinney (2022). *Python for Data Analysis* (Ấn bản 3). O’Reilly Media.

### Trích dẫn thư mục ghi chú (tùy chọn)
[Tên bạn]. (Năm). *Ghi chú học tập Python for Data Analysis (ấn bản 3)*. GitHub repository: [Link repo]

## Môi trường và phụ thuộc
Khuyến nghị:
- Python >= 3.10
- JupyterLab

Cài đặt tối thiểu:
```bash
pip install numpy pandas matplotlib jupyterlab

