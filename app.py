from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

HF_API_KEY = os.getenv("HF_API_KEY")

def call_huggingface(user_input):
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    data = {
        "inputs": f"[INST] {user_input} [/INST]",
        "parameters": {
            "max_new_tokens": 800,
            "temperature": 0.7,
            "return_full_text": True
        }
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
        headers=headers,
        json=data
    )

    if response.status_code != 200:
        print("HF API error:", response.status_code, response.text)
        return f"Error from Hugging Face: {response.status_code}"

    try:
        result = response.json()
        if isinstance(result, list):
            return result[0]["generated_text"].replace("[/INST]", "").strip()
        else:
            return "Unexpected response format"
    except Exception as e:
        print("JSON decode error:", response.text)
        return f"Error parsing response: {str(e)}"



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    reply = call_huggingface(user_input)
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True)
