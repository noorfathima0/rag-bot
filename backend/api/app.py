from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(
    title="Real-time RAG API",
    description="Ask questions based on real-time Indian news.",
    version="1.0.0"
)

# Enable CORS if you plan to connect from a frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
