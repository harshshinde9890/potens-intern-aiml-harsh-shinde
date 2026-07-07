from src.llm.gemini import GeminiLLM

llm = GeminiLLM().get_llm()

response = llm.invoke("What is Artificial Intelligence?")

print(response.content)