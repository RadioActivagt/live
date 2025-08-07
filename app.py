
from flask import Flask, Response, stream_with_context
import requests

app = Flask(__name__)

# URL del stream original (HTTP)
STREAM_URL = "http://uk15freenew.listen2myradio.com:30682/"

@app.route("/stream")
def stream_proxy():
    def generate():
        with requests.get(STREAM_URL, stream=True) as r:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
    return Response(stream_with_context(generate()), content_type="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
