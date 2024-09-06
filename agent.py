# 필요한 모듈 import
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor

def create_agent(k=5):
    ### 1-1. Search 도구 ###
    # TavilySearchResults 클래스의 인스턴스를 생성합니다
    # k=5은 검색 결과를 5개까지 가져오겠다는 의미입니다
    search = TavilySearchResults(k=k)

    ### 1-3. tools 리스트에 도구 목록을 추가합니다 ###
    tools = [search]

    ########## 2. LLM 을 정의합니다 ##########
    # LLM 모델을 생성합니다.
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    ########## 3. Prompt 를 정의합니다 ##########

    # hub에서 prompt를 가져옵니다 - 이 부분을 수정할 수 있습니다!
    prompt = hub.pull("hwchase17/openai-functions-agent")

    ########## 4. Agent 를 정의합니다 ##########

    # OpenAI 함수 기반 에이전트를 생성합니다.
    # llm, tools, prompt를 인자로 사용합니다.
    agent = create_openai_functions_agent(llm, tools, prompt)

    ########## 5. AgentExecutor 를 정의합니다 ##########

    # AgentExecutor 클래스를 사용하여 agent와 tools를 설정하고, 상세한 로그를 출력하도록 verbose를 True로 설정합니다.
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor