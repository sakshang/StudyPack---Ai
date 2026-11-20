
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Send a simple test prompt
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Explain machine learning in exactly 3 simple sentences."
)

print("\n--- GEMINI RESPONSE ---\n")
print(response.text)
