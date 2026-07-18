from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

history = []

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    history.append(HumanMessage(content=question))

    response = model.invoke(history)

    print("AI:", response.content)

    history.append(AIMessage(content=response.content))
print(history)