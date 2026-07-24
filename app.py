import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 WEB APP THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

st.markdown("---")

col1,col2=st.columns(2)

with col1:

    roa=st.number_input(
        "ROA (%)",
        value=5.0
    )

    roe=st.number_input(
        "ROE (%)",
        value=15.0
    )

    lnst=st.number_input(
        "Lợi nhuận sau thuế (VNĐ)",
        value=5000000000.0,
        step=100000000
    )

    tsdb=st.number_input(
        "Giá trị tài sản bảo đảm",
        value=10000000000.0,
        step=100000000
    )

with col2:

    tien_vay=st.number_input(
        "Số tiền vay",
        value=5000000000.0,
        step=100000000
    )

    thoi_gian=st.number_input(
        "Thời gian vay (năm)",
        value=5
    )

    lai_suat=st.number_input(
        "Lãi suất (%/năm)",
        value=9.5
    )

st.markdown("---")

if st.button("THẨM ĐỊNH"):

    ltv=tien_vay/tsdb*100

    tien_lai=tien_vay*lai_suat/100*thoi_gian

    tong=tien_vay+tien_lai

    diem=0

    # ROA
    if roa>=8:
        diem+=20
    elif roa>=5:
        diem+=15
    elif roa>=2:
        diem+=10

    # ROE
    if roe>=20:
        diem+=20
    elif roe>=15:
        diem+=15
    elif roe>=10:
        diem+=10

    # LNST
    if lnst>=10000000000:
        diem+=20
    elif lnst>=5000000000:
        diem+=15
    elif lnst>0:
        diem+=10

    # LTV
    if ltv<=60:
        diem+=20
    elif ltv<=80:
        diem+=10

    # Lãi suất
    if lai_suat<=8:
        diem+=20
    elif lai_suat<=10:
        diem+=15
    else:
        diem+=10

    if diem>=80:
        ket_luan="🟢 CHẤP THUẬN"

    elif diem>=60:
        ket_luan="🟡 CẦN XEM XÉT"

    else:
        ket_luan="🔴 TỪ CHỐI"

    st.success("Kết quả thẩm định")

    c1,c2,c3=st.columns(3)

    c1.metric("Điểm tín dụng",f"{diem}/100")

    c2.metric("LTV",f"{ltv:.2f}%")

    c3.metric("Tổng tiền phải trả",f"{tong:,.0f} VNĐ")

    st.write("### Kết luận")

    st.header(ket_luan)

    bang=pd.DataFrame({

        "Chỉ tiêu":[
            "ROA",
            "ROE",
            "LTV",
            "Điểm"
        ],

        "Giá trị":[
            roa,
            roe,
            ltv,
            diem
        ]

    })

    fig=go.Figure()

    fig.add_trace(

        go.Bar(

            x=bang["Chỉ tiêu"],

            y=bang["Giá trị"]

        )

    )

    st.plotly_chart(fig,use_container_width=True)

    st.dataframe(bang)
