from fastapi import APIRouter, Query
from typing import List
from youtube_transcript_api import YouTubeTranscriptApi
from app.utils.helpers import extract_video_id

router = APIRouter()

@router.get("/search")
def search_terms(youtube_url: str, terms: List[str] = Query(...)):
    video_id = extract_video_id(youtube_url)
    if not video_id:
        return {"error": "Invalid YouTube URL"}

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        return {"error": str(e)}

    matches = []
    for entry in transcript:
        text = entry["text"].lower()
        for term in terms:
            if term.lower() in text:
                timestamp = int(entry["start"])
                matches.append({
                    "term": term,
                    "timestamp": timestamp,
                    "text": entry["text"],
                    "link": f"https://www.youtube.com/watch?v={video_id}&t={timestamp}s"
                })

    return {"matches": matches}
