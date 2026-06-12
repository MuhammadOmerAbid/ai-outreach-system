import anthropic
from shared.config import ANTHROPIC_API_KEY, CLAUDE_MODEL

_client = None


def _get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    return _client


def ask(system: str, user: str, max_tokens: int = 1024) -> str:
    client = _get_client()
    msg = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return msg.content[0].text.strip()
