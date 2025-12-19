# Lab 13B – Tập phổ biến & Luật kết hợp (Association Rules)

## A) Mục tiêu
- Tìm frequent itemsets và luật kết hợp từ dữ liệu giao dịch
- Hiểu support, confidence, lift (không làm kiểu bấm nút)

## B) Dataset
- Dữ liệu dạng transaction: mỗi giao dịch gồm các item
- Nếu dữ liệu dạng bảng: chuyển sang one-hot transaction format

## C) Nhiệm vụ bắt buộc
1) Chuẩn hóa transaction data
- Làm sạch item trùng, chuẩn hóa tên item

2) Frequent itemsets
- Apriori hoặc FP-Growth
- Chọn min_support hợp lý (giải thích vì sao)

3) Sinh luật
- Sinh luật với confidence threshold
- Báo cáo top luật theo lift (và giải thích lift)

4) Phân tích luật
- Ít nhất 10 luật “đáng chú ý”
- Nêu 3 luật “rác” và vì sao nó rác (ví dụ support thấp/hiển nhiên)

5) Ứng dụng
- Gợi ý cross-sell / bundle / recommendation (3–5 bullet)

## D) Output
- Notebook: `project/notebooks/lab13_association_rules.ipynb`
