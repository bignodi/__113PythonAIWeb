import streamlit as st

## sidebar 範例
## 方式一：object notation （直接寫object 名稱, e.g. selectbox）
# select_val = st.sidebar.selectbox(
#      "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# #st.write("選擇的方式:", select_val)

# ## 方式二: with notation (用with)
# with st.sidebar:
#     radio_val = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

# st.write("選擇的方式:", select_val, ",", radio_val)

## 部分功能無法用object notation , 就只能用with (st.echo, st.spinner, and st.toast)


with st.sidebar:
    select_val = st.sidebar.selectbox(
        "How would you like to be contacted?",
            ("Email", "Home phone", "Mobile phone")
        )
    
    radio_val = ""
    if select_val == "Email":
        with st.form("my_form2"):
            if select_val == "Email":
                radio_val = st.radio(
                    "Choose a shipping method",
                ("Standard (5-15 days)", "Express (2-5 days)")
                )
            
            else:
                radio_val = ""
            
            st.form_submit_button("確定")
       
        
st.write("選擇的方式:", select_val, ",", radio_val)
