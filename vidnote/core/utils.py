from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from django.conf import settings
from openai import OpenAI



def extract_video_id(url):
    parsed_url = urlparse(url)
    
    if "youtube.com" in parsed_url.hostname:
        query = parse_qs(parsed_url.query)
        return query.get("v", [None])[0]
    
    if "youtu.be" in parsed_url.hostname:
        return parsed_url.path[1:]
    
    return None

def fetch_transcript(video_id):

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])

        text = " ".join(item["text"] for item in transcript)
        return text
    
    except Exception as e:
        return None
    
def generate_notes(transcript_text):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Beginner friendly
                messages=[
                    {"role": "system", "content": "Create simple study notes from this transcript."},
                    {"role": "user", "content": f"Make notes from: {transcript_text}"}
                ]
            )
    
    return response.choices[0].message.content.strip()