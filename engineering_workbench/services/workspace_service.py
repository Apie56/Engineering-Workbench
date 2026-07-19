"""In-memory coordination for engineering workspaces."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from uuid import UUID

from engineering_workbench.core import Workspace
from engineering_workbench.services.project_service import ProjectService


class WorkspaceService:
    """Create standalone workspaces or attach them to a project context."""

    def __init__(self, project_service: ProjectService) -> None:
        self._project_service = project_service
        self._workspaces: dict[UUID, Workspace] = {}

    def create(
        self,
        name: str,
        workspace_type: str,
        *,
        description: str = "",
        context: Mapping[str, Any] | None = None,
        project_id: UUID | None = None,
    ) -> Workspace:
        """Create a workspace and optionally attach it to a registered project."""
        workspace = Workspace(
            name=name,
            workspace_type=workspace_type,
            description=description,
            context=context or {},
        )
        project = self._project_service.get(project_id) if project_id is not None else None
        self.add(workspace)
        if project is not None:
            project.add_workspace(workspace)
        return workspace

    def add(self, workspace: Workspace) -> None:
        """Register a workspace exactly once."""
        if workspace.id in self._workspaces:
            raise ValueError(f"Workspace '{workspace.name}' is already registered")
        self._workspaces[workspace.id] = workspace

    def get(self, workspace_id: UUID) -> Workspace:
        """Return a workspace or raise a clear error when it does not exist."""
        try:
            return self._workspaces[workspace_id]
        except KeyError as error:
            raise KeyError(f"No workspace with id '{workspace_id}' is registered") from error

    def find(self, workspace_id: UUID) -> Workspace | None:
        """Return a workspace when it is registered, otherwise ``None``."""
        return self._workspaces.get(workspace_id)

    def list(self) -> tuple[Workspace, ...]:
        """Return registered workspaces in creation order."""
        return tuple(self._workspaces.values())
