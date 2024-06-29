import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st

## 改寫為 將捉取ubike module 拆出去
## 這裡只做頁面顯示處理
import source
from source import Root

st.write("**改寫拆解版本**")

data_str = source.download_youbike()
root = Root.model_validate_json(data_str)
data = root.model_dump()

def ijk(value):
    return value['行政區']

areas:list[str] = list(set(map(ijk,data)))

option = st.selectbox("請選擇行政區",areas)
st.write("您選擇:", option)