
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Ollama configuration
OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
).rstrip("/")

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5:1.5b"
)

# Tavily configuration
TAVILY_API_KEY = os.getenv(
    "TAVILY_API_KEY",
    ""
)

# Gmail configuration
GMAIL_CLIENT_FILE = os.getenv(
    "GMAIL_CLIENT_FILE",
    "credentials.json"
)

GMAIL_TOKEN_FILE = os.getenv(
    "GMAIL_TOKEN_FILE",
    "token.json"
)

# Gmail read limit: maximum 5 emails
try:
    GMAIL_MAX_READ = int(
        os.getenv("GMAIL_MAX_READ", "5")
    )
except ValueError:
    GMAIL_MAX_READ = 5

GMAIL_MAX_READ = max(1, min(5, GMAIL_MAX_READ))

# Gmail read-only permission
GMAIL_SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

# Application configuration
APP_NAME = "HULK AI"
APP_VERSION = "1.0.0"
