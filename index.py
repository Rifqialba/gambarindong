import requests
from dotenv import load_dotenv
import os

load_dotenv() 

# Masukkan token API Hugging Face Anda di sini
api_token = "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"

# Prompt untuk menghasilkan gambar
prompt = "KUCING MAIN SAMA PINGUIN"

# Header untuk otentikasi
headers = {
    "Authorization": f"Bearer {api_token}"
}

# Payload untuk permintaan API
payload = {
    "inputs": prompt
}

# Endpoint untuk model Stable Diffusion
api_url = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

response = requests.post(api_url, headers=headers, json=payload)

# Cek apakah permintaan berhasil
if response.status_code == 200:
    image_data = response.content
    with open("generated_image.png", "wb") as image_file:
        image_file.write(image_data)
    print("Image saved as generated_image.png")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
