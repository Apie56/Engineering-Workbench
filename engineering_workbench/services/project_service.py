"""In-memory coordination for engineering projects."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from uuid import UUID

from engineering_workbench.core import Project


class ProjectService:
    """Create and retrieve projects without defining their persistence mechanism."""

    def __init__(self) -> None:
        self._projects: dict[UUID, Project] = {}

    def create(
        self,
        name: str,
        description: str = "",
        metadata: Mapping[str, Any] | None = None,
    ) -> Project:
        """Create and register an engineering project."""
        project = Project(name=name, description=description, metadata=metadata or {})
        self.add(project)
        return project

    def add(self, project: Project) -> None:
        """Register a project exactly once."""
        if project.id in self._projects:
            raise ValueError(f"Project '{project.name}' is already registered")
        self._projects[project.id] = project

    def get(self, project_id: UUID) -> Project:
        """Return a project or raise a clear error when it does not exist."""
        try:
            return self._projects[project_id]
        except KeyError as error:
            raise KeyError(f"No project with id '{project_id}' is registered") from error

    def find(self, project_id: UUID) -> Project | None:
        """Return a project when it is registered, otherwise ``None``."""
        return self._projects.get(project_id)

    def list(self) -> tuple[Project, ...]:
        """Return registered projects in creation order."""
        return tuple(self._projects.values())
