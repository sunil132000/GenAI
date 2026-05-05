import streamlit as st

st.title("Simple Sales Dashboard")
selected_month = st.selectbox("select month",["January","February","March","April"])
sales ={
    "January":1200,
    "February":1500,
    "March":900,
    "April":2000
}

st.subheader("Sales Data")
st.metric(label=f"{selected_month} Sales", value=sales[selected_month])
st.bar_chart(list(sales.values()))