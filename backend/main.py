
from fastapi import FastAPI
from openai import OpenAI



app = FastAPI()

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

@app.get("/api")
async def root():
    
    return completion.choices[0].message.content
