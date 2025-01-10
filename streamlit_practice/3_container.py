import streamlit as st

container_1 = st.container(border=True , height = 200)
container_2 = st.container(border=True , height = 200)

with container_1 :
    st.write("컨테이너 1")

with container_2 :
    st.write("컨테이너 2")