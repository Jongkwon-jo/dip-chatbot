import streamlit as st
import os

st.title("API 설정")

st.markdown("""
* OpenAI API 키 발급 방법은 아래 링크를 참고해 주세요!
* [발급방법](https://openai.com)
"""
)

# API 키 입력
api_key = st.text_input("API 키 입력", type="password")
search_api_key = st.text_input("Tavily Search API 키 입력(검색용)", type="password")

# 설정 확인 버튼
confirm_btn = st.button("설정하기", key="api_key")

if confirm_btn:
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        st.write(f"API 키가 설정되었습니다: `{api_key[:10]}************`")
    if search_api_key:
        os.environ["TAVILY_API_KEY"] = search_api_key
        st.write(f"API 키가 설정되었습니다: `{search_api_key[:10]}************`")
