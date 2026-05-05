import streamlit as st

st.sidebar.title("Sidebar")

name = st.sidebar.text_input("Enter Product Name")
selecteCategory = st.sidebar.selectbox("Select Category",['Electronics', 'Table',"Wooden","cloth","Fashion"])
price = st.sidebar.text_input("Enter Price")
if st.sidebar.button("Add Product"):
    st.write("SuccessFully added")
