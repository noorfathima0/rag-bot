import httpx

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3"

def ask_ollama(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = httpx.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("message", {}).get("content", "No response from model.")
    except Exception as e:
        return f"Ollama error: {str(e)}"
