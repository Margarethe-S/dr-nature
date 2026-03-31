from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from test_interface.test_lm_connection import get_lm_response

app = Flask(__name__)
CORS(app)


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROMPT_DIR = os.path.join(BASE_DIR, "system_prompt")
ENV_PATH = os.path.join(BASE_DIR, ".env")


# Online-Showcase-Memory bei Server-Neustart automatisch zurückgesetzt

conversation_history = []

MAX_MESSAGES = 10

def trim_history():
    global conversation_history
    if len(conversation_history) > MAX_MESSAGES:
        conversation_history = conversation_history[-MAX_MESSAGES:]


@app.route("/")
def home():
    return "✅ Dr. Nature Backend läuft!"


@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    data = request.get_json()
    user_input = data.get("message", "")
    user_msg = data.get("message", "")
    mode = data.get("mode", "core_mode")
    prompt_path = os.path.join(PROMPT_DIR, f"{mode}.txt")


    if not os.path.exists(prompt_path):
        prompt_path = os.path.join(PROMPT_DIR, "core_mode.txt")

    conversation_history.append({
        "role": "user", 
        "content": user_msg
        })
    trim_history()

    try:
        reply_text = get_lm_response(user_msg, prompt_path, conversation_history)

        conversation_history.append({
            "role": "assistant", 
            "content": reply_text
            })
        trim_history()

    except Exception as e:
        reply_text = f"⚠️ Fehler bei der KI-Anfrage: {e}"

    return jsonify({"reply": reply_text})


# ✅ HIER wird der Server wirklich gestartet:
if __name__ == "__main__":
    app.run(debug=True)
