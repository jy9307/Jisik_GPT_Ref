import streamlit as st

# 제목
st.title("나의 취미 소개")

# 두 열로 나누기
col1, col2 = st.columns(2)

# 왼쪽: 영화 보기
with col1:
    with st.container(border=True):
        st.markdown("### 🎬 영화 보기")
        st.write("저는 영화 보는 걸 정말 좋아해요. 주로 주말 저녁마다 시간을 내서 극장에 가거나 집에서 스트리밍으로 보는 것을 즐깁니다.")
        st.write("특히 감독의 연출력이나 이야기 전개를 집중해서 보는 걸 좋아하고, 짙은 여운이 남는 영화를 사랑합니다.")
        st.image("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="영화관 가고싶다", use_container_width=True)

# 오른쪽: 책 읽기
with col2:
    with st.container(border=True):
        st.markdown("### 📚 책 읽기")
        st.write("책 읽는 것은 정말 즐거운 일입니다. 조용한 카페나 자기 전 침대에서 읽는 걸 좋아해요.")
        st.write("책 속에서 이전에 얻지 못한 새로운 통찰을 얻는 게 정말 흥미롭고, 때론 이를 통해 세상을 새롭게 보곤 합니다.")
        st.image("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f", caption="도서관냄새는 최고에요", use_container_width=True)
