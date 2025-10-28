from fastapi import APIRouter, UploadFile
import shutil
from app.supabase_client import upload_to_supabase
from app.mongo_client import save_candidate
from app.resume_processor import extract_text, extract_fields

router = APIRouter()

import os
os.makedirs("temp", exist_ok=True)

@router.post("/upload")
async def upload_resume(file: UploadFile):
    path = f"temp/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print('passed------')
    metadata_id = upload_to_supabase(path, file.filename)
    text = extract_text(path)
    fields = extract_fields(text)
    print('passed supa------')

    candidate_data = {"candidateid": metadata_id, **fields}
    save_candidate(candidate_data)
    return {"status": "success", "candidateid": metadata_id}
