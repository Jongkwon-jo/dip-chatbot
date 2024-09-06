# LangSmith 추적을 설정합니다. https://smith.langchain.com
# .env 파일에 LANGCHAIN_API_KEY를 입력합니다.
# !pip install -qU langchain-teddynote
import streamlit as st
from conversation_chain import EnglishConversationChain, SummaryChain, BlogChain
import os 

if "OPENAI_API_KEY" in os.environ:
    st.write("API 키가 설정되었습니다.")
else:
    st.error("API 키가 설정되지 않았습니다.")

# 사이트의 제목 입력
st.title("나만의 챗GPT!")

with st.sidebar:
    selected_model = st.selectbox("모델 선택", ['gpt-4o-mini', 'gpt-4o'], index=0 )

def generate_answer(mychain, question):
    # 답변을 출력할 빈 껍데기를 만든다.
    answer_container = st.empty()        

    # 답변을 요청
    answer = blog_chain.stream({"question": question})

    final_answer = ""
    for token in answer:
        # final_answer에 토큰을 추가
        final_answer += token
        # 답볍을 출력
        answer_container.markdown(final_answer)
        
# 사용자가 입력할 상황
question = st.chat_input("영어회화에 주어질 상황에 입력해 보세요.")

# request_btn이 클릭이 된다면...
if question:
    # 1) 사용자의 입력을 먼저 출력
    st.chat_message("user").write(question)

    with st.chat_message("ai"):
        summary_chain = SummaryChain().create_chain()
        blog_chain = BlogChain().create_chain()
        english_chain = EnglishConversationChain().create_chain()

        generate_answer(summary_chain, question)
        generate_answer(blog_chain, question)
        generate_answer(english_chain, question)
