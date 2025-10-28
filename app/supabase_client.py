from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_KEY
from datetime import datetime

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_to_supabase(file, filename):
    print('supabase------')
    response = supabase.storage.from_("resumes").upload(filename, file)
    print(response)
    metadata = {
        "filename": filename,
        "upload_time": datetime.now().isoformat(),
    }
    print('metadata---')
    print(metadata)
    meta = supabase.table("resume_metadata").insert(metadata).execute()
    print('meta------', meta)
    return meta.data[0]["id"]
