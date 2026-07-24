import streamlit as st
import pandas as pd

st.set_page_config(page_title="Thẩm Định Cho Vay Doanh Nghiệp", layout="wide")

# Thêm CSS để giới hạn chiều cao khung Banner (ví dụ: tối đa 300px)
st.markdown(
    """
    <style>
    .banner-img img {
        width: 100%;
        height: 400px; /* Hoặc 400px tùy bạn chọn */
        object-fit: cover; /* Tự cắt viền thừa, giữ đúng tỷ lệ hình ảnh */
        border-radius: 8px; /* Bo tròn góc nhẹ cho đẹp mắt */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Đặt ảnh vào trong một div có class banner-img
st.markdown('<div class="banner-img">', unsafe_allow_html=True)
st.image("logo.jpg")
st.markdown('</div>', unsafe_allow_html=True)

# Cấu hình trang
st.set_page_config(page_title="Thẩm Định Cho Vay Doanh Nghiệp", layout="wide")

st.title("🏦 Hệ Thống Thẩm Định Cho Vay Doanh Nghiệp")
st.write("Nhập thông tin tài chính và thông tin khoản vay để phân tích rủi ro sơ bộ.")

st.divider()

# Chia cột nhập liệu
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Chỉ số Tài chính Doanh nghiệp")
    roa = st.number_input("ROA (%)", value=5.0, step=0.1)
    roe = st.number_input("ROE (%)", value=12.0, step=0.1)
    lnst = st.number_input("Lợi nhuận sau thuế - LNST (Tỷ VNĐ)", value=2.5, step=0.1)
    tsdb = st.number_input("Giá trị Tài sản bảo đảm - TSĐB (Tỷ VNĐ)", value=10.0, step=0.5)

with col2:
    st.subheader("2. Đề xuất Khoản vay")
    so_tien_vay = st.number_input("Số tiền đề nghị vay (Tỷ VNĐ)", value=6.0, step=0.5)
    thoi_gian_vay = st.number_input("Thời gian vay (Tháng)", value=12, min_value=1)
    lai_suat = st.number_input("Lãi suất cho vay (%/năm)", value=9.5, step=0.1)

st.divider()

# Tính toán các chỉ số thẩm định
# 1. Hệ số LTV (Loan to Value)
ltv = (so_tien_vay / tsdb * 100) if tsdb > 0 else 0

# 2. Ước tính nghĩa vụ trả nợ hàng tháng (Gốc đều + Lãi tháng đầu tiên)
goc_hang_thang = (so_tien_vay * 10**9) / thoi_gian_vay
lai_thang_dau = (so_tien_vay * 10**9) * (lai_suat / 100 / 12)
tong_tra_thang_dau = goc_hang_thang + lai_thang_dau

# 3. Khả năng bao phủ từ LNST hàng tháng
lnst_hang_thang = (lnst * 10**9) / 12
kha_nang_tra_no = (lnst_hang_thang / tong_tra_thang_dau) if tong_tra_thang_dau > 0 else 0

# Hiển thị kết quả
st.subheader("📊 Kết Quả Phân Tích & Đánh Giá")

m1, m2, m3 = st.columns(3)
m1.metric("Tỷ lệ LTV (Vay / TSĐB)", f"{ltv:.1f}%")
m2.metric("Nghĩa vụ trả nợ tháng đầu", f"{tong_tra_thang_dau / 10**6:,.0f} Triệu VNĐ")
m3.metric("Độ bao phủ LNST / Nợ tháng", f"{kha_nang_tra_no:.2f} lần")

# Đánh giá rủi ro sơ bộ
st.subheader("📝 Kết luận Thẩm định Sơ bộ")

canh_bao = []
if ltv > 70:
    canh_bao.append("⚠️ Tỷ lệ LTV vượt mức an toàn thông thường (> 70%).")
if roa < 2.0:
    canh_bao.append("⚠️ Hiệu quả sử dụng tài sản (ROA) thấp (< 2%).")
if roe < 5.0:
    canh_bao.append("⚠️ Tỷ suất sinh lời trên vốn chủ sở hữu (ROE) yếu (< 5%).")
if kha_nang_tra_no < 1.0:
    canh_bao.append("⚠️ Lợi nhuận sau thuế hàng tháng không đủ bao phủ nghĩa vụ trả nợ gốc + lãi.")

if not canh_bao:
    st.success("✅ **Hồ sơ đạt điều kiện thẩm định sơ bộ.** Đề xuất tiếp tục chuyển sang bước thẩm định chi tiết dòng tiền.")
else:
    st.warning("⚠️ **Hồ sơ có dấu hiệu rủi ro cao:**")
    for cb in canh_bao:
        st.write(cb)
