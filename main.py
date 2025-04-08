# main.py
from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Optional home route (for checking if the server is live)
@app.route('/')
def home():
    return "✅ Proxy is live and working!"

# Main proxy route
@app.route('/proxy')
def proxy():
    image_url = request.args.get('url')
    if not image_url:
        return "❌ Error: No URL provided", 400

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        return Response(response.content, content_type=response.headers.get('Content-Type'))
    except requests.exceptions.RequestException as e:
        return f"❌ Error fetching image: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
