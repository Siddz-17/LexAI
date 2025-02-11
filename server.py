from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from youtube import get_video_info, get_video_transcript
from summarizer import summarize_transcript, answer_question
from pydantic import BaseModel

class VideoUrl(BaseModel):
    url: str

class QuestionData(BaseModel):
    summary: str
    question: str

app = FastAPI()

origins = [
    "http://localhost:5173",  # Or wherever your frontend is running
    "http://localhost:4173",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:4173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/video-info")
async def video_info(video_url: VideoUrl):
    try:
        video_info = await get_video_info(video_url.url)
        return video_info
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/summarize")
async def summarize(video_url: VideoUrl):
    try:
        transcript = await get_video_transcript(video_url.url)
        summary = summarize_transcript(transcript)
        return {"summary": summary}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/answer")
async def answer(question_data: QuestionData):
    answer = answer_question(question_data.summary, question_data.question)
    return {"answer": answer}
