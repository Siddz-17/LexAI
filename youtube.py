from youtube_transcript_api import YouTubeTranscriptApi
import re
import json
import aiohttp

async def get_video_id(url: str) -> str:
    """Extract video ID from YouTube URL."""
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)

async def get_video_info(url: str) -> dict:
    """Get video information using YouTube oEmbed."""
    video_id = await get_video_id(url)
    oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(oembed_url) as response:
            if response.status == 200:
                data = await response.json()
                return {
                    "id": video_id,
                    "title": data["title"],
                    "thumbnail": f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
                }
            else:
                raise ValueError("Could not fetch video information")

async def get_video_transcript(url: str) -> str:
    """Get video transcript."""
    video_id = await get_video_id(url)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])
    except Exception as e:
        raise ValueError(f"Could not fetch transcript: {str(e)}")
