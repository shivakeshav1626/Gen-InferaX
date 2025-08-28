import requests

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def dynamic_prompt(question, expertise="beginner", answer_type="summary"):
    prompt = (
        f"User expertise: {expertise}\n"
        f"Preferred answer type: {answer_type}\n"
        f"Please answer the following research question accordingly. Respond in JSON format with keys 'answer', 'sources', and 'confidence':\n{question}"
    )
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ],
        "generationConfig": {
            "topP": 0.8,  # Top P sampling for diversity
            "temperature": 0.7,  # Temperature for creativity
            "topK": 40,  # Top K sampling for diversity
            "stopSequences": ["<END>"]  # Stop sequence to end generation
        }
    }
    response = requests.post(
        f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        headers=headers,
        json=data
    )
    result = response.json()
    # Token usage logging
    token_count = None
    # Gemini API returns token usage in 'usageMetadata' if enabled
    if 'usageMetadata' in result:
        token_count = result['usageMetadata'].get('totalTokens')
    elif 'candidates' in result and 'usageMetadata' in result['candidates'][0]:
        token_count = result['candidates'][0]['usageMetadata'].get('totalTokens')
    # Print token usage
    if token_count is not None:
        print(f"Tokens used in this AI call: {token_count}")
    else:
        print("Token usage information not available from Gemini API response.")
    # Try to parse structured output
    response_text = result['candidates'][0]['content']['parts'][0]['text']
    import json
    try:
        structured = json.loads(response_text)
        print("Structured Output:", structured)
        return structured
    except Exception:
        print("Raw Output (not valid JSON):", response_text)
        return response_text

# Example usage
question = "What are the key differences between FAISS and Pinecone vector databases?"
answer = dynamic_prompt(question, expertise="expert", answer_type="detailed")
print("Gemini LLM Answer:", answer)