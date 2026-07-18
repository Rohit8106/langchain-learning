from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

prompt2=PromptTemplate(
    template='summarize the joke - {topic}',
    input_variables=['topic']
)

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "AI"})

print(result)