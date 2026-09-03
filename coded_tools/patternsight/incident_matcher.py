"""
incident_matcher.py

CodedTool for PatternSight. Called by similarity_retrieval_agent.

Searches a synthetic historical incident corpus for incidents similar to a
new incident description, using TF-IDF + cosine similarity. Runs entirely
locally - no external API, no cost, no rate limit.

Expected data file: data/synthetic_incidents.json
"""

import json
import logging
import os
from typing import Any
from typing import Union

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from neuro_san.interfaces.coded_tool import CodedTool

DATA_PATH = "data/synthetic_incidents.json"


class IncidentMatcher(CodedTool):
    """Finds similar past incidents via TF-IDF cosine similarity."""

    # Zero-argument constructor, as required by the framework.
    def __init__(self):
        self.incidents: list[dict[str, Any]] = self._load_incidents()
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.corpus_matrix = None
        if self.incidents:
            descriptions = [inc["description"] for inc in self.incidents]
            self.corpus_matrix = self.vectorizer.fit_transform(descriptions)

    def _load_incidents(self) -> list[dict[str, Any]]:
        if not os.path.exists(DATA_PATH):
            return []
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    async def async_invoke(self, args: dict[str, Any], sly_data: dict[str, Any]) -> Union[dict[str, Any], str]:
        logger = logging.getLogger(self.__class__.__name__)
        logger.debug("========== Calling %s ==========", self.__class__.__name__)

        incident_text: str = args.get("incident_text")
        top_k: int = args.get("top_k", 3)

        if not incident_text:
            return "Error: 'incident_text' is required."

        if self.corpus_matrix is None:
            return "Error: incident corpus is empty or not found at data/synthetic_incidents.json."

        query_vec = self.vectorizer.transform([incident_text])
        similarities = cosine_similarity(query_vec, self.corpus_matrix)[0]

        # Rank incidents by similarity, descending
        ranked_indices = similarities.argsort()[::-1][:top_k]

        matches = []
        for idx in ranked_indices:
            score = float(similarities[idx])
            if score <= 0.0:
                continue
            incident = self.incidents[idx]
            matches.append({
                "incident_id": incident.get("incident_id"),
                "description": incident.get("description"),
                "root_cause": incident.get("root_cause"),
                "root_cause_category": incident.get("root_cause_category"),
                "resolution": incident.get("resolution"),
                "responsible_team": incident.get("responsible_team"),
                "estimated_resolution_time_hours": incident.get("estimated_resolution_time_hours"),
                "similarity_score": round(score, 3),
            })

        logger.debug(">>> %s returning %d matches", self.__class__.__name__, len(matches))
        return {"matches": matches}

    # Pure in-memory math, guaranteed non-blocking - safe to delegate to the
    # async version for callers that still use the sync invoke() path.
    def invoke(self, args: dict[str, Any], sly_data: dict[str, Any]) -> Union[dict[str, Any], str]:
        import asyncio
        return asyncio.run(self.async_invoke(args, sly_data))