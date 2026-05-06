
import streamlit as st

st.set_page_config(
    page_title="نظام إدارة الذهب الاحترافي",
    layout="wide"
)

st.title("💎 نظام إدارة محلات الذهب")

st.markdown("### الواجهة الرئيسية")

col1, col2, col3, col4 = st.columns(4)

col1.metric("رأس المال", "0")
col2.metric("الكاش", "0")
col3.metric("متوسط البيع", "0")
col4.metric("الربح اليومي", "0")

st.info("هذا إصدار تجريبي أولي للنظام الاحترافي")
