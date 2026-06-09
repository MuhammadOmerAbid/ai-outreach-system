# AI Outreach System â€” Monorepo

![CI](https://github.com/MuhammadOmerAbid/ai-outreach-system/actions/workflows/ci.yml/badge.svg) ![License](https://img.shields.io/github/license/MuhammadOmerAbid/ai-outreach-system) ![Python](https://img.shields.io/badge/python-3.11+-blue)


A three-agent system for getting international clients, finding remote jobs, and doing academic outreach â€” all with human approval before any outbound action.

---

## Agents

| Folder | Agent | Purpose |
|--------|-------|---------|
| `agent_content/` | LinkedIn Content Agent | Turns your rough notes into polished LinkedIn posts, sends to Telegram for approval |
| `agent_jobs/` | Remote Job Hunter | Finds remote jobs, scores them against your profile, drafts cover notes |
| `agent_leadgen/` | Lead Gen + Enrichment Engine | Finds prospects, enriches, drafts cold emails, sends via Instantly/Smartlead after approval |

---

## Monorepo Structure

```
ai-outreach-system/
â”œâ”€â”€ README.md
â”œâ”€â”€ .env.example          # every API key needed (copy to .env and fill in)
â”œâ”€â”€ .gitignore
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ shared/               # shared utilities used by all agents
â”‚   â”œâ”€â”€ config.py         # loads .env settings
â”‚   â”œâ”€â”€ llm.py            # Claude API wrapper
â”‚   â”œâ”€â”€ approval.py       # Telegram bot approval flow
â”‚   â””â”€â”€ db.py             # SQLite helpers
â”œâ”€â”€ agent_content/        # Agent 1 â€” LinkedIn Content Agent
â”œâ”€â”€ agent_jobs/           # Agent 3 â€” Remote Job Hunter
â””â”€â”€ agent_leadgen/        # Agent 2 â€” Lead Gen + Enrichment Engine
```

---

## Prerequisites â€” Accounts & API Keys

Before running anything, sign up for these:

| Service | What For | Where to Get Key |
|---------|----------|-----------------|
| Anthropic | Claude AI (all agents) | https://console.anthropic.com |
| Telegram | Approval bot (all agents) | Create bot via @BotFather on Telegram |
| Apollo.io | Lead sourcing (Agent 2) | https://developer.apollo.io |
| Instantly or Smartlead | Cold email sending (Agent 2) | https://app.instantly.ai or https://app.smartlead.ai |
| Taplio *(optional)* | LinkedIn post scheduling (Agent 1) | https://taplio.com |

---

## Setup

```bash
# 1. Clone and enter the repo
cd ai-outreach-system

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
copy .env.example .env
# Open .env and fill in all your API keys

# 5. Run an agent (examples)
python agent_content/main.py
python agent_jobs/main.py
python agent_leadgen/main.py
```

---

## Safety Rules (Non-Negotiable)

1. **No LinkedIn scraping** â€” never use unofficial LinkedIn automation
2. **Human approval required** before any email, post, or connection request is sent
3. **Official APIs only** â€” Apollo, RemoteOK, WeWorkRemotely RSS, Wellfound
4. **Cold email safety** â€” separate sending domains only, daily cap of 30 per inbox, unsubscribe link in every email
5. **No auto-apply to jobs** â€” you apply manually after reviewing AI-drafted cover notes
6. **Secrets in `.env` only** â€” never hardcoded, `.env` is gitignored

---

## Build Order (Phases)

- **Phase 0** â€” Scaffold (this step) âœ…
- **Phase 1** â€” Agent 1: LinkedIn Content Agent
- **Phase 2** â€” Agent 3: Remote Job Hunter
- **Phase 3** â€” Agent 2: Lead Gen + Enrichment Engine

---

## Tech Stack

- Python 3.11+
- Anthropic Claude API
- SQLite (upgradeable to Postgres)
- Telegram Bot (`python-telegram-bot`)
- APScheduler for scheduling
- python-dotenv for config
