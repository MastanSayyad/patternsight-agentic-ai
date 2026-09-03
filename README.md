### PatternSight Agentic Ai
**Agentic Operational Memory & Prevention Network for Insurance Operations**

> **PatternSight transforms historical operational knowledge into actionable intelligence, helping insurance support teams resolve incidents faster and prevent recurring failures.**

<!-- Built for the **Agentic AI Hackathon: Build with Neuro® AI Multi-Agent Accelerator (Neuro SAN)**

- Team: **Tacet Discord**  
-  Members: **Mastan Babu Sayyad**, **Gunashree B**
- Track: **Track 2 - Vibe Coding + Grounding**  
- Organizer: **Cognizant AI Lab (CAIL)** -->

<!-- ## Overview

Insurance support teams often spend significant time investigating production incidents, batch failures, claim-processing issues, and underwriting exceptions.

Many of these issues have occurred before, but valuable operational knowledge remains scattered across:

- Incident tickets
- Support teams
- Knowledge repositories
- Individual SMEs

As a result:

- Similar incidents are repeatedly investigated from scratch
- Resolution time increases
- Institutional knowledge is difficult to retain
- Recurring root causes remain unnoticed

**PatternSight** addresses this challenge by acting as an **operational memory layer** that retrieves historical incidents, identifies recurring patterns, recommends resolutions, and supports human decision-making through a multi-agent workflow powered by Neuro SAN.



# Problem Statement

In insurance application support and operations, resolving production incidents requires searching historical tickets and knowledge repositories to determine:

- What happened?
- Has it happened before?
- What was the root cause?
- How was it fixed?
- Who resolved it?

This process is often manual, time-consuming, and highly dependent on experienced SMEs.



# Solution

PatternSight is a multi-agent incident intelligence and prevention system that:

✅ Retrieves similar historical incidents

✅ Suggests likely root causes

✅ Identifies recurring operational patterns

✅ Recommends resolutions

✅ Identifies responsible support teams

✅ Estimates resolution timelines

✅ Includes human review before recommendations are finalized



# Business Value

### Reduce Investigation Time

Surface similar incidents and previous resolutions instantly.

### Reduce SME Dependency

Provide junior support engineers with relevant historical context.

### Detect Recurring Problems

Identify chronic operational issues before they become larger failures.

### Preserve Institutional Knowledge

Convert scattered operational history into reusable organizational knowledge.

### Improve Decision Making

Provide grounded recommendations with supporting evidence.



# High-Level Architecture

```text
Ingestion Agent
        ↓
Similarity Retrieval Agent
        ↓
Root Cause Suggestion Agent
        ↓
Recurring Pattern Agent
        ↓
Resolution Recommender Agent
        ↓
Review Agent (Human-in-the-Loop)
```



# Agent Responsibilities

## Ingestion Agent

Responsibilities:

- Receive incoming incident description
- Normalize incident information
- Extract key details

Example:

```text
Claim processing batch failed due to database timeout.
```



## Similarity Retrieval Agent

Responsibilities:

- Search historical incident corpus
- Find most relevant incidents
- Return similarity scores

Answers:

```text
Have we seen this before?
```



## Root Cause Suggestion Agent

Responsibilities:

- Analyze matched historical incidents
- Suggest likely root cause
- Flag knowledge gaps if no suitable match exists

Answers:

```text
What most likely caused this issue?
```



## Recurring Pattern Agent

Responsibilities:

- Count historical occurrences
- Detect recurring operational issues
- Highlight chronic problem categories

Answers:

```text
Is this a one-time event or recurring issue?
```



## Resolution Recommender Agent

Responsibilities:

- Retrieve previous resolutions
- Recommend corrective actions
- Identify support ownership
- Estimate resolution timeline

Answers:

```text
How was this fixed before?
Who should resolve it?
```



## Review Agent

Responsibilities:

- Present recommendation package
- Require human approval
- Prevent automated acceptance of unsupported conclusions

Answers:

```text
Is this recommendation ready for action?
```



# Technology Stack

## Framework

- Neuro SAN Studio
- Neuro SAN Multi-Agent Orchestration

## Language

- Python 3.11+

## Configuration

- HOCON

## Retrieval & Similarity

- scikit-learn TF-IDF
- Cosine Similarity

Optional:

- sentence-transformers embeddings

## Data

- Synthetic Insurance Incident Corpus
- Markdown Knowledge Base

## LLM Providers

Designed to support:

- Gemini
- Groq
- Mistral

through Neuro SAN LLM configurations and fallbacks.



# Repository Structure

```text
patternsight-agentic-ai/
├── README.md
├── pyproject.toml
├── .env
├── .gitignore
│
├── config/
│   └── llm_config.hocon
│
├── registries/
│   └── patternsight.hocon
│
├── coded_tools/
│   ├── incident_matcher.py
│   └── pattern_counter.py
│
├── data/
│   └── synthetic_incidents.json
│
├── kb/
│   ├── db_connection_pool.md
│   ├── message_queue_failure.md
│   └── external_api_validation_gap.md
│
└── docs/
    ├── architecture.md
    ├── demo_script.md
    └── project_summary.md
```



# Setup

Create project:

```bash
uv init
```

Create virtual environment:

```bash
uv venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

Install Neuro SAN Studio:

```bash
uv add neuro-san-studio
```

Initialize Neuro SAN:

```bash
ns init
```

Verify configuration:

```bash
ns check-config
```

Verify LLM setup:

```bash
ns check-llm-keys
```

Import network:

```bash
ns import
```

Run server:

```bash
ns run
```



# Example Workflow

Input:

```text
Claim processing batch failed due to database connection timeout.
```

PatternSight:

1. Normalizes the incident
2. Searches historical incidents
3. Finds similar incidents
4. Proposes root cause
5. Checks recurrence frequency
6. Recommends resolution
7. Identifies ownership team
8. Presents recommendation for review

Output:

```text
Match Confidence: 92%

Likely Root Cause:
Database Connection Pool Exhaustion

Occurrences:
14 Historical Matches

Recommended Resolution:
Restart service and increase connection pool size

Support Team:
Middleware Support

Estimated Resolution Time:
2 Hours

Status:
Recurring Issue Detected
```



# Future Enhancements

## Knowledge Graph Integration

Replace file-based retrieval with graph-based reasoning.

Possible technologies:

- Neo4j
- GraphRAG



## Impact Analysis Agent

Determine downstream business impact of incidents.

Examples:

- Claims processing delays
- Underwriting disruption
- Batch processing failures



## Automated Knowledge Creation

Generate new KB articles when previously unseen incidents are resolved.



## Advanced Enterprise Deployments

Support:

- Azure OpenAI
- Bedrock
- Enterprise Knowledge Sources
- Governance Workflows



# Compliance

This project uses:

✅ Synthetic incident data

✅ Synthetic knowledge base content

✅ Open-source frameworks

The solution does **not** use:

❌ Production incidents

❌ Customer data

❌ Personal data (PII)

❌ Confidential organizational information


 -->


