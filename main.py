import streamlit as st
from login import login_page
from feedback import feedback

# 세션 초기화
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    feedback()
else:
    login_page()
