import streamlit as st
from pages_practice.login import login_ui
from pages_practice.home import home_page

# 세션 초기화
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

st.set_page_config(page_title="간단 로그인 페이지", page_icon="🔐", layout="centered")

if st.session_state['logged_in']:
    home_page()
else:
    login_ui()
