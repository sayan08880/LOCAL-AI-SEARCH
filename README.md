
# HULK AI

A local AI assistant built with Python, Ollama, Gmail API, and Tavily Web Search.

## Features

- Local AI responses using Ollama.
- Gmail email analysis and summarization.
- Read up to 5 recent Gmail emails.
- Generate email drafts using AI.
- Web search using Tavily API.
- Terminal-based interactive menu.
- Gmail emails are never sent automatically.

## Project Structure

```text
HULK-AI/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── hulk/
    ├── __init__.py
    ├── config.py
    ├── cli.py
    ├── ollama_client.py
    ├── gmail_service.py
    ├── gmail_ai.py
    └── web_search.py
```

## Requirements

- Python 3
- Ollama
- Qwen 2.5 1.5B model
- Tavily API key
- Google Gmail API credentials

## Installation on Fedora

### 1. Clone or create the project folder

```bash
mkdir -p ~/HULK-AI/hulk
cd ~/HULK-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
nano .env
```

Add your Tavily API key to the `.env` file.

### 5. Install the Ollama model

```bash
ollama pull qwen2.5:1.5b
```

Start Ollama:

```bash
ollama serve
```

### 6. Configure Gmail API

1. Open Google Cloud Console.
2. Create a Google Cloud project.
3. Enable Gmail API.
4. Configure the OAuth consent screen.
5. Create an OAuth Client ID.
6. Select Desktop application.
7. Download the JSON credentials.
8. Save the downloaded file as `credentials.json` inside the HULK-AI folder.

If your OAuth app is in Testing mode, add your Gmail account as a test user.

### 7. Run HULK AI

```bash
python main.py
```

## Main Menu

1. Gmail Automation
2. Web Searcher
3. Refresh All Status
4. Exit

## Gmail Features

- Check Gmail connection.
- Analyse the latest 5 emails.
- Summarize email content.
- Generate an email subject and body.
- Drafts are displayed for manual copying.

**Note:** The Gmail integration uses read-only access. It does not send emails or save drafts to Gmail.

## Security

Never share these files publicly:

- `.env`
- `credentials.json`
- `token.json`

Do not upload them to GitHub.

## Technologies

- Python
- Ollama
- Qwen 2.5 1.5B
- Gmail API
- Tavily Search API
# LOCAL-AI-SEARCH
