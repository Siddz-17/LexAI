import streamlit as st
import requests
import os
import asyncio
import re
import json
import aiohttp
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi
from groq import Groq
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn
from threading import Thread

# Load environment variables
load_dotenv()

# Set API URL (for local testing or deployment)
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Initialize FastAPI
app = FastAPI()

# Enable CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class VideoUrl(BaseModel):
    url: str

class QuestionData(BaseModel):
    summary: str
    question: str

# Groq API Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Helper Functions
async def get_video_id(url: str) -> str:
    """Extract video ID from YouTube URL."""
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)

async def get_video_info(url: str) -> dict:
    """Fetch video information using YouTube oEmbed."""
    video_id = await get_video_id(url)
    oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(oembed_url) as response:
            if response.status == 200:
                data = await response.json()
                return {"id": video_id, "title": data["title"], "thumbnail": f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"}
            else:
                raise ValueError("Could not fetch video information")

async def get_video_transcript(url: str) -> str:
    """Retrieve transcript from YouTube video."""
    video_id = await get_video_id(url)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])
    except Exception as e:
        raise ValueError(f"Could not fetch transcript: {str(e)}")

def summarize_transcript(text: str) -> str:
    """Generate a summary from the transcript using Groq API."""
    messages = [{"role": "user", "content": f"Summarize this video transcript:\n{text}"}]
    chat_completion = client.chat.completions.create(messages=messages, model="llama3-8b-8192")
    return chat_completion.choices[0].message.content.strip()

def answer_question(summary: str, question: str) -> str:
    """Answer a user question based on the video summary."""
    messages = [{"role": "user", "content": f"Summary:\n{summary}\n\nQuestion: {question}"}]
    chat_completion = client.chat.completions.create(messages=messages, model="llama3-8b-8192")
    return chat_completion.choices[0].message.content.strip()

# API Endpoints
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

# Run FastAPI in a separate thread
def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

Thread(target=run_fastapi, daemon=True).start()

# Streamlit Frontend
st.set_page_config(page_title="YouTube Summarizer", page_icon="🎬", layout="wide")

st.title("🎬 LexAI - YouTube Summarizer")
st.subheader("Transform lengthy YouTube videos into concise, insightful summaries.")

video_url = st.text_input("Enter YouTube Video URL:", placeholder="Paste the YouTube link here")

if video_url:
    if "video_info" not in st.session_state or st.session_state.get("video_url") != video_url:
        st.session_state.pop("summary", None)
        try:
            response = requests.post(f"{API_URL}/api/video-info", json={"url": video_url})
            response.raise_for_status()
            video_info = response.json()
            st.session_state["video_info"] = video_info
            st.session_state["video_url"] = video_url
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching video info: {e}")

    if "video_info" in st.session_state and st.session_state.get("video_url") == video_url:
        st.image(st.session_state["video_info"]["thumbnail"], width=300)
        st.write(f"**Title:** {st.session_state['video_info']['title']}")

    if st.button("Summarize Video"):
        try:
            response = requests.post(f"{API_URL}/api/summarize", json={"url": video_url})
            response.raise_for_status()
            summary = response.json()["summary"]
            st.session_state["summary"] = summary
        except requests.exceptions.RequestException as e:
            st.error(f"Error summarizing video: {e}")

    if "summary" in st.session_state:
        st.subheader("Video Summary")
        st.markdown(st.session_state["summary"])

        question = st.text_input("Ask a question about the summary:")
        if question:
            try:
                response = requests.post(f"{API_URL}/api/answer", json={"summary": st.session_state["summary"], "question": question})
                response.raise_for_status()
                answer = response.json()["answer"]
                st.write(f"**Answer:** {answer}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error answering question: {e}")

st.markdown("<p style='text-align: center;'>Powered by LLama3. Built with ❤️ using Streamlit.</p>", unsafe_allow_html=True)
