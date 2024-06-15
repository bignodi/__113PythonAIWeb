import streamlit as st

## 前端 叫cookie (在browser內); 後端 叫session
## st.session_state
## 市面主流用 callback 做

st.write(st.session_state)

if 'robert' not in st.session_state:
    ## subscript
    st.session_state['robert'] = 30

st.write(st.session_state)

## .運算子
st.session_state.robert = 50

st.write(st.session_state)

