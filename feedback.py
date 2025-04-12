import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import os

load_dotenv()



llm = ChatOpenAI(
    temperature=0.5
)

mid_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    당신은 글쓰기 도우미입니다. 
    학생이 현재까지 쓴 글을 읽고, 더 나은 글을 쓸 수 있도록 쉬운 말로 피드백을 제공해주세요.
    다만, 학생이 보고 베낄 수 있는 예시를 제공하지는 말아주세요.
    """),
    ("human", "이름 : {name}, 현재까지 쓴 내용 : {input}")
])

final_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    당신은 글쓰기 채점 및 피드백 도우미입니다. 
    학생이 현재까지 쓴 글을 읽고, 최저 1점에서 최대 5점의 점수를 제공해주세요.
    그리고 나서 다음과 같은 순서로 피드백을 제공해주세요.
     
    1) 점수 배점 이유
    2) 글이 더 나아지기 위해 필요한 피드백
    """),
    ("human", "이름 : {name}, 최종 제출 내용 : {input}")
])

mid_chain = (
    mid_prompt
    | llm
    | StrOutputParser()
)

final_chain = (
    final_prompt
    | llm
    | StrOutputParser()
)



# 학생 UI
def student_feedback():

    with open("today_topic.txt", "r", encoding="utf-8") as f:
        topic = f.read()

    st.set_page_config(page_title="글쓰기 자동 피드백 도우미", layout="wide")
    st.title("글쓰기 자동 피드백 도우미")

    try:

        st.markdown(f"#### 오늘의 주제: {topic}")
    except FileNotFoundError:
        st.markdown("#### 오늘의 주제: 아직 설정되지 않았습니다.")

    col1, col2 = st.columns(2)

    with col1:
        container1 = st.container(border=True)
        mid_feedback_button = st.button("지금까지의 글 점검하기", type="secondary", use_container_width=True)
        container2 = st.container(border=True, height=200)
        
        with container1:
            name = st.session_state['username']
            st.markdown(f"이름 : {name}")
            content = st.text_area("자신이 쓴 글을 입력해주세요", height=200)

        with container2:
            st.markdown("#### 중간 피드백")
            if mid_feedback_button:

                mid_feedback_result = mid_chain.invoke({"name": name, "input": content})
                st.markdown(mid_feedback_result)

    with col2:
        final_feedback_button = st.button("최종 제출", type="primary", use_container_width=True)
        container1 = st.container(border=True, height=500)

        with container1:
            st.markdown("#### 최종 피드백")
            if final_feedback_button:
                # final_chain은 외부에서 정의된 것으로 가정
                final_feedback_result = final_chain.invoke({"name": name, "input": content})
                st.markdown(final_feedback_result)

                # 오늘 날짜 (YYMMDD 형식)
                today = datetime.now().strftime("%y%m%d")  # 예: 250409

                # 데이터 구성
                new_data = {
                    "날짜": today,
                    "주제" : topic,
                    "이름": name,
                    "제출 답변": content,
                    "인공지능 피드백": final_feedback_result
                }

                # 기존 데이터 로드 (파일이 없으면 빈 DataFrame 생성)
                try:
                    df = pd.read_excel("student_answer.xlsx")
                except FileNotFoundError:
                    df = pd.DataFrame(columns=["날짜", "주제", "이름", "제출 답변", "인공지능 피드백"])

                # 새로운 데이터 추가
                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

                # Excel 파일로 저장
                df.to_excel("student_answer.xlsx", index=False)
                st.success("선생님에게 제출이 완료되었습니다!")

def teacher_feedback():
    st.set_page_config(page_title="교사 관리 페이지", layout="wide")
    st.title("교사 관리 페이지")

    # 오늘의 주제 표시 및 변경
    topic_file = "today_topic.txt"
    if os.path.exists(topic_file):
        with open(topic_file, "r", encoding="utf-8") as f:
            topic = f.read()
    else:
        topic = ""

    today_topic = st.text_input("#### 오늘의 주제:", value=topic)

    if st.button("오늘의 주제 변경"):
        with open(topic_file, "w", encoding="utf-8") as f:
            f.write(today_topic)
        st.success("오늘의 주제가 변경되었습니다.")
        st.rerun()

    if st.button("제출 확인용 새로고침"):
        st.rerun()

    # student_answer.xlsx 파일 로드
    excel_file = "student_answer.xlsx"
    if os.path.exists(excel_file):
        df = pd.read_excel(excel_file)

        if df.empty:
            st.warning("아직 제출된 데이터가 없습니다.")
        else:
            st.markdown("### 학생 제출 목록")

            # 🔍 열 필터 기능
            with st.expander("🔍 열 필터"):
                filter_columns = ["이름", "주제"]
                for col in filter_columns:
                    unique_values = df[col].dropna().unique().tolist()
                    selected_values = st.multiselect(f"{col} 필터", unique_values, default=unique_values)
                    df = df[df[col].isin(selected_values)]

            # 📥 엑셀 파일 다운로드 버튼
            with open(excel_file, "rb") as f:
                excel_data = f.read()
            st.download_button(
                label="📥 전체 제출 목록 다운로드 (.xlsx)",
                data=excel_data,
                file_name="student_answer.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            # 🧹 파일 초기화 기능
            if st.button("⚠️ 모든 제출 데이터 초기화"):
                confirm = st.checkbox("정말 초기화하시겠습니까? 이 작업은 되돌릴 수 없습니다.")
                if confirm:
                    empty_df = pd.DataFrame(columns=["날짜", "주제", "이름", "제출 답변", "인공지능이 준 피드백"])
                    empty_df.to_excel(excel_file, index=False)
                    st.success("제출 목록이 초기화되었습니다.")
                    st.rerun()

            # 데이터프레임 표시
            st.dataframe(df, use_container_width=True)
    else:
        st.warning("student_answer.xlsx 파일이 없습니다. 학생이 제출한 데이터가 아직 없습니다.")

# 메인 함수
def feedback():
    # auth에 따라 UI 분기
    auth = st.session_state.get('auth', 'student')  # 기본값은 student
    if auth == "student":
        student_feedback()
    elif auth == "teacher":
        teacher_feedback()
    else:
        st.error("잘못된 권한입니다. auth 값이 'student' 또는 'teacher'여야 합니다.")