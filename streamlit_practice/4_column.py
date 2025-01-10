import streamlit as st

col1, col2 = st.columns(2)

with col1 :
    st.markdown("# 1열")
    st.write("1열입니다.")

with col2 :
    st.markdown("# 2열")
    st.write("2열입니다.")