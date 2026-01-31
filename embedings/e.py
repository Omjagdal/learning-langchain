from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv  
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
texts = [
    "LangChain is a framework for building applications with LLMs.",
    "OpenAI provides powerful language models for various tasks.",
    "Embeddings are numerical representations of text data."
]
embedding_vectors = embeddings.embed_documents(texts)
query = "What is LangChain?"
query_vector = embeddings.embed_query(query)

similarities = cosine_similarity(query_vector, embedding_vectors)
most_similar_index = np.argmax(similarities)
print("Most similar text:", texts[most_similar_index])
print("Similarity score:", similarities[0][most_similar_index]) 