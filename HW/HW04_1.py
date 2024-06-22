## call back 寫法

import streamlit as st

def chkBMI(bmi):
    if bmi < 18.5:
        return "體重過輕"
    elif bmi >= 18.5 and bmi < 24:
        return "正常範圍"
    elif bmi >=24 and bmi < 27 :
        return "過重"
    elif bmi >=27 and bmi < 30:
        return "輕度肥胖"
    elif bmi >=30 and bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"


st.header("BMI值計算")
st.divider()

st.markdown("**BMI值計算公式:**    BMI = 體重(公斤) / 身高$^2$(公尺$^2$)")
st.markdown("例如：一個52公斤的人，身高是155公分，則BMI為 :")
st.markdown("52(公斤)/1.55 $^2$ ( 公尺$^2$ )= 21.6")
st.markdown("體重正常範圍為  BMI=18.5～24")

st.markdown("**:violet[快看看自己的BMI是否在理想範圍吧!]**")

bmi =0

with st.form(key='my_form'):
    height = st.number_input(label="身高")
    weight = st.number_input(label="體重")
    submit = st.form_submit_button(label="開始計算")

if submit:
    bmi = round(weight/(height/100) ** 2, 3)

#st.write(weight)
#st.write(height)
txt1 = str(bmi)
st.write(f"你的BMI為   {txt1}")
#st.write(txt1)
result = chkBMI(bmi)
st.write(result)



