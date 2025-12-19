# Lab 12 – Classification Models + XAI

## A) Mục tiêu
- So sánh nhiều mô hình phân lớp một cách công bằng
- Biết giải thích mô hình (XAI) thay vì chỉ báo điểm số

## B) Dataset
- Chọn dataset phân lớp (gợi ý: Pima/Churn/Fraud_Detection nếu có)
- Nếu lệch lớp: bắt buộc báo cáo imbalance + cách xử lý

## C) Nhiệm vụ bắt buộc

### 1) Huấn luyện & so sánh mô hình (tối thiểu 4)
- Decision Tree
- Naive Bayes
- 1 mô hình “nâng cao”: RandomForest / GradientBoosting / XGBoost (nếu được) / SVM
- 1 baseline: Logistic Regression (để so sánh)

### 2) Đánh giá đúng
- Confusion Matrix
- Precision / Recall / F1
- ROC-AUC (nếu binary)
- Nếu lệch lớp: thêm PR-AUC hoặc chú trọng Recall/F1

### 3) Tuning (tối thiểu 1 mô hình)
- GridSearchCV hoặc RandomizedSearchCV
- Báo cáo best params + cải thiện metric

### 4) XAI (bắt buộc)
- Global: feature importance (tree-based) hoặc permutation importance
- Local: giải thích 3 mẫu dự đoán (đúng/sai) bằng:
  - SHAP (ưu tiên nếu làm được) hoặc
  - LIME (nếu SHAP khó)

### 5) Kết luận
- Chọn mô hình cuối cùng + lý do (metric + interpretability + chi phí)
- Nêu 3 lỗi sai phổ biến bạn mắc khi phân lớp

## D) Output nộp
- Notebook: `project/notebooks/lab12_classifiers.ipynb`
- Notebook XAI: `project/notebooks/lab12_xai.ipynb`
- Report: `project/reports/lab12_report.md`
- Zip: `Lab12_HoTen_MaSV.zip`
