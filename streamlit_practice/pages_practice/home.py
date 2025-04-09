import streamlit as st

def home_page():
    st.title("🏠 홈 페이지")
    st.write(f"{st.session_state.get('username', '사용자')}님, 환영합니다!")

    if st.button("로그아웃"):
        st.session_state['logged_in'] = False
        st.success("로그아웃 되었습니다.")
        st.rerun()