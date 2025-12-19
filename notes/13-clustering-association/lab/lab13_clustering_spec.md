# Lab 13A – Phân cụm (Clustering)

## A) Mục tiêu
- Nhóm dữ liệu không nhãn thành các cụm có ý nghĩa
- Biết chọn K và đánh giá clustering

## B) Dataset
- Dataset số (numeric) hoặc đã encode/scale
- Nếu có nhiều feature: bắt buộc scale

## C) Nhiệm vụ bắt buộc
1) Tiền xử lý
- Missing/outlier cơ bản
- Scaling: StandardScaler hoặc MinMaxScaler

2) Thuật toán (tối thiểu 2)
- KMeans (bắt buộc)
- 1 thuật toán khác: Hierarchical / DBSCAN / GMM

3) Chọn số cụm & đánh giá
- Elbow + Silhouette (bắt buộc)
- (tuỳ) Davies-Bouldin

4) Trực quan hóa
- PCA/TSNE 2D để plot clusters
- Mô tả đặc trưng từng cụm (mean/median theo cụm)

5) Insight
- Đặt “tên” cho từng cụm và giải thích (3–6 dòng/cụm)

## D) Output
- Notebook: `project/notebooks/lab13_clustering.ipynb`
