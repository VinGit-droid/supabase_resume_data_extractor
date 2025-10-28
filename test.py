import requests
from app.config import HUGGINGFACE_API_KEY
#from app.config import HF_API_KEY


API_TOKEN = HUGGINGFACE_API_KEY

#headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer API_TOKEN"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.text)
    return response.json()
data = query({"inputs": "How can AI assist in everyday tasks?"})

print(data)