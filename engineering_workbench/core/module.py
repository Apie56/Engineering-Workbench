"""Module domain object."""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from engineering_workbench.core._common import new_id, require_text
from engineering_workbench.core.tool import Tool


@dataclass(slots=True)
class Module:
    """A reusable collection of related engineering tools."""

    name: str
    description: str
    version: str = "0.1.0"
    tools: list[Tool] = field(default_factory=list)
    id: UUID = field(default_factory=new_id, init=False)

    def __post_init__(self) -> None:
        self.name = require_text(self.name, "Module name")
        self.description = require_text(self.description, "Module description")
        self.version = require_text(self.version, "Module version")

    def add_tool(self, tool: Tool) -> None:
        """Add a focused capability to this module exactly once."""
        if self.get_tool(tool.id) is not None:
            raise ValueError(f"Tool '{tool.name}' is already in module '{self.name}'")
        self.tools.append(tool)

    def remove_tool(self, tool_id: UUID) -> Tool:
        """Remove and return a tool by identity."""
        tool = self.get_tool(tool_id)
        if tool is None:
            raise KeyError(f"No tool with id '{tool_id}' exists in module '{self.name}'")
        self.tools.remove(tool)
        return tool

    def get_tool(self, tool_id: UUID) -> Tool | None:
        """Return a tool by identity when it belongs to this module."""
        return next((tool for tool in self.tools if tool.id == tool_id), None)
