from retrieval.query_handler import query_news_index
from retrieval.prompt_template import build_prompt
from llm.ollama_client import ask_ollama

def answer_question(user_query: str, domain: str = "general", top_k: int = 3) -> str:
    articles = query_news_index(user_query, domain=domain, k=top_k)
    if not articles:
        return "No relevant articles found."

    prompt = build_prompt(user_query, articles)
    return ask_ollama(prompt)
