from langchain_google_genai import GoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyAldnsS1yp3H_Y7S7MffOnshA4CPw6VWlY"

model = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append( user_input)
    if user_input.lower() in ["exit", "quit"]:
        break

    response = model.invoke(user_input)
    chat_history.append(response)
    print("Bot:", response)
print(chat_history)