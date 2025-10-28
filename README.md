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

EndPoints

<img width="970" height="584" alt="endpoints" src="https://github.com/user-attachments/assets/e0495bb7-a343-4110-b0b6-15776f8573a0" />


Uploading a resume

<img width="1270" height="380" alt="image-1" src="https://github.com/user-attachments/assets/cfd14c01-1e73-4f2c-802b-f6a8d28861f0" />


<img width="962" height="675" alt="image-2" src="https://github.com/user-attachments/assets/2210ba83-06fb-4061-a3c5-9b3e863d0b0f" />



Supabase Data Capture


<img width="1218" height="697" alt="resume_metadata_supabase" src="https://github.com/user-attachments/assets/f7ec9d3b-68fa-444a-92ca-11dabea3c504" />



<img width="1216" height="445" alt="supabase_resumes_storage" src="https://github.com/user-attachments/assets/67de337d-77a1-4129-b751-b776c9b2b95e" />



Code Breaks Here!!!


<img width="782" height="619" alt="code_breaks_here" src="https://github.com/user-attachments/assets/7af2bf33-80cc-485d-8c04-77a47f54464f" />


<img width="730" height="653" alt="error_i_got" src="https://github.com/user-attachments/assets/ac4d3d72-90b6-445d-bf99-b4e644590516" />



