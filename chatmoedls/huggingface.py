from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id =" TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task ="text-generation",
    
)
model = ChatHuggingFace (llm=llm)
response = model.invoke("What is LangChain?")
print("Response:", response)