from langchain_core.prompts import PromptTemplate
from base_chain import BaseConversationChain

class EnglishConversationChain(BaseConversationChain):
    def create_prompt(self):
        template = """
        당신은 영어를 가르치는 10년차 영어 선생님입니다. 주어진 상황에 맞는 영어 회화를 작성해 주세요.
        양식은 Example을 참고하여 작성해 주세요.

        #상황:
        {question}

        #Example:
        **영어 회화**
        - Teacher: "I noticed you've been struggling with your English test preparations.
        - Student: "I’m having trouble with grammar and vocabulary. It’s overwhelming."
        - Teacher: "That’s completely normal. Let’s break it down together."
        - Student: "That sounds good. I really need to understand verb tenses better."
        - Teacher: "Great! We can start with present simple and present continuous."

        **한글 해석**
        - 선생님: "영어 시험 준비로 어려움을 겪고 있다는 것을 알았습니다."
        - 학생: "문법과 어휘에 문제가 있습니다. 압도적입니다."
        - 선생님: "완전히 정상입니다. 함께 분해해 봅시다."
        - 학생: "좋아요. 저는 정말로 동사 시제를 더 잘 이해해야 해요."
        - 선생님: "좋아요! 우리는 현재를 단순하고 연속적으로 제시하는 것으로 시작할 수 있습니다."
        """        
        prompt = PromptTemplate.from_template(template)
        return prompt
    
class SummaryChain(BaseConversationChain):
    def create_prompt(self):
        template = """
        당신은 요약을 잘하는 요약 AI 입니다. 주어진 내용을 요약해 주세요.
        요약은 bullet point로 작성해 주세요.
        문장의 시작은 적절한 emoji로 시작해 주세요.
        #Context:
        {question}
        """        
        prompt = PromptTemplate.from_template(template)
        return prompt
    
class BlogChain(BaseConversationChain):
    def create_prompt(self):
        template = """
        당신은 블로그 글을 작성하는 AI 입니다.
        주어진 글은 뉴스 기사입니다. 뉴스 기사의 내용을 블로그 글로 작성해 주세요.
        블로그 글의 끝에는 hashtag를 추가해 주세요.
        블로그는 3-5 문단으로 작성해 주세요.
        
        #Context:
        {question}
        """        
        prompt = PromptTemplate.from_template(template)
        return prompt
    