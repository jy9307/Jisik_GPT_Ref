import streamlit as st
import pandas as pd

#user_info.csv와 연결된 계정 정보
#user_info.csv만 수정하시면 됩니다.
user_info = {row["id"]: (row["pw"], row["auth"]) for _, row in pd.read_csv("user_info.csv", dtype={"id": str, "pw" :str}).iterrows()}


# 로그인 페이지
def login_page():
    st.markdown("## 🔐__반 친구들 반갑습니다!")
    st.markdown("✍️선생님이 알려준 아이디와 비밀번호로 로그인하세요.")
    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")

    login_button = st.button("로그인")

    if login_button:
        if username in user_info.keys() and user_info[username][0] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['auth'] = user_info[username][1]
            
            st.rerun()
        else:
            st.error("Invalid username or password")