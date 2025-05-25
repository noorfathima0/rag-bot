def build_prompt(user_question: str, articles: list) -> str:
    context = "\n\n".join([
        f"Title: {a['title']}\nContent: {a['content']}" for a in articles
    ])
    return f"""Use the articles below to answer the question.

{context}

Question: {user_question}
Answer:"""
