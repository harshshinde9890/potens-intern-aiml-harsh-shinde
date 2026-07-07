import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

for model in genai.list_models():
    print(model.name)
    print(model.supported_generation_methods)
    print("-" * 60)