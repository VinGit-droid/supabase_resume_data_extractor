from fastapi import FastAPI
from app.routes import upload, candidates, ask

app = FastAPI()
app.include_router(upload.router)
app.include_router(candidates.router)
app.include_router(ask.router)
