from sentence_transformers import SentenceTransformer
import numpy as np
from pathway_pipeline.etl import run_pathway_pipeline

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_query(text: str) -> np.ndarray:
    return embedding_model.encode(text)

def query_news_index(user_query: str, domain: str = "general", k: int = 3):
    vector_index = run_pathway_pipeline(domain=domain)
    query_vector = embed_query(user_query)
    matches = vector_index.search(query_vector, k=k)
    return [
        {
            "title": m.title,
            "content": m.content,
            "url": m.url,
            "publishedAt": m.publishedAt
        } for m in matches
    ]
