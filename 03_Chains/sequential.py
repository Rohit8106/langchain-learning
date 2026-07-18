from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on {TOPIC}",
    input_variables=["TOPIC"]
)

prompt2 = PromptTemplate(
    template="Generate a five-point summary from the following text:\n\n{TEXT}",
    input_variables=["TEXT"]
)

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({
    "TOPIC": "Unemployment in India"
})

print(result) 

chain.get_graph().print_ascii()