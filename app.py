from flask import Flask, render_template, request, jsonify, views
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])  # Pastikan metode POST disertakan di sini
def generate_image():
    api_token = os.getenv('HUGGING_FACE_API_TOKEN')  # Gunakan environment variable untuk token
    prompt = request.json['prompt']

    headers = {
        'Authorization': f'Bearer {api_token}'
    }
    payload = {
        'inputs': prompt
    }
    api_url = 'https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4'

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.content, 200, {'Content-Type': 'image/png'}
    else:
        return jsonify({'error': f'Request failed with status code {response.status_code}'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
