"""Tool domain object."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import UUID

from engineering_workbench.core._common import Metadata, new_id, require_text


@dataclass(slots=True)
class Tool:
    """A focused engineering task, such as a calculation or lookup."""

    name: str
    description: str
    inputs: Metadata = field(default_factory=dict)
    outputs: Metadata = field(default_factory=dict)
    id: UUID = field(default_factory=new_id, init=False)

    def __post_init__(self) -> None:
        self.name = require_text(self.name, "Tool name")
        self.description = require_text(self.description, "Tool description")

    def validate(self, values: Metadata) -> None:
        """Validate values before a concrete tool performs engineering work.

        Concrete tools will extend this method with their domain constraints.
        """
        if not isinstance(values, dict):
            raise TypeError("Tool inputs must be provided as a dictionary")

    def run(self, values: Metadata) -> dict[str, Any]:
        """Run the tool after validation.

        The kernel intentionally defines no engineering calculations. A concrete
        tool supplies calculation or lookup behaviour in a future sprint.
        """
        self.validate(values)
        raise NotImplementedError("Concrete tools must implement run()")
