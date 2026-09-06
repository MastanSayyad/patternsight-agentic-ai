# PatternSight Architecture

This reflects the actual working `patternsight.hocon` confirmed via live runs, not the
earlier draft. If this ever drifts from the real file, the file is the source of truth.


## High-Level Flow

```
                         USER MESSAGE
                              │
                              ▼
                  ┌─────────────────────────┐
                  │   ingestion_agent          │  ← front man / entry point
                  │   (triage: A / B / C)      │
                  └──────────────┬──────────────┘
                                 │  (Case B only)
                                 ▼
                  ┌─────────────────────────┐
                  │ similarity_retrieval_      │
                  │  agent                     │
                  └──────────────┬──────────────┘
                                 │
                         ┌───────┴───────┐
                         ▼               │
                ┌─────────────────┐      │
                │ incident_matcher  │      │  (coded tool - TF-IDF, local)
                └─────────────────┘      │
                                 │◄───────┘
                                 ▼
                  ┌─────────────────────────┐
                  │ root_cause_suggestion_     │
                  │  agent                     │  ← Knowledge Gap decision point
                  └──────────────┬──────────────┘
                                 ▼
                  ┌─────────────────────────┐
                  │ recurring_pattern_agent    │
                  └──────────────┬──────────────┘
                                 │
                         ┌───────┴───────┐
                         ▼               │
                ┌─────────────────┐      │
                │ pattern_counter   │      │  (coded tool - date-window count, local)
                └─────────────────┘      │
                                 │◄───────┘
                                 ▼
                  ┌─────────────────────────┐
                  │ resolution_recommender_    │
                  │  agent                     │
                  └──────────────┬──────────────┘
                                 ▼
                  ┌─────────────────────────┐
                  │  review_agent              │  ← formats output, asks approval
                  └──────────────┬──────────────┘
                                 ▼
                    RESULT RELAYED BACK VERBATIM
                    THROUGH EVERY AGENT ABOVE
                                 ▼
                         USER SEES FINAL ANSWER
                    ending in the approval question
                                 │
                                 ▼
                  ┌─────────────────────────┐
                  │  USER REPLIES ("approved")│
                  └──────────────┬──────────────┘
                                 ▼
                  ingestion_agent Case C:
                  confirms pending question existed,
                  replies directly - NO re-run of the pipeline
```

## Agent Roster

| # | Agent | Type | Job |
|---|---|---|---|
| 1 | `ingestion_agent` | Front man (LLM) | Triages every message into Case A (chat), B (new incident), or C (approval reply). Relays downstream results verbatim. |
| 2 | `similarity_retrieval_agent` | LLM + tool caller | Calls `incident_matcher` once, hands result to root cause agent. |
| — | `incident_matcher` | Coded tool (Python) | TF-IDF cosine similarity search over `data/synthetic_incidents.json`. Zero LLM cost. |
| 3 | `root_cause_suggestion_agent` | LLM | Decides Knowledge Gap vs. real root cause, using the 0.4 similarity threshold. |
| 4 | `recurring_pattern_agent` | LLM + tool caller | Calls `pattern_counter` once (skipped if Knowledge Gap), quotes the count verbatim. |
| — | `pattern_counter` | Coded tool (Python) | Counts root-cause occurrences in a 90-day window. Zero LLM cost. |
| 5 | `resolution_recommender_agent` | LLM | Compiles resolution steps, responsible team, ETA; adds permanent-fix note if recurring. |
| 6 | `review_agent` | LLM | Formats final package with fixed headers; ends with the mandatory approval question. |

## Key Design Decisions

**1. Triage before pipeline (`ingestion_agent`, Case A/B/C).**
Prevents "Hi" or small talk from burning six LLM calls. Also prevents a stray "approved"
from falsely confirming a recommendation that was never actually made — Case C explicitly
checks that a real pending approval question preceded it.

**2. "EXACTLY ONCE" / verbatim-relay language throughout.**
Free-tier models tend to re-deliberate after a tool or agent responds, causing the chain to
bounce backward instead of moving forward (this was observed directly in early testing —
`otrace` logs showed repeated climbing and re-descending). Explicit single-pass, no-loopback
instructions fixed this.

**3. Knowledge Gap threshold: similarity score < 0.4.**
Below this, the system refuses to guess a root cause and instead recommends creating a new
KB article. This is a deliberate honesty mechanism — a wrong confident answer is worse than
an honest "no precedent found" in an operations context.

**4. Recurrence threshold: 3+ occurrences within a 90-day rolling window.**
Computed live from `datetime.today()` at call time, not from a fixed date — meaning the
exact count can shift slightly as real time passes, even with unchanged data. Worth
re-verifying close to demo day.

**5. `max_execution_seconds: 600`.**
Raised from the framework default to give a full 6-hop chain on free-tier models enough
headroom to finish without hitting a hard timeout mid-run.

**6. Two coded tools, zero LLM cost for retrieval/counting.**
`incident_matcher` and `pattern_counter` are pure Python (`scikit-learn` TF-IDF, plain date
arithmetic) — the LLM is only used for the four reasoning/formatting agents, not for search
or counting. This is what makes the system usable on a free-tier API key.

**7. Human-in-the-loop is a real turn boundary, not a formality.**
`review_agent`'s approval question is the mandatory last line of the first turn. The system
does not proceed past it automatically — it waits for a second, separate user message before
anything is "finalized."

## Data

- `data/synthetic_incidents.json` — fully synthetic, no PII/confidential data, per hackathon
  rules. Fields: `incident_id`, `description`, `root_cause`, `root_cause_category`,
  `resolution`, `responsible_team`, `estimated_resolution_time_hours`, `date`.

## Config

- `config/llm_config.hocon` — fallback chain (Groq → Gemini → Mistral, reordered for speed
  on free tiers).
