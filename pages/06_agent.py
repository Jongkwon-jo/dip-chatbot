from langchain_core.messages import ChatMessage
from agent import create_agent
import streamlit as st

st.title("검색이 가능한 챗봇")

# 대화 기록이 없다면, chat_history라는 키로 빈 대화를 저장하는 list를 생성
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# chain을 초기화
if "search_agent" not in st.session_state:
    st.session_state["search_agent"] = None

def add_history(role, message):
    st.session_state["chat_history"].append(ChatMessage(role=role, content=message))
    
def print_history():
    for chat_message in st.session_state["chat_history"]:
        # 메시지 출력(role: 누가 말한 메시지 인가?) .write(content: 메시지 내용)
        st.chat_message(chat_message.role).write(chat_message.content)

with st.sidebar:
    search_count  = st.number_input("검색 결과의 개수를 입력해주세요", min_value=1, max_value=10, value=5, step=1)

    # 설정이 완료 되었는지 확인하는 버튼
    confirm_btn = st.button("설정 완료")

# 파일이 업로드 되었을 때
if confirm_btn:
    st.session_state["search_agent"] = create_agent(k=search_count)

# 이전의 대화 내용들을 출력
print_history()

user_input = st.chat_input("궁금한 내용을 입력해 주세요")

if user_input:
    # 파일이 업로드가 된 이후
    if st.session_state["search_agent"]:
        search_agent = st.session_state["search_agent"]
        # 사용자의 질문을 출력합니다.
        st.chat_message("user").write(user_input)

        # AI의 답변을 출력합니다.
        with st.chat_message("ai"):
            # 스트리밍 답변을 출력할 빈 컨테이너를 만든다.
            chat_container = st.empty()

            # 사용자가 질문을 입력하면, 체인에 질문을 넣고 실행합니다.
            ai_answer = search_agent.invoke({"input": user_input})
            st.write(ai_answer["output"])
        
        # 대화 내용을 기록에 추가
        add_history("user", user_input) # 사용자의 질문
        add_history("ai", ai_answer["output"]) # 챗봇의 답변