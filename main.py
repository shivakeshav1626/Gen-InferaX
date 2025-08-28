import requests

GEMINI_API_KEY = "AIzaSyAys17efuQBG7x_wtMzUIKqx51oLf2he6k"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def zero_shot_prompt(question):
    prompt = f"Answer the following research question in a clear, structured way:\n{question}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(
        f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        headers=headers,
        json=data
    )
    result = response.json()
    return result['candidates'][0]['content']['parts'][0]['text']

# Example usage
question = "What are the key differences between FAISS and Pinecone vector databases?"
answer = zero_shot_prompt(question)
print("Gemini LLM Answer:", answer)