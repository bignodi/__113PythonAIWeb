import streamlit as st

st.write("未使用表單時, slider/checkbox 值會立刻捉取")
slider_val = st.slider("Form slider")
checkbox_val = st.checkbox("Form checkbox")

st.write("slider值: ", slider_val, "checkbox值:", checkbox_val)