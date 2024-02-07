from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key="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")

llm.invoke("how can langsmith help with testing?")

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")])
