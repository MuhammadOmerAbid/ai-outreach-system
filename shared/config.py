import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY", "")
INSTANTLY_API_KEY = os.getenv("INSTANTLY_API_KEY", "")
SMARTLEAD_API_KEY = os.getenv("SMARTLEAD_API_KEY", "")
SENDING_DOMAIN = os.getenv("SENDING_DOMAIN", "")
DAILY_SEND_CAP = int(os.getenv("DAILY_SEND_CAP", "30"))
TAPLIO_API_KEY = os.getenv("TAPLIO_API_KEY", "")

CLAUDE_MODEL = "claude-sonnet-4-6"
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)
