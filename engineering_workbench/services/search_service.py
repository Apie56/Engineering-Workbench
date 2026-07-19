"""Unified in-memory search across Engineering Workbench information."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from uuid import UUID

from engineering_workbench.services.knowledge_service import KnowledgeService
from engineering_workbench.services.project_service import ProjectService
from engineering_workbench.services.resource_service import ResourceService
from engineering_workbench.services.workspace_service import WorkspaceService


@dataclass(frozen=True, slots=True)
class SearchResult:
    """A discoverable platform entity returned by unified search."""

    entity_type: str
    entity_id: UUID
    title: str
    summary: str
    entity: Any


class SearchService:
    """Search registered platform information through one consistent interface."""

    def __init__(
        self,
        project_service: ProjectService,
        workspace_service: WorkspaceService,
        resource_service: ResourceService,
        knowledge_service: KnowledgeService,
    ) -> None:
        self._project_service = project_service
        self._workspace_service = workspace_service
        self._resource_service = resource_service
        self._knowledge_service = knowledge_service

    def search(self, query: str) -> tuple[SearchResult, ...]:
        """Return entities whose searchable text contains ``query``.

        This first implementation searches information already held by platform
        services. Persistence and indexing are deliberately deferred to later
        sprints.
        """
        needle = query.strip().casefold()
        if not needle:
            raise ValueError("Search query must not be blank")

        results: list[SearchResult] = []
        for project in self._project_service.list():
            self._append_if_match(
                results, needle, "project", project.id, project.name, project.description, project
            )
        for workspace in self._workspace_service.list():
            self._append_if_match(
                results,
                needle,
                "workspace",
                workspace.id,
                workspace.name,
                f"{workspace.workspace_type} {workspace.description}",
                workspace,
            )
            for module in workspace.modules:
                self._append_if_match(
                    results, needle, "module", module.id, module.name, module.description, module
                )
                for tool in module.tools:
                    self._append_if_match(
                        results, needle, "tool", tool.id, tool.name, tool.description, tool
                    )
        for resource in self._resource_service.list():
            self._append_if_match(
                results,
                needle,
                "resource",
                resource.id,
                resource.name,
                resource.resource_type,
                resource,
            )
        for knowledge in self._knowledge_service.list():
            self._append_if_match(
                results,
                needle,
                "knowledge",
                knowledge.id,
                knowledge.title,
                f"{knowledge.knowledge_type} {knowledge.content}",
                knowledge,
            )
        return tuple(sorted(results, key=lambda result: (result.title.casefold(), result.entity_type)))

    @staticmethod
    def _append_if_match(
        results: list[SearchResult],
        needle: str,
        entity_type: str,
        entity_id: UUID,
        title: str,
        summary: str,
        entity: Any,
    ) -> None:
        searchable_text = f"{title} {summary}".casefold()
        if needle in searchable_text:
            results.append(SearchResult(entity_type, entity_id, title, summary, entity))
