from fastapi import FastAPI, Form
from openai import OpenAI
from repository import download_video,split_text_into_chunks
import whisper
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
model = whisper.load_model("base")
client = OpenAI()

@app.post("/transcribe-file")
async def transcribe_audio(url: str = Form(...)):
    mp3_path = download_video(url)
    result = model.transcribe(mp3_path)
    text = result["text"]
    chunks = split_text_into_chunks(text)
    all_questions = []

    for chunk in chunks:
        response = client.responses.create(
            model = "gpt-4.1-mini",
            input=f"Please create 100 quiz questions based on the following text:{chunk}"
        )
        all_questions.append({"questions": response.output_text})
        return all_questions




