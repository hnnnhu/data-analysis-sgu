# DA09 – Thuật toán hồi quy tuyến tính & Logistic

## A) Mục tiêu
- Hiểu Linear Regression và Logistic Regression: không chỉ gọi hàm, mà biết kiểm tra giả định và đánh giá đúng metric.

## B) Dataset
- Linear Regression: dataset có target liên tục (giá nhà, doanh thu, ...)
- Logistic Regression: dataset có nhãn 0/1 (Pima diabetes, churn, ...)

## C) Nhiệm vụ bắt buộc

### 1) Linear Regression
- Chuẩn bị dữ liệu + split
- Fit Linear Regression
- Đánh giá: MAE, RMSE, R2
- Kiểm tra residuals (plot residual vs predicted)
- Phân tích hệ số (coef) và giải thích ý nghĩa

### 2) Logistic Regression
- Chuẩn bị dữ liệu + split (stratify)
- Fit Logistic Regression (có regularization nếu cần)
- Đánh giá: confusion matrix, precision/recall/F1, ROC-AUC
- Chọn threshold (không mặc định 0.5 nếu lệch lớp)
- Phân tích feature importance theo |coef|

### 3) So sánh và kết luận
- Khi nào dùng Linear vs Logistic?
- 5 lỗi sai phổ biến bạn gặp (ví dụ: leakage, scaling sai, metric sai)
