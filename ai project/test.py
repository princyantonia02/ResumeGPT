import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def query_hf(prompt):
    payload = {
        "model": "deepseek-ai/DeepSeek-R1",   # ✅ exact working model
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(URL, headers=HEADERS, json=payload, timeout=120)
    if response.status_code != 200:
        print(f"HTTP Error: {response.status_code}\n{response.text}")
        return ""
    data = response.json()
    return data["choices"][0]["message"]["content"]

# --- test ---
output = query_hf("Hello! Say something friendly.")
print("AI Response:")
print(output)
