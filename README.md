# AI Notes Summarizer


Students spend excessive time reviewing lengthy study materials. This tool lets you paste your notes and instantly get:
- A concise summary
- Extracted key points
- Auto-generated flashcards
- A downloadable text file of everything

## Tech Stack
- Python + Flask (backend)
- HTML/CSS/JavaScript (frontend)
- Google Gemini API (AI summarization)

## Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-notes-summarizer.git
   cd ai-notes-summarizer
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and paste your free Gemini API key:
   ```bash
   cp .env.example .env
   ```
   Get a free key at https://aistudio.google.com → "Get API Key".

4. Run the app:
   ```bash
   python app.py
   ```

5. Open your browser to `http://localhost:5000`

## Usage
> Note: PDF upload support is planned as a future enhancement (see Issue #3).
> Note: Large notes may take longer to process; a file-size limit and clearer error messages are planned (see Issue #4).
1. Paste your notes in the text box
2. Click **Summarize**
3. View the summary, key points, and flashcards
4. Click **Download Summary** to save as a text file

## Screenshots
_(Add screenshots here, e.g. `![Upload screen](screenshots/upload.png)`)_

## Contributors
See [CONTRIBUTORS.md](CONTRIBUTORS.md)
