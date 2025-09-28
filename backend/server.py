from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from test_interface.test_lm_connection import get_lm_response



app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "✅ Dr. Nature Backend läuft!"


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    user_msg = data.get("message", "")
    mode = data.get("mode", "core_mode")
    prompt_path = f"system_prompt/{mode}.txt"


    if not os.path.exists(prompt_path):
        prompt_path = "system_prompt/core_mode.txt"


    try:
        reply_text = get_lm_response(user_msg, prompt_path)
    except Exception as e:
        reply_text = f"⚠️ Fehler bei der KI-Anfrage: {e}"


    return jsonify({"reply": reply_text})


# ✅ HIER wird der Server wirklich gestartet:
if __name__ == "__main__":
    app.run(debug=True)

