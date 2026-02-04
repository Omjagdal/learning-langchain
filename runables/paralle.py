from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()


# Define simple functions
uppercase = RunnableLambda(lambda x: x.upper())
word_count = RunnableLambda(lambda x: len(x.split()))
reverse_text = RunnableLambda(lambda x: x[::-1])

# Run them in parallel
parallel_chain = RunnableParallel(
    upper=uppercase,
    count=word_count,
    reverse=reverse_text
)

# Invoke
result = parallel_chain.invoke("hello langchain")

print(result)
