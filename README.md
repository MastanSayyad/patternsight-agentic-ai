![Release](https://img.shields.io/badge/Version-v0.1.0-white?logo=github&style=flat)

<div align="center">
<img width="400"alt=" logo" src="https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/docs/Logo.gif"/>

![Team](https://img.shields.io/badge/Team-Tacet%20Discord-black?style=flat)
![Cognizant](https://img.shields.io/badge/Cognizant-blue?style=flat)
[![Documentation](https://img.shields.io/badge/Documentation-Read%20Docs-yellow?logo=read-the-docs&style=flat)](https://github.com/MastanSayyad/patternsight-agentic-ai/tree/main/docs)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NeuroSAN](https://img.shields.io/badge/Neuro%20SAN-4B32C3?style=for-the-badge)
![HOCON](https://img.shields.io/badge/HOCON-543B2A?style=for-the-badge)
![scikitlearn](https://img.shields.io/badge/scikit--learn-green?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Mistral](https://img.shields.io/badge/Mistral%20AI-FA520F?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-black?style=for-the-badge)
![uv](https://img.shields.io/badge/uv-DE5FE9?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
</div>

### PatternSight Agentic Ai ✦ [(Sample Run)](https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/docs/sample_run.md)

> **Transforms historical operational knowledge into actionable intelligence, helping insurance support teams resolve incidents faster and prevent recurring failures.**

Built for the **Agentic AI Hackathon: Build with [Neuro® AI](https://github.com/cognizant-ai-lab/neuro-san-studio) Multi-Agent Accelerator (Neuro SAN)**
- Team: **Tacet Discord**  
-  Members: **Mastan Babu Sayyad**, **Gunashree B**
- Track: **Track 2**  
- Organizer: [**Cognizant AI Lab (CAIL)**](https://github.com/cognizant-ai-lab)

## Overview
Insurance teams often spend significant time investigating production incidents, batch failures, claim-processing issues, and underwriting exceptions.Many of these issues have occurred before, but valuable operational knowledge remains scattered across Incident tickets, Support teams, Knowledge repositories, Documentations and Individual SMEs

**PatternSight** addresses this challenge by acting as an **operational memory layer** that 
- Retrieves similar historical incidents
- Suggests likely root causes
- Identifies recurring patterns
- Recommends resolutions
- Estimates resolution timelines
and Supports human decision-making through a multi-agent workflow powered by [Neuro SAN](https://github.com/cognizant-ai-lab/neuro-san-studio).

## Architecture ⚙︎
> This reflects the actual working `patternsight.hocon`

<p align="center">
        <img src="https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/docs/architecture-diagram.png">
</p>

## Agent Responsibilities ᵎ!ᵎ

| Agent | Responsibility | Decides |
|---|---|---|
| **Ingestion Agent** | Normalizes the incoming incident description | Frontman, router/normalizer |
| **Similarity Retrieval Agent** | Searches the synthetic historical corpus for similar past incidents | "Which past incidents look like this one?" |
| **Root Cause Suggestion Agent** | Proposes the likely root cause, or flags a knowledge gap if no good match exists | "What probably caused this, and do we even have precedent?" |
| **Recurring Pattern Agent** | Counts how often this root cause has occurred historically | "Is this a one-off or a chronic issue?" |
| **Resolution Recommender Agent** | Extracts resolution steps, responsible team, ETA; recommends a permanent fix if recurring | "What fixed it before, who owns it, and does it need a permanent fix?" |
| **Review Agent** | Human confirms before the recommendation is finalized | "Is this good enough to act on?" |

<p align="center">
        <img src="https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/docs/patternsight-agent.gif">
</p>

## Project Structure 🗁

```text
patternsight-agentic-ai/
│
├── README.md                           
├── .gitignore                             
├── .env.example                           # template - real keys go in .env (untracked)
├── pyproject.toml                         
│
├── config/
│   └── llm_config.hocon                  
│
├── registries/
│   ├── manifest.hocon                     # root manifest - includes patternsight entry
│   ├── aaosa.hocon                       
│   ├── aaosa_basic.hocon                 
│   ├── aaosa_basic_debug.hocon          
│   ├── expertise_scoping_instructions.hocon  
│   └── patternsight/
│       ├── patternsight.hocon             # main agent network
│       └── manifest.hocon                 
│
├── coded_tools/
│   ├── __init__.py
│   └── patternsight/
│       ├── __init__.py
│       ├── incident_matcher.py            # TF-IDF similarity search, validated live
│       └── pattern_counter.py             # recurrence counting, validated live
│
├── data/
│   └── synthetic_incidents.json            # fully synthetic
│
└── docs/
    ├── architecture.md                    
    ├── project_summary.md              
    └── sample_run.md                                                   
```

## Features ᵎ!ᵎ

| Feature | Description | Delivered By |
|---|---|---|
| **Historical Incident Retrieval** | Retrieves similar past incidents from a historical corpus using TF-IDF similarity search — grounded in real data, not guesswork. | `similarity_retrieval_agent` + `incident_matcher` (coded tool) |
| **Root Cause Suggestion** | Proposes the most likely root cause based on matched precedent, explicitly citing which past incident(s) it's based on. | `root_cause_suggestion_agent` |
| **Recurring Pattern Detection** | Counts how often a given root cause has occurred within a rolling time window and flags chronic, recurring issues. | `recurring_pattern_agent` + `pattern_counter` (coded tool) |
| **Resolution Recommendation** | Recommends concrete resolution steps drawn from how the matched precedent was previously resolved. | `resolution_recommender_agent` |
| **Responsible Team Identification** | Identifies which support team owns the resolution, based on historical precedent. | `resolution_recommender_agent` |
| **Resolution Time Estimation** | Provides an estimated resolution time, drawn from the matched historical incident. | `resolution_recommender_agent` |
| **Permanent Fix Guidance** | When an issue is flagged recurring, recommends a permanent structural fix instead of a repeat workaround. | `resolution_recommender_agent` |
| **Human-in-the-Loop Review** | Presents the full recommendation and requires explicit human approval before anything is treated as final. | `review_agent` |

## Technology Stack </>


- [Neuro SAN Studio](https://github.com/cognizant-ai-lab/neuro-san-studio)
- [Neuro SAN](https://github.com/cognizant-ai-lab/neuro-san) Multi-Agent Orchestration
- Python 3.11+
- HOCON
- scikit-learn TF-IDF, Cosine Similarity
- Synthetic Insurance Incident Corpus
- Gemini (Groq, Mistral through Neuro SAN LLM configurations and fallbacks.)


## Installation ⓘ

### Step 1: Clone the Repository

```bash
git clone https://github.com/MastanSayyad/patternsight-agentic-ai
cd patternsight-agentic-ai
```

> [!NOTE]
> If you don't have Git installed, you can download the ZIP file from the repository page.

### Step 2: Prerequisites

> [!IMPORTANT]
> You need Python 3.11+ installed. We recommend [`uv`](https://docs.astral.sh/uv/) for
> package and environment management, it's faster and more reliable than plain `pip`.

```bash
uv init
uv venv
```

> [!TIP]
> Don't have `uv`? Use the standard library instead:
> ```bash
> python -m venv .venv
> ```

### Step 3: Activate the Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```
**macOS / Linux:**
```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies

```bash
uv add neuro-san-studio scikit-learn langchain-mistralai
```
### Step 5: Set Up Environment Variables

Create `.env` and fill in your own API keys (Gemini, Mistral, Groq whichever you have).

> [!WARNING]
> Never commit your real `.env` file. It's already listed in `.gitignore`, but double-check.

### Step 6: Initialize Neuro SAN

```bash
ns init
```

> [!NOTE]
> The `ns init` menu only offers OpenAI, Anthropic, and Gemini. Mistral and Groq aren't
> Update manually `config/llm_config.hocon`.

### Step 7: Verify Your Setup

```bash
ns check-llm-keys
ns check-config
```

### Step 8: Validate the Network

```bash
ns validate registries/patternsight/patternsight.hocon --verbose
```
This checks the HOCON structure and agent references without making any API calls or
using any quota safe to run as often as you like.

### Step 9: Run the Server

```bash
ns run
```

- Server: `http://localhost:8080`
- nsflow UI: `http://localhost:4173`

![image](https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/docs/Neuro-San-Ui.png)

---

**For more information, see:**
- [README.md](https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/README.md) - *Project overview*
- [Project Summary](https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/docs/Project_Summary.md) - *Project report including objectives, architecture, and outcomes*
- [Sample Run](https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/docs/sample_run.md) - *Backup Run in case live LLM quota runs out*


