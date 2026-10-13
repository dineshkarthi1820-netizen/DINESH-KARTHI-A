# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS learning assistant based on the supplied project specification.

## Features

- Ask educational questions
- Explain difficult topics in simple language
- Generate exactly 3 MCQs with 4 options
- Summarize educational text
- Generate beginner-to-advanced learning paths

The original specification describes FastAPI, Jinja2, HTML/CSS, Gemini, and a lightweight local LaMini-Flan-T5 explanation model. This runnable version uses the current Google GenAI Python SDK for all five features so the project is practical to install and run today. The explanation logic remains isolated in `explanation_module.py`, so a local model can be substituted later.

## Project structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── run_windows.bat
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Windows + VS Code setup

1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. Open Terminal in VS Code.
4. Create a virtual environment:

```powershell
python -m venv .venv
```

5. Activate it:

```powershell
.venv\Scripts\activate
```

6. Install packages:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

7. Copy `.env.example` to `.env`.
8. Put your Gemini API key into `.env`:

```text
GEMINI_API_KEY=your_real_key_here
```

9. Start the application:

```powershell
python -m uvicorn main:app --reload
```

10. Open:

```text
http://127.0.0.1:8000
```

You can also double-click `run_windows.bat` after completing the setup.

## API endpoints

- `POST /qa`
- `POST /explain`
- `POST /quiz`
- `POST /summarize`
- `POST /learn/recommendations`
- `GET /health`

FastAPI's interactive API documentation is also available at:

```text
http://127.0.0.1:8000/docs
```

## Important

Do not put your real API key inside source code or commit `.env` to GitHub.
