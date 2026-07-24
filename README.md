# 🏦 Web App Thẩm định cho vay doanh nghiệp

## Giới thiệu

Web App được xây dựng nhằm hỗ trợ đánh giá sơ bộ khả năng cấp tín dụng cho doanh nghiệp dựa trên các chỉ tiêu tài chính và thông tin khoản vay. Ứng dụng giúp tự động tính toán các chỉ số quan trọng, chấm điểm tín dụng và đưa ra kết luận hỗ trợ quyết định cho vay.

---

## Chức năng

- Nhập chỉ tiêu ROA (%)
- Nhập chỉ tiêu ROE (%)
- Nhập lợi nhuận sau thuế (LNST)
- Nhập giá trị tài sản bảo đảm (TSĐB)
- Nhập số tiền vay
- Nhập thời gian vay
- Nhập lãi suất cho vay
- Tính tỷ lệ cho vay trên tài sản bảo đảm (LTV)
- Tính tiền lãi và tổng số tiền phải thanh toán
- Chấm điểm tín dụng doanh nghiệp
- Đưa ra kết luận:
  - ✅ Chấp thuận
  - ⚠️ Cần xem xét
  - ❌ Từ chối
- Hiển thị biểu đồ trực quan kết quả đánh giá

---

## Công nghệ sử dụng

- Python 3
- Streamlit
- Pandas
- Plotly

---

## Cấu trúc dự án

```
Loan-App/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Cài đặt

Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

Chạy ứng dụng:

```bash
streamlit run app.py
```

---

## Dữ liệu đầu vào

Người dùng nhập các thông tin sau:

- ROA (%)
- ROE (%)
- Lợi nhuận sau thuế
- Giá trị tài sản bảo đảm
- Số tiền vay
- Thời gian vay
- Lãi suất cho vay

---

## Kết quả đầu ra

Ứng dụng sẽ tính toán và hiển thị:

- Điểm tín dụng
- Tỷ lệ LTV
- Tiền lãi phải trả
- Tổng số tiền phải thanh toán
- Kết luận thẩm định
- Biểu đồ đánh giá

---

## Tác giả

- Họ và tên: Nguyễn Trần Thiên Hương
- Trường: (Điền tên trường của bạn)
- Môn học: (Điền tên môn học)
- Năm thực hiện: 2026
