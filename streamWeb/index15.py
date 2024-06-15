import streamlit as st

st.title("計數器範例: by callback")

if 'count' not  in st.session_state:
    st.session_state.count = 0

## 利用callback (按下按鈕時, 執行function)
def increment_counter():
    st.session_state.count += 1

#st.button("加一", key="Increment", on_click=increment_counter)
st.button("加一", on_click=increment_counter)

st.write("Count=", st.session_state.count)