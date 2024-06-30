from flask import Flask, render_template, request, jsonify
import requests
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

# Hugging Face API endpoint
api_url = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

# Hugging Face API token
api_token = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.form['text_prompt']
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    payload = {
        "inputs": prompt
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            image_data = response.content
            return jsonify({"image": image_data.decode('utf-8')})
        else:
            return jsonify({"error": "Failed to generate image"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
