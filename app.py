import os
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

app = Flask(__name__)

@app.route('/')
def get_url():
    playlist_id = request.args.get("playlist_id")
    request_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist_id}&key={os.getenv("YOUTUBE_API_KEY")}"
    if "page_token" in request.args:
        request_url += f"&pageToken={request.args.get("page_token")}"
    return request.post(request_url).text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')