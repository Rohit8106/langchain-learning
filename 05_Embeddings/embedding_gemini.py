from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

vector = embeddings.embed_query("What is the capital of India?")

print("Vector dimension:", len(vector))
print(vector[:10])