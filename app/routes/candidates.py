from fastapi import APIRouter
from app.mongo_client import get_all_candidates, get_candidate_by_id

router = APIRouter()

@router.get("/candidates")
def list_candidates():
    return get_all_candidates()

@router.get("/candidate/{candidate_id}")
def get_candidate(candidate_id: str):
    return get_candidate_by_id(candidate_id)
