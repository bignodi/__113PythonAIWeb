import streamlit as st
import numpy as np

#st.write("This is outside the container")

# with st.container(border=True):
#     st.write("This is inside the container")
#     st.bar_chart(np.random.randn(50,3))

# st.write("This is outside the container")

container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

container.write("This is inside too")