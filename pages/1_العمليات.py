import streamlit as st

st.title("📒 العمليات والتداولات")

tab1, tab2 = st.tabs(["بيع", "شراء"])

with tab1:
    st.subheader("إضافة فاتورة بيع")

    customer = st.text_input("اسم الزبون")
    pieces = st.number_input("عدد القطع", min_value=1, value=1)

    for i in range(int(pieces)):
        st.markdown(f"### القطعة {i+1}")
        st.text_input("نوع القطعة", key=f"type_{i}")
        st.number_input("الوزن", key=f"weight_{i}")
        st.selectbox("العيار", [9,10,12,14,18,21,22,24,"عراقي"], key=f"karat_{i}")
        st.number_input("سعر الخام", key=f"raw_{i}")
        st.number_input("الأجور", key=f"wage_{i}")
        st.number_input("السعر الإجمالي", key=f"total_{i}")

    st.number_input("الواصل")
    st.text_area("ملاحظات")

    st.button("حفظ الفاتورة")

with tab2:
    st.subheader("إضافة شراء")

    st.text_input("اسم الزبون")
    st.text_input("نوع القطعة")
    st.number_input("الوزن")
    st.selectbox("العيار", [9,10,12,14,18,21,22,24,"عراقي"])
    st.number_input("السعر الإجمالي")
    st.text_area("ملاحظات")

    st.button("حفظ الشراء")
