import streamlit as st


st.title("計數器範例")
count = 0

## 和式碼只有跑一次 "加一"
# increment = st.button("加一")
# if increment:
#     count += 1

# st.write("Count=", count)



increment = st.button("加一")
stop = st.button("STOP!")

while not stop:
    if increment:
        count += 1
        st.write("Count=", count)




