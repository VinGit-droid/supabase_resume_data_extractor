from fastapi import APIRouter, Request
import requests
from app.mongo_client import get_candidate_by_id
from app.config import HUGGINGFACE_API_KEY

router = APIRouter()

@router.post("/ask/{candidate_id}")
async def ask_question(candidate_id: str, request: Request):
    question = (await request.json())["question"]
    candidate = get_candidate_by_id(candidate_id)
    context = str(candidate)

    url = "https://api-inference.huggingface.co/models/your-qa-model"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": {"question": question, "context": context}}

    response = requests.post(url, headers=headers, json=payload)
    return response.json()
