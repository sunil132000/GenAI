import  streamlit as st

st.title("Calculator")
price = st.number_input('Enter Price')
discountPercentage =st.slider('Enter Discount',0,50)
if st.button("Calculate"):
    discount = price * discountPercentage /100
    discounted_price = price - discount
    st.write(f"Discounted Price :{discounted_price}")
