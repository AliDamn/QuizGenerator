
FastAPI Quiz Generator from YouTube Videos

This project is a FastAPI application that takes a YouTube video URL, extracts the audio, transcribes it using **Whisper**, and generates quiz questions using OpenAI GPT.

---

Features

- Download audio from YouTube videos.
- Transcribe audio to text with OpenAI Whisper.
- Split large text into manageable chunks.
- Generate quiz questions automatically using GPT-4.1-mini.

---

Tech Stack

- **FastAPI** – API framework
- **Whisper** – Audio transcription
- **OpenAI API** – Question generation
- **yt-dlp** – YouTube video downloader
- **Python-dotenv** – Environment variable management

---

Installation

1. Clone the repository:

```bash
git clone git@github.com:AliDamn/QuizGenerator.git
cd AiAgent
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

Usage

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Endpoint

POST `/transcribe-file`

Form Parameters:

* `url` – URL of the YouTube video to process

Example with `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/transcribe-file" -F "url=https://www.youtube.com/watch?v=example"
```

Response:

```json
[
  {
    "questions": "Generated quiz questions for the first chunk of text..."
  },
  {
    "questions": "Generated quiz questions for the second chunk of text..."
  }
]
```

---

Project Structure

```
.
├── main.py                  # FastAPI application
├── repository.py            # Functions: download_video, split_text_into_chunks
├── .env                     # Environment variables
└── README.md                # Project documentation
```

---

## Notes

* The audio is downloaded in MP3 format using `yt-dlp`.
* Text is split into chunks of ~1500 characters for easier processing.
* Each chunk is sent separately to OpenAI for question generation.


