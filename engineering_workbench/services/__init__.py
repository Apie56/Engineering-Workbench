"""Platform services for coordinating Engineering Kernel domain objects."""

from engineering_workbench.services.knowledge_service import KnowledgeService
from engineering_workbench.services.project_service import ProjectService
from engineering_workbench.services.resource_service import ResourceService
from engineering_workbench.services.search_service import SearchResult, SearchService
from engineering_workbench.services.workspace_service import WorkspaceService

__all__ = [
    "KnowledgeService",
    "ProjectService",
    "ResourceService",
    "SearchResult",
    "SearchService",
    "WorkspaceService",
]
