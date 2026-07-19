"""Knowledge domain object."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from engineering_workbench.core._common import Metadata, new_id, require_text, utc_now


@dataclass(slots=True)
class Knowledge:
    """Reusable engineering information independent of a project."""

    title: str
    content: str
    knowledge_type: str
    source: str | None = None
    metadata: Metadata = field(default_factory=dict)
    id: UUID = field(default_factory=new_id, init=False)
    created_at: datetime = field(default_factory=utc_now, init=False)

    def __post_init__(self) -> None:
        self.title = require_text(self.title, "Knowledge title")
        self.content = require_text(self.content, "Knowledge content")
        self.knowledge_type = require_text(self.knowledge_type, "Knowledge type")
