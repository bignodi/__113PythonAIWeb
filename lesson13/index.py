import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st

## 改寫為 將捉取ubike module 拆出去
## 這裡只做頁面顯示處理
import source
from source import Root

## 用pandas 呈現資料
import pandas as pd

#####################################################
# st.write("**改寫拆解版本**")

# data_str = source.download_youbike()
# root = Root.model_validate_json(data_str)
# data = root.model_dump()

# def ijk(value):
#     return value['行政區']

# areas:list[str] = list(set(map(ijk,data)))

# option = st.selectbox("請選擇行政區",areas)
# st.write("您選擇:", option)


#####################################################
## 加上錯誤訊息處理, 不讓異常連線影響程式
## 可到source.py 把url 改掉測試
# st.write("**改寫拆解版本+異常處理**")
# try:
#     data_str = source.download_youbike()
# except Exception as e:
#     st.error(e)
# else:
#     root = Root.model_validate_json(data_str)
#     data = root.model_dump()

#     def ijk(value):
#         return value['行政區']
    
#     areas:list[str] = list(set(map(ijk,data)))

#     option = st.selectbox("請選擇行政區",areas)
#     st.write("您選擇:", option)                              


#####################################################
## map function改寫為lambda 及
# st.write("**改寫拆解版本+異常處理+sidebar**")
# try:
#     data_str = source.download_youbike()
# except Exception as e:
#     st.error(e)
# else:
#     root = Root.model_validate_json(data_str)
#     data = root.model_dump()

#     areas:list[str] = list(set(map(lambda value:value['行政區'],data)))

#     with st.sidebar:
#         st.selectbox(":orange[請選擇行政區:]",options=areas)


#####################################################
## 右方顯示區域, 並指定進入時出現淡水區
# st.write("**改寫拆解版本+異常處理+sidebar**")
# try:
#     data_str = source.download_youbike()
# except Exception as e:
#     st.error(e)
# else:
#     root = Root.model_validate_json(data_str)
#     data = root.model_dump()

#     areas:list[str] = list(set(map(lambda value:value['行政區'],data)))

#     ## 右邊出現選擇區域
#     def area_change():
#         st.write(st.session_state.sarea)

#     if 'sarea' not in st.session_state:
#         st.session_state.sarea = '淡水區'

#     with st.sidebar:
#         st.selectbox(":orange[請選擇行政區:]",options=areas,on_change=area_change, key='sarea')

#     st.write(st.session_state)

#####################################################
# try:
#     data_str = source.download_youbike()
# except Exception as e:
#     st.error(e)
# else:
#     root = Root.model_validate_json(data_str)
#     data = root.model_dump()

#     areas:list[str] = list(set(map(lambda value:value['行政區'],data)))


#     ## 右邊出現選擇區域, 並將該區域站點資料列出
#     def area_change():
#         sarea_name = st.session_state.sarea
#         st.write(sarea_name)
#         display_data = []
#         for item in data:
#             if item['行政區'] == sarea_name:
#                 display_data.append(item)
#         st.write(display_data)

    
#     with st.sidebar:
#         st.selectbox(":orange[請選擇行政區:]",options=areas,on_change=area_change, key='sarea')

#     st.title("台北市youbike各行政區站點資料")


#####################################################
## 用table 顯示站點資料, 並處理因table 顯示資料造成 title 浮動的問題 (用container把table包起來)
# try:
#     data_str = source.download_youbike()
# except Exception as e:
#     st.error(e)
# else:
#     root = Root.model_validate_json(data_str)
#     data = root.model_dump()
#     areas:list[str] = list(set(map(lambda value:value['行政區'],data)))


#     st.title("台北市youbike各行政區站點資料")
#     #tableContainer = st.container()
#     ## table 加上捲動軸
#     tableContainer = st.container(height=500, border=False)

#     ## 右邊出現選擇區域, 並將該區域站點資料列出,  用table 顯示
#     def area_change():
#         sarea_name = st.session_state.sarea
#         display_data = []
#         ## 資料結構是 list 內有dict 
#         for item in data:
#             if item['行政區'] == sarea_name:
#                 display_data.append(item)
#         with tableContainer:
#             st.subheader(sarea_name)
#             # table 顯示
#             #st.table(data=display_data)
#             #改成dataframe顯示
#             st.dataframe(data=display_data)

    
#     with st.sidebar:
#         st.selectbox(":orange[請選擇行政區:]",options=areas,on_change=area_change, key='sarea')


#####################################################
## 用pandas 處理資料呈現, 並過濾要顯示的欄位
try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    areas:list[str] = list(set(map(lambda value:value['行政區'],data)))


    st.title("台北市youbike各行政區站點資料")
    #tableContainer = st.container()
    ## table 加上捲動軸
    #tableContainer = st.container(height=500, border=False)
    ## 顯示圖表, 把height拿掉
    tableContainer = st.container(border=False)

    ## 右邊出現選擇區域, 並將該區域站點資料列出,  用table 顯示
    def area_change():
        sarea_name = st.session_state.sarea
        display_data = []
        ## 資料結構是 list 內有dict 
        for item in data:
            if item['行政區'] == sarea_name:
                display_data.append(item)
        with tableContainer:
            st.subheader(sarea_name)
            ## table 顯示
            #st.table(data=display_data)
            ## 改成dataframe顯示
            #st.dataframe(data=display_data)
            ## 用pandas顯示
            #df1 = pd.DataFrame(display_data)
            ## 用pandas顯示, 並過濾欄位
            df1 = pd.DataFrame(display_data, 
                               columns=['站點名稱','日期時間','地址','總數','可借','可還'])
            st.dataframe(data=df1)

            ## 圖表顯示, 可借數
            df2 = pd.DataFrame(display_data, 
                               columns=['站點名稱','總數','可借'])
            st.scatter_chart(df2, x='站點名稱', y='總數', size='可借')

            ## 圖表顯示, 可還數
            df3 = pd.DataFrame(display_data, 
                               columns=['站點名稱','總數','可還'])
            st.scatter_chart(df3, x='站點名稱', y='可還', size='可還', color="#ff0000")



    
    with st.sidebar:
        st.selectbox(":orange[請選擇行政區:]",options=areas,on_change=area_change, key='sarea')


