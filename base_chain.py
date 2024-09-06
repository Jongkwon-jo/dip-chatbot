from abc import ABC, abstractmethod
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser



class BaseConversationChain(ABC):
    @abstractmethod
    def create_prompt(self):
        pass

    def create_model(self):
        return ChatOpenAI(model_name='gpt-4o-mini')

    def create_outputparser(self):
        return StrOutputParser()

    def create_chain(self):
        prompt = self.create_prompt()
        model = self.create_model()
        output_parser = self.create_outputparser()
        chain = prompt | model | output_parser
        return chain