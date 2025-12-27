# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Hello Gemini")
# print(response.text)

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Hello Gemini"
)

print(response.text)