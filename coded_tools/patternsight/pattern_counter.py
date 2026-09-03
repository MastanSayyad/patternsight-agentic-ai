"""
pattern_counter.py

CodedTool for PatternSight. Called by recurring_pattern_agent.

Given a root cause category, counts how many times it has occurred in the
historical incident corpus within a recurrence window (default: 90 days).
Pure counting - no LLM call needed, runs fully locally.

Expected data file: data/synthetic_incidents.json (same file used by
incident_matcher.py). Each record must have a "date" field in
YYYY-MM-DD format and a "root_cause_category" field.
"""

import json
import logging
import os
from datetime import datetime
from datetime import timedelta
from typing import Any
from typing import Union

from neuro_san.interfaces.coded_tool import CodedTool

DATA_PATH = "data/synthetic_incidents.json"

# Adjust based on how your demo data is spread out.
RECURRENCE_WINDOW_DAYS = 90
# Number of occurrences within the window before something counts as
# "recurring" rather than a one-off.
RECURRENCE_THRESHOLD = 3


class PatternCounter(CodedTool):
    """Counts historical occurrences of a root cause category within a time window."""

    # Zero-argument constructor, as required by the framework.
    def __init__(self):
        self.incidents: list[dict[str, Any]] = self._load_incidents()

    def _load_incidents(self) -> list[dict[str, Any]]:
        if not os.path.exists(DATA_PATH):
            return []
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    async def async_invoke(self, args: dict[str, Any], sly_data: dict[str, Any]) -> Union[dict[str, Any], str]:
        logger = logging.getLogger(self.__class__.__name__)
        logger.debug("========== Calling %s ==========", self.__class__.__name__)

        category: str = args.get("root_cause_category")
        if not category:
            return "Error: 'root_cause_category' is required."

        reference_date = datetime.today()
        window_start = reference_date - timedelta(days=RECURRENCE_WINDOW_DAYS)

        count = 0
        for incident in self.incidents:
            if incident.get("root_cause_category") != category:
                continue
            incident_date_str = incident.get("date")
            if not incident_date_str:
                continue
            try:
                incident_date = datetime.strptime(incident_date_str, "%Y-%m-%d")
            except ValueError:
                continue
            if window_start <= incident_date <= reference_date:
                count += 1

        result = {
            "root_cause_category": category,
            "count": count,
            "window_days": RECURRENCE_WINDOW_DAYS,
            "is_recurring": count >= RECURRENCE_THRESHOLD,
        }
        logger.debug(">>> %s returning %s", self.__class__.__name__, result)
        return result

    # Pure in-memory counting, guaranteed non-blocking.
    def invoke(self, args: dict[str, Any], sly_data: dict[str, Any]) -> Union[dict[str, Any], str]:
        import asyncio
        return asyncio.run(self.async_invoke(args, sly_data))