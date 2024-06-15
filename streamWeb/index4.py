import streamlit as st
import time

# with st.empty():
#     for sec in range(60):
#         st.write(f"{sec} seconds have passed")
#         time.sleep(1)
#     st.write("1 minute over")

placeholder = st.empty()

with placeholder:
    for sec in range(30):
        st.write(f"{sec} seconds have passed")
        time.sleep(1)
    st.write("1 minute over")

time.sleep(5)
placeholder.empty()