"""Workspace domain object."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from engineering_workbench.core._common import Metadata, new_id, require_text, utc_now
from engineering_workbench.core.module import Module
from engineering_workbench.core.resource import Resource


@dataclass(slots=True)
class Workspace:
    """An engineering environment that orchestrates a workflow."""

    name: str
    workspace_type: str
    description: str = ""
    context: Metadata = field(default_factory=dict)
    modules: list[Module] = field(default_factory=list)
    resources: list[Resource] = field(default_factory=list)
    id: UUID = field(default_factory=new_id, init=False)
    created_at: datetime = field(default_factory=utc_now, init=False)
    updated_at: datetime = field(default_factory=utc_now, init=False)

    def __post_init__(self) -> None:
        self.name = require_text(self.name, "Workspace name")
        self.workspace_type = require_text(self.workspace_type, "Workspace type")

    def add_module(self, module: Module) -> None:
        """Attach an engineering capability to this workflow."""
        if self.get_module(module.id) is not None:
            raise ValueError(f"Module '{module.name}' is already in workspace '{self.name}'")
        self.modules.append(module)
        self._touch()

    def remove_module(self, module_id: UUID) -> Module:
        """Remove and return a module by identity."""
        module = self.get_module(module_id)
        if module is None:
            raise KeyError(f"No module with id '{module_id}' exists in workspace '{self.name}'")
        self.modules.remove(module)
        self._touch()
        return module

    def get_module(self, module_id: UUID) -> Module | None:
        """Return a module by identity when it belongs to this workspace."""
        return next((module for module in self.modules if module.id == module_id), None)

    def add_resource(self, resource: Resource) -> None:
        """Attach supporting engineering evidence to this workflow."""
        if self.get_resource(resource.id) is not None:
            raise ValueError(f"Resource '{resource.name}' is already in workspace '{self.name}'")
        self.resources.append(resource)
        self._touch()

    def remove_resource(self, resource_id: UUID) -> Resource:
        """Remove and return a resource by identity."""
        resource = self.get_resource(resource_id)
        if resource is None:
            raise KeyError(
                f"No resource with id '{resource_id}' exists in workspace '{self.name}'"
            )
        self.resources.remove(resource)
        self._touch()
        return resource

    def get_resource(self, resource_id: UUID) -> Resource | None:
        """Return a resource by identity when it belongs to this workspace."""
        return next((resource for resource in self.resources if resource.id == resource_id), None)

    def _touch(self) -> None:
        self.updated_at = utc_now()
