# PatternSight Agetic Ai | Project Summary

- **Team:** Tacet Discord (2 members)
- **Event:** Agentic AI Hackathon - Build with Neuro® AI Multi-Agent Accelerator (neuro-san)
- **Track:** Track 2 | Vibe Coding + Grounding
- **Framework:** Neuro SAN Studio

## Problem Statement

In insurance accounts application support and operations, resolving production incidents, batch
failures, claim processing issues, and underwriting exceptions requires searching across
**incident tickets, knowledge repositories, and past resolutions**. This is slow, dependent on
subject-matter experts, and the same root causes recur without anyone noticing the pattern
until it becomes chronic.

## Solution Overview

PatternSight is a six-agent Neuro SAN network that acts as an operational memory layer for
insurance support teams. Given a new incident description, it:

1. Retrieves similar past incidents from a historical corpus (local TF-IDF similarity search)
2. Reasons about the most probable root cause, explicitly citing precedent or honestly
   flags a knowledge gap when no good precedent exists, rather than guessing
3. Counts how often that specific root cause has recurred, flagging chronic issues
4. Compiles a resolution recommendation: fix steps, responsible team, estimated time
5. Gates the entire recommendation behind a human reviewer before it is treated as final

## Business Value

- **Faster investigation:** similar incidents and precedent are surfaced instantly instead
  of manual searching across tickets and tribal knowledge.
- **Reduced SME dependency:** junior support staff get a grounded starting point without
  needing a senior engineer's institutional memory.
- **Prevention, not just reaction:** recurring root causes are flagged explicitly, enabling
  permanent fixes instead of repeated workarounds.
- **Trust by design:** every recommendation is reviewed by a human before being finalized
  the system supports decisions, it does not make them unsupervised.

## Agent Architecture

| Agent | Role |
|---|---|
| `ingestion_agent` | Entry point; normalizes the incoming incident |
| `similarity_retrieval_agent` | Retrieves similar past incidents via the `incident_matcher` coded tool |
| `root_cause_suggestion_agent` | Proposes a root cause, or flags a knowledge gap |
| `recurring_pattern_agent` | Counts historical occurrences via the `pattern_counter` coded tool |
| `resolution_recommender_agent` | Compiles fix, responsible team, and ETA |
| `review_agent` | Human-in-the-loop approval gate |

Two coded tools (`incident_matcher.py`, `pattern_counter.py`) run entirely locally in Python no external API cost for the retrieval or counting steps, only the reasoning steps call
the LLM. This makes the system usable on free-tier LLM access.

## Neuro SAN

The design is a genuine sequential reasoning pipeline, not a single script wearing
agent-shaped configuration: each agent has a distinct decision to make (retrieve vs. reason
vs. count vs. recommend vs. approve), and the framework's agent-to-agent delegation is what
lets each step hand off cleanly with its own scoped instructions and tools. including two
custom Python coded tools integrated directly into the reasoning chain.

## Data & Compliance

All incident data is fully synthetic (20 records, written by the team), no real PII,
financial, medical, or confidential organizational data is used, per the hackathon's data
usage rules.

## Future Enhancements

- Migrate from TF-IDF/local search to a true knowledge graph (e.g. Neo4j) modeling explicit
  relationships between policies, claims, batch jobs, and incidents
- Add an Impact Analysis agent mapping root-cause categories to downstream process impact
- Auto-generate new knowledge base articles when a knowledge gap is resolved
- Swap free-tier LLM access for a stronger model as budget allows

## Team

**Tacet Discord**
- **Mastan Babu Sayyad:** Agents and Orchastration
- **Gunashre B:** Data and Tools 