"""Project domain object."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from engineering_workbench.core._common import Metadata, new_id, require_text, utc_now
from engineering_workbench.core.workspace import Workspace


@dataclass(slots=True)
class Project:
    """A persistent engineering context containing related workspaces."""

    name: str
    description: str = ""
    metadata: Metadata = field(default_factory=dict)
    workspaces: list[Workspace] = field(default_factory=list)
    id: UUID = field(default_factory=new_id, init=False)
    created_at: datetime = field(default_factory=utc_now, init=False)
    updated_at: datetime = field(default_factory=utc_now, init=False)

    def __post_init__(self) -> None:
        self.name = require_text(self.name, "Project name")

    def add_workspace(self, workspace: Workspace) -> None:
        """Attach an engineering workflow to this project exactly once."""
        if self.get_workspace(workspace.id) is not None:
            raise ValueError(
                f"Workspace '{workspace.name}' is already in project '{self.name}'"
            )
        self.workspaces.append(workspace)
        self._touch()

    def remove_workspace(self, workspace_id: UUID) -> Workspace:
        """Remove and return a workspace by identity."""
        workspace = self.get_workspace(workspace_id)
        if workspace is None:
            raise KeyError(
                f"No workspace with id '{workspace_id}' exists in project '{self.name}'"
            )
        self.workspaces.remove(workspace)
        self._touch()
        return workspace

    def get_workspace(self, workspace_id: UUID) -> Workspace | None:
        """Return a workspace by identity when it belongs to this project."""
        return next(
            (workspace for workspace in self.workspaces if workspace.id == workspace_id),
            None,
        )

    def list_workspaces(self) -> tuple[Workspace, ...]:
        """Return an immutable view of the project's workspaces."""
        return tuple(self.workspaces)

    def _touch(self) -> None:
        self.updated_at = utc_now()
