from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt=PromptTemplate(
    template='write the summary of the following poem  {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()
loader=TextLoader('cricket.txt',encoding='utf-8')

docs=loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain=prompt|model|parser
result=chain.invoke({'poem':docs[0].page_content})
print(result)