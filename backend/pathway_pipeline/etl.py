import pathway as pw
from sentence_transformers import SentenceTransformer
import numpy as np
from ingestion.data_stream import stream_articles

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

class ArticleSchema(pw.Schema):
    title: str
    content: str
    url: str
    publishedAt: str

def embed_text(text: str) -> np.ndarray:
    return embedding_model.encode(text)

def run_pathway_pipeline(domain="general"):
    input_stream = pw.io.python.read(lambda: stream_articles(domain=domain), schema=ArticleSchema)

    embedded_table = input_stream.select(
        title=input_stream.title,
        content=input_stream.content,
        url=input_stream.url,
        publishedAt=input_stream.publishedAt,
        embedding=pw.declare_type(np.ndarray).const(
            embed_text(input_stream.title + " " + input_stream.content)
        )
    )

    vector_index = pw.ml.index(embedded_table, column="embedding")
    return vector_index

