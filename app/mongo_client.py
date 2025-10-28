from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["resume_db"]
collection = db["candidates"]

def save_candidate(candidate_data):
    collection.insert_one(candidate_data)

def get_all_candidates():
    return list(collection.find({}, {"_id": 0}))

def get_candidate_by_id(candidateid):
    return collection.find_one({"candidateid": candidateid}, {"_id": 0})
