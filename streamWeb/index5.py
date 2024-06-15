import streamlit as st

## 第一個bar_chart 可有可無
st.bar_chart({"data":[1,5,2,6,2,1]})

## 加上expander 收合功能
# with st.expander("expander 收合功能範例"):
#     st.write('''
#         用expander 
#         長條圖範例程式
#         可做收合功能
#     ''')
#     st.markdown('''
#     ### 內文用markdown 功能展示 ###
#     - list 1
#     - list 2
#     > **list 3**
#     ''')
#     st.image("https://static.streamlit.io/examples/dice.jpg")

## 預設為False
with st.expander(":green-background[expander 範例]",expanded=True):
    st.write('''
        用expander 
        長條圖範例程式
        可做收合功能
    ''')
    st.markdown('''
    ### 內文用markdown 功能展示 ###
    - list 1
    - list 2
    > **list 3**
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")