"""Resource domain object."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from engineering_workbench.core._common import Metadata, new_id, require_text, utc_now


@dataclass(slots=True)
class Resource:
    """Supporting evidence used or produced during engineering work."""

    name: str
    resource_type: str
    location: str | None = None
    metadata: Metadata = field(default_factory=dict)
    id: UUID = field(default_factory=new_id, init=False)
    created_at: datetime = field(default_factory=utc_now, init=False)

    def __post_init__(self) -> None:
        self.name = require_text(self.name, "Resource name")
        self.resource_type = require_text(self.resource_type, "Resource type")
