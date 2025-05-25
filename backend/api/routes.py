from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from retrieval.rag_orchestrator import answer_question
from config.subscriptions import add_subscription

router = APIRouter()

# Shared input schema
class QuestionRequest(BaseModel):
    question: str
    domain: str = "general"

# ✅ Ask with domain support
@router.post("/ask")
def ask_question(payload: QuestionRequest):
    try:
        answer = answer_question(payload.question, domain=payload.domain)
        return {"question": payload.question, "domain": payload.domain, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Subscribe to topic alerts
@router.post("/subscribe")
def subscribe_user(payload: QuestionRequest):
    add_subscription("default_user", payload.question)
    return {"message": f"Subscribed to topic: '{payload.question.strip()}'"}
