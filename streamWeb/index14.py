import streamlit as st

st.title("計數器範例:  用session_state記錄值/傳值 ")

if 'count' not  in st.session_state:
    st.session_state.count = 0

## 利用session_state event 去捉值
# increment = st.button("加一")
# st.write(increment)

# if increment:
#     st.session_state.count += 1

# st.write("Count=", st.session_state.count)


## 利用session_state event, 觀察session_state值
increment = st.button("加一", key="Incremnet")
st.write(st.session_state)

if increment:
    st.session_state.count += 1

st.write("Count=", st.session_state.count)
