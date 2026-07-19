"""In-memory coordination for supporting engineering resources."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from uuid import UUID

from engineering_workbench.core import Resource
from engineering_workbench.services.workspace_service import WorkspaceService


class ResourceService:
    """Create resources and attach them to registered workspaces."""

    def __init__(self, workspace_service: WorkspaceService) -> None:
        self._workspace_service = workspace_service
        self._resources: dict[UUID, Resource] = {}

    def create(
        self,
        name: str,
        resource_type: str,
        *,
        location: str | None = None,
        metadata: Mapping[str, Any] | None = None,
        workspace_id: UUID | None = None,
    ) -> Resource:
        """Create a resource and optionally attach it to a workspace."""
        resource = Resource(name, resource_type, location, metadata or {})
        workspace = self._workspace_service.get(workspace_id) if workspace_id is not None else None
        self.add(resource)
        if workspace is not None:
            workspace.add_resource(resource)
        return resource

    def add(self, resource: Resource) -> None:
        """Register a resource exactly once."""
        if resource.id in self._resources:
            raise ValueError(f"Resource '{resource.name}' is already registered")
        self._resources[resource.id] = resource

    def get(self, resource_id: UUID) -> Resource:
        """Return a resource or raise a clear error when it does not exist."""
        try:
            return self._resources[resource_id]
        except KeyError as error:
            raise KeyError(f"No resource with id '{resource_id}' is registered") from error

    def list(self) -> tuple[Resource, ...]:
        """Return registered resources in creation order."""
        return tuple(self._resources.values())
