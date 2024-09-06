from langchain_core.messages import ChatMessage
from rag import naver_news_crawling, create_stuff_summary_chain
import streamlit as st

st.title("네이버 뉴스 요약")

# 대화 기록이 없다면, chat_history라는 키로 빈 대화를 저장하는 list를 생성
if "summary_history" not in st.session_state:
    st.session_state["summary_history"] = []

# chain을 초기화
if "news_summary_chain" not in st.session_state:
    st.session_state["news_summary_chain"] = None

# 대화 기록에 채틱을 추가
def add_history(message):
    st.session_state['summary_history'].append(message)

def print_history():
    for chat_message in st.session_state["summary_history"]:
        # 메시지 출력(role: 누가 말한 메시지 인가?) .write(content: 메시지 내용)
        st.markdown(chat_message)

with st.sidebar:
    naver_news_url  = st.text_input("네이버 뉴스 URL을 입력해주세요")

    # 설정이 완료 되었는지 확인하는 버튼
    confirm_btn = st.button("요약 시작")

@st.cache_resource(show_spinner="URL을 분석 중입니다...")
def embed_file(url):
    docs = naver_news_crawling(url)
    return docs

# 이전까지의 요약을 출력
print_history()

# 파일이 업로드 되었을 때
if confirm_btn:
    # URL 크롤링
    docs = embed_file(naver_news_url)
    # 요약 체인 생성
    summary_chain = create_stuff_summary_chain()
    final_summary = summary_chain.invoke({"context": docs})
    st.markdown(f"### 다음은 {naver_news_url} 의 요약본입니다.")
    # 요약본 출력
    st.markdown(final_summary)
    
    add_history(f"### 다음은 {naver_news_url} 의 요약본입니다.")
    # 히스토리에 추가
    add_history(final_summary)