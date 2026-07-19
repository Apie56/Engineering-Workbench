"""Shared primitives for Engineering Kernel domain objects."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4


def new_id() -> UUID:
    """Return a globally unique identity for a domain object."""
    return uuid4()


def utc_now() -> datetime:
    """Return a timezone-aware timestamp for domain history."""
    return datetime.now(UTC)


def require_text(value: str, field_name: str) -> str:
    """Validate a human-facing required text value."""
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be blank")
    return normalized


Metadata = Mapping[str, Any]
