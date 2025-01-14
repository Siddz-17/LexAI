from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key='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')

def summarize_transcript(text: str) -> str:
    """Summarize video transcript."""
    messages = [{
        "role": "user",
        # Customize this prompt to change the summary style
        "content": f"Create a concise summary of this YouTube video transcript. Focus on the main points and key takeaways:\n{text}"
    }]
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-70b-8192"  # You can change the model here
    )
    
    return chat_completion.choices[0].message.content.strip()

def answer_question(summary: str, question: str) -> str:
    """Answer question about the summary."""
    messages = [{
        "role": "user",
        # Customize this prompt for Q&A style
        "content": f"Given this video summary:\n{summary}\n\nPlease answer this question: {question}\n\nProvide a clear and specific answer based on the summary content."
    }]
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192"  # You can change the model here
    )
    
    return chat_completion.choices[0].message.content.strip()
