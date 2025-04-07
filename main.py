from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "🖼️ Instagram Image Proxy is running!"

@app.route("/proxy")
def proxy():
    image_url = request.args.get('url')
    if not image_url:
        return {"error": "Missing URL"}, 400

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.instagram.com/"
        }

        r = requests.get(image_url, headers=headers)
        if r.status_code == 200:
            return Response(r.content, content_type=r.headers['Content-Type'])
        else:
            return {"error": f"Image fetch failed with status {r.status_code}"}, r.status_code
    except Exception as e:
        return {"error": str(e)}, 500

# This line is needed to run the Flask app on Replit
app.run(host='0.0.0.0', port=3000)
