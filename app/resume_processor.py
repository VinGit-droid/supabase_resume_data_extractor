import requests
from docx import Document
import pdfplumber


from app.config import HUGGINGFACE_API_KEY

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages)
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)

def extract_fields(text):
    print('text----', text)

    

    url = "https://huggingface.co/yashpwr/resume-ner-bert-v2"
    print('HuggingFace======')
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": text}
    print("xxxxxxxx", headers)
    response = requests.post(url, headers=headers, json=payload)
    print("Status Code:", response.status_code)
    print("Response Text:", response.json)
    print(response)

    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        raise Exception(f"JSON decode error: {str(e)}; Response text: {response.text}")
'''
def test():
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": text}
    response = requests.post(f"https://api-inference.huggingface.co/models/{NER_MODEL}", headers=headers, json=payload)
    entities = response.json()
    
    result = {
        "education": {},
        "experience": {},
        "skills": [],
        "hobbies": [],
        "certifications": [],
        "projects": [],
        "introduction": ""
    }

    for ent in entities:
        label = ent["entity_group"].lower()
        word = ent["word"]
        if label in result:
            if isinstance(result[label], list):
                result[label].append(word)
            elif isinstance(result[label], dict):
                result[label][word] = word
            else:
                result[label] += word + " "
    return result

from transformers import pipeline

# Create NER pipeline
ner_pipeline = pipeline(
    "token-classification",
    model="yashpwr/resume-ner-bert-v2",
    aggregation_strategy="simple"
)

# Extract entities
text = "Sarah Johnson holds a Master's degree in Computer Science from Stanford University. Skills: Python, TensorFlow, SQL."
results = ner_pipeline(text)

for entity in results:
    print(f"{entity['entity_group']}: {entity['word']} (confidence: {entity['score']:.3f})")
    

'''