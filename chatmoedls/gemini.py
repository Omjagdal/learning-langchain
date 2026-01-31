from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyBDhkGEdF5mixkK_Xhc2wHVk7IQMPNpP0s"

model = ChatGoogleGenerativeAI(
    model="gemini-pro",   # ✅ ONLY MODEL SUPPORTED IN v1beta
    temperature=0.2,
)

response = model.invoke("What is the capital of India?")
print(response.content)
