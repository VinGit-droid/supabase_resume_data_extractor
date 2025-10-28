# 🧠 Resume Parser API

This FastAPI app allows resume uploads, extracts candidate data using Hugging Face models, and stores it in Supabase and MongoDB.

## 🚀 Features

- `/upload`: Upload `.pdf` or `.docx` resumes
- Supabase: Stores file and metadata
- MongoDB: Stores structured candidate data
- Hugging Face: Extracts resume fields and answers questions
- `/candidates`: Lists all candidates
- `/candidate/{id}`: Full candidate info
- `/ask/{id}`: Ask natural questions about a candidate

## 🔧 Setup

### Environment Variables

Create a `.env` file:

### Keys
SUPABASE_URL=your_supabase_url 
SUPABASE_KEY=your_supabase_key 
MONGO_URI=your_mongodb_uri 
HUGGINGFACE_API_KEY=your_huggingface_key


### Install Dependencies
-bash
pip install -r requirements,txt

### Run Server

uvicorn app.main:app --reload

### 📸 Screenshots

Uploading a resume
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](endpoints.png)
![alt text](upload_browser.png)
![alt text](supabase_resumes_storage.png)
![alt text](resume_metadata_supabase.png)
Q&A response
