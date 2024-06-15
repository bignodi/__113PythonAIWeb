import streamlit as st

## st.write 直接支援markdown 語法
st.write("## Hello! **_World_**")

## Magic 直接寫
"Streamlit Magic ~~"

## st.markdown 就是指定用markdown
st.markdown("這是用 *st.streamlit* 寫出來的 **很** ***酷*** 喔.")
multi = '''
:red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
:gray[pretty] :rainbow[colors] and :blue-background[highlight] text.
'''

st.markdown(multi)

## st.caption
st.caption("這是st.caption 範例")

## st.divider() 畫分隔線
st.divider()

## st.subheader
st.subheader('這是subheader 的範例, 加上分隔線', divider="rainbow")

## st.code
st.markdown('這是st.code 程式碼顯示範例')
code = '''
def hello():
print("Hello,Streamlit!")
'''

st.code(code, language='python')


## 
import requests
from requests import Response

aqi_url = "https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
res:Response = requests.get(aqi_url)
