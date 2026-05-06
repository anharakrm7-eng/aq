
import streamlit as st

st.title("⚙️ الإعدادات")

st.text_input("اسم المحل")
st.text_input("رقم الهاتف")
st.text_input("العنوان")
st.text_input("الإدارة")

st.number_input("رأس المال")

st.subheader("إعدادات العيار العراقي")
st.number_input("نسبة العيار العراقي")

st.button("حفظ الإعدادات")
