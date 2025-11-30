from flask import Flask, request, jsonify
from flask_cors import CORS
from model_utils import predict, download_model
import sys

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['POST'])
def classify_text():
    data = request.get_json()
    text = data.get('text', '')
    result = predict(text)
    return jsonify({'isSpam': result})


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "--download-model":
        download_model()
    else:
        app.run(host='0.0.0.0', port=8080)
