import os
import json
from flask import Flask, request, jsonify, render_template
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# ---- Configure Gemini ----
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("WARNING: GEMINI_API_KEY not set. Set it in your .env file.")

client = genai.Client(api_key=API_KEY) if API_KEY else None

MODEL_NAME = "gemini-2.5-flash"  # current free-tier friendly model


def build_prompt(notes_text):
    return f"""You are a helpful study assistant. A student has given you their notes below.

Do the following and return ONLY valid JSON (no markdown, no backticks, no extra text) with this exact structure:
{{
  "summary": "a concise 3-5 sentence summary of the notes",
  "key_points": ["point 1", "point 2", "point 3", "..."],
  "flashcards": [
    {{"question": "a question testing understanding", "answer": "the answer"}},
    {{"question": "...", "answer": "..."}}
  ]
}}

Generate 5-8 key points and 5-8 flashcards based on the notes.

NOTES:
\"\"\"
{notes_text}
\"\"\"
"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/summarize", methods=["POST"])
def summarize():
    data = request.get_json(silent=True) or {}
    notes_text = data.get("notes", "").strip()

    if not notes_text:
        return jsonify({"error": "Please paste some notes first."}), 400

    if not API_KEY:
        return jsonify({"error": "Server is missing GEMINI_API_KEY. Check your .env file."}), 500

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=build_prompt(notes_text)
        )

        raw_text = response.text.strip()

        # Clean up in case the model wraps the JSON in markdown fences
        if raw_text.startswith("```"):
            raw_text = raw_text.strip("`")
            if raw_text.lower().startswith("json"):
                raw_text = raw_text[4:].strip()

        parsed = json.loads(raw_text)

        return jsonify({
            "summary": parsed.get("summary", ""),
            "key_points": parsed.get("key_points", []),
            "flashcards": parsed.get("flashcards", [])
        })

    except json.JSONDecodeError:
        return jsonify({"error": "AI response could not be parsed. Please try again."}), 500
    except Exception as e:
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)