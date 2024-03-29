


from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(openai_api_key="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")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are my English teacher, You answer question and ask a follow up question. Please keep both the answers and questions short and concise."),
    ("user", "{input}")])
chain = prompt | llm
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

def englishteacher(text):
   response = chain.invoke({"input": text})
   print('AI Teacher: ', response)
   return  response