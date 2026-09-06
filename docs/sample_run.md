# PatternSight Sample Run (Captured)

This is a real, unedited transcript from a successful run against the current
`patternsight.hocon` and `data/synthetic_incidents.json`. Kept here as a backup in case
live LLM quota runs out during judging, this proves the system works end-to-end even if
the live demo can't complete on the day.

![image](https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/docs/Neuro-San-Ui.png)

## Turn 1: New Incident

**User:**
> Batch job nightly_claims_load failed with a database connection timeout.

<img width="1061" height="510" alt="image" src="https://github.com/MastanSayyad/patternsight-agentic-ai/blob/main/docs/patternsight-agent.gif" />

**PatternSight:**

<img width="1215" height="735" alt="image" src="https://github.com/user-attachments/assets/c951e8b3-1234-4cce-b9c7-732ebb31e692" />


> ### Similar Incidents
> Best Match: INC-001 (Similarity score: 0.766)
>
> ### Root Cause
> Database connection pool exhaustion during peak nightly batch window.
>
> ### Recurrence
> This root cause has occurred exactly 4 times in the last 90 days. This is flagged as
> RECURRING. A permanent fix is recommended rather than a repeat workaround.
>
> ### Recommendation
> **Responsible Team:** Database Administration (DBA) Team
> **Estimated Resolution Time:** 45 minutes
> **Resolution Steps:**
> 1. Increase the database connection pool size limit for the batch processing instance.
> 2. Reset/flush stalled connection pools.
> 3. Re-run the `nightly_claims_load` batch job.
>
> Do you approve this recommendation as-is, or would you like to correct the root cause,
> responsible team, or resolution steps before it is finalized?

## Turn 2: Human Approval

**User:**
> approved

**PatternSight:**
> Recommendation finalized and logged.

<img width="1236" height="281" alt="image" src="https://github.com/user-attachments/assets/bf0ace5d-b741-4c4c-8488-4e6065d295cb" />

## What This Demonstrates

- **Real retrieval, not a lookup table:** the 0.766 similarity score is computed live by
  `incident_matcher` (TF-IDF cosine similarity) against `data/synthetic_incidents.json` 
  it is not hardcoded.
- **Real counting, not a guess:** "exactly 4 times in the last 90 days" comes directly from
  `pattern_counter`, which counts `db_connection_pool` occurrences within a rolling 90-day
  window computed from the actual current date at run time. This number will shift slightly
  over time as older incidents age out of the window that is expected behavior, not a bug.
- **Genuine human-in-the-loop gate:** the system stops after Turn 1 and waits. Turn 2 is a
  separate message from a separate model call (`ingestion_agent`'s Case C), not a scripted
  continuation — the recommendation is not treated as final until the human explicitly
  approves it.

## Typical Agent Trace for a Run Like This

The full six-agent chain fires once per hop, in strict forward order, for a matched
incident like this one:

```
otrace: [ingestion_agent]
otrace: [ingestion_agent, similarity_retrieval_agent]
otrace: [..., incident_matcher]
otrace: [..., root_cause_suggestion_agent]
otrace: [..., recurring_pattern_agent]
otrace: [..., pattern_counter]
otrace: [..., resolution_recommender_agent]
otrace: [..., review_agent]
```

(Note: this trace shape is documented from prior validated runs against this same agent
network; it is not pasted from the exact run above, since the trace log for that specific
run was not captured. The final answer above is the real, verbatim output.)
