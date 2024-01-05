
from fastapi import FastAPI, UploadFile
from openai import OpenAI
from pathlib import Path

UPLOAD_DIR = Path() / 'uploads'

app = FastAPI()
client = OpenAI()


@app.post('/uploadfile/')
async def create_upload_file(file_upload: UploadFile):
    data = await file_upload.read()
    save_to = UPLOAD_DIR / file_upload.filename
    with open(save_to, 'wb') as f:
        f.write(data)
    return {"filename": file_upload.filename}



@app.get("/api")
async def root():
    return ""

