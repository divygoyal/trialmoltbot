# Trial Molt Bot: Autonomous SEO & Vibecoding OS

Trial Molt Bot is an "Autonomous Web Growth" platform that transforms SEO management from a manual chore into a "Vibecoding" experience. It connects Google Search Console (GSC) data with GitHub repository access to provide one-click, AI-driven site optimizations via Telegram.

## 🏛 System Design

### 1. High-Level Architecture
The platform follows a **Centralized Brain, Decentralized Muscle** model:
- **Command Center:** A FastAPI backend that orchestrates data flow between GSC, GitHub, and Telegram.
- **The Brain:** OpenClaw sub-agents that perform deep SEO analysis and code generation.
- **The Interface:** A Telegram Bot for real-time alerts and "Click-to-Deploy" optimizations, plus a Next.js dashboard for onboarding.

### 2. Data Flow
1. **Ingestion:** Backend pulls GSC data (Keywords, Impressions, Position) via API.
2. **Analysis:** `seo_analyzer.py` identifies "Striking Distance" keywords (Pos 11-20) and "CTR Healers" (High Imp, Low CTR).
3. **Recommendation:** The Telegram Bot pings the user with a specific optimization strategy.
4. **Action (Vibecoding):** Upon user approval, the `github_manager.py` uses the GitHub API to fetch source code, apply the AI-generated fix, and push a commit directly to the repository.

### 3. Component Breakdown
- **`/backend`**: FastAPI server handling OAuth, GitHub integration, and the Vibecoding engine.
- **`/frontend`**: Next.js dashboard for user onboarding and system status.
- **`/agents`**: OpenClaw logic templates for specialized SEO and Coding tasks.
- **`bot.py`**: The Telegram interface for human-in-the-loop approvals.

---

## 🚀 Key Features (The God Vision)

- **Striking Distance Automator:** One-click push to move Page 2 keywords to Page 1.
- **CTR Healer:** AI-rewritten Meta Titles/Descriptions based on live GSC performance.
- **Self-Healing Web:** Automated broken link fixing and image optimization.
- **Vibecoding:** Natural language code edits via Telegram voice or text notes.

## 🛠 Tech Stack
- **Languages:** Python (Backend), TypeScript (Frontend)
- **Frameworks:** FastAPI, Next.js, Tailwind CSS
- **APIs:** GitHub REST API, Google Search Console API, Telegram Bot API
- **AI Engine:** OpenClaw (Multi-agent orchestration)

---
*Created with ❤️ by the Trial Molt Bot Team.*
