"""In-memory coordination for reusable engineering knowledge."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from uuid import UUID

from engineering_workbench.core import Knowledge


class KnowledgeService:
    """Create and retrieve knowledge that remains independent of projects."""

    def __init__(self) -> None:
        self._knowledge: dict[UUID, Knowledge] = {}

    def create(
        self,
        title: str,
        content: str,
        knowledge_type: str,
        *,
        source: str | None = None,
        metadata: Mapping[str, Any] | None = None,
    ) -> Knowledge:
        """Create and register reusable engineering knowledge."""
        knowledge = Knowledge(title, content, knowledge_type, source, metadata or {})
        self.add(knowledge)
        return knowledge

    def add(self, knowledge: Knowledge) -> None:
        """Register a knowledge record exactly once."""
        if knowledge.id in self._knowledge:
            raise ValueError(f"Knowledge '{knowledge.title}' is already registered")
        self._knowledge[knowledge.id] = knowledge

    def get(self, knowledge_id: UUID) -> Knowledge:
        """Return knowledge or raise a clear error when it does not exist."""
        try:
            return self._knowledge[knowledge_id]
        except KeyError as error:
            raise KeyError(f"No knowledge with id '{knowledge_id}' is registered") from error

    def list(self) -> tuple[Knowledge, ...]:
        """Return registered knowledge in creation order."""
        return tuple(self._knowledge.values())
