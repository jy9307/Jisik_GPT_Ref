import streamlit as st

USER_DB = {
    "jaylee": "1234",
    "guest": "pass"
}

def login_ui():
    st.title("🔐 로그인")
    st.write("아이디와 비밀번호를 입력하세요")

    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")
    login_btn = st.button("로그인")

    if login_btn:
        if username in USER_DB and USER_DB[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success("✅ 로그인 성공! 홈으로 이동합니다.")
            st.rerun()
        else:
            st.error("❌ 아이디 또는 비밀번호가 틀렸습니다.")