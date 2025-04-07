from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    image_url = request.args.get('url')
    if not image_url:
        return '🖼️ Instagram Image Proxy is running! Add ?url= to fetch an image.'

    try:
        # Fetch the image from Instagram
        resp = requests.get(image_url, stream=True)

        # Forward the response headers and content
        return Response(resp.content, content_type=resp.headers['Content-Type'])
    except Exception as e:
        return f"⚠️ Error fetching image: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
