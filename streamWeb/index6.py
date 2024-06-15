import streamlit as st


# st.write("未使用表單時, slider/checkbox 值會立刻捉取")
# slider_val = st.slider("Form slider")
# checkbox_val = st.checkbox("Form checkbox")

# st.write("slider值: ", slider_val, "checkbox值:", checkbox_val)

# st.divider()

## event-drive的觀念
with st.container(height=300, border=True):
    st.write("未使用表單時, slider/checkbox 值會立刻捉取")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    st.write("slider值: ", slider_val, "checkbox值:", checkbox_val)


with st.form("my_form"):
    st.write("表單內, 需submit後, 值才會被記錄")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    ## 表單一定要有submit button
    submitted = st.form_submit_button("確認/提交")

    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("表單外")        