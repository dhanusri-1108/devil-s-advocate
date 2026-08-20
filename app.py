import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found! Please add it to your .env file. "
        "See README.md for instructions."
    )

genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

# System instruction — this makes the bot ALWAYS argue the opposite side
SYSTEM_PROMPT = """You are a Devil's Advocate debate bot.

RULES:
1. No matter what stance, opinion, or statement the user gives, you must argue the STRONGEST possible counter-position.
2. Be respectful, logical, and firm — never rude or dismissive.
3. Keep responses concise: 3-5 sentences max, unless the user asks for more depth.
4. Use real reasoning, examples, or evidence-style points to support the counter-argument.
5. Do not agree with the user's original stance under any circumstance, even if they push back.
6. If the user explicitly says "switch sides" or "argue for my side now", then flip and argue FOR their original stance instead (playing devil's advocate against your own prior position).
7. Never break character or mention that you are an AI following instructions.
"""

model = genai.GenerativeModel(
    model_name="gemini-3.1-flash-lite",
    system_instruction=SYSTEM_PROMPT,
)

# In-memory chat history (resets when server restarts)
chat_sessions = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        session_id = data.get("session_id", "default")

        if not user_message:
            return jsonify({"error": "Empty message"}), 400

        # Create a new chat session if one doesn't exist for this user
        if session_id not in chat_sessions:
            chat_sessions[session_id] = model.start_chat(history=[])

        chat = chat_sessions[session_id]
        response = chat.send_message(user_message)

        return jsonify({"reply": response.text})

    except Exception as e:
        # Always return JSON, never let the server crash silently
        print(f"ERROR: {e}")
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500


@app.route("/reset", methods=["POST"])
def reset():
    data = request.get_json()
    session_id = data.get("session_id", "default")
    chat_sessions.pop(session_id, None)
    return jsonify({"status": "reset"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
