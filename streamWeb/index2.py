import streamlit as st


col1,col2 = st.columns([2,1])

with col1:
    st.title("這是欄位1 Header")
    st.header("這是欄位1 Header")
    st.subheader("這是欄位1 subheader")
    
with col2:
    st.title("這是欄位2 Header")
    st.header("這是欄位2 Header")
    st.subheader("這是欄位2 subheader")

