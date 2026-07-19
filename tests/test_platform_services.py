"""Behaviour tests for the in-memory platform service layer."""

import unittest

from engineering_workbench import Module, Tool
from engineering_workbench.services import (
    KnowledgeService,
    ProjectService,
    ResourceService,
    SearchService,
    WorkspaceService,
)


class PlatformServicesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.projects = ProjectService()
        self.workspaces = WorkspaceService(self.projects)
        self.resources = ResourceService(self.workspaces)
        self.knowledge = KnowledgeService()
        self.search = SearchService(
            self.projects, self.workspaces, self.resources, self.knowledge
        )

    def test_services_create_an_attached_engineering_workflow(self) -> None:
        project = self.projects.create("Packaging Cell Improvement")
        workspace = self.workspaces.create(
            "Current-State Analysis",
            "industrial-engineering",
            project_id=project.id,
        )
        resource = self.resources.create(
            "Cycle time observations",
            "spreadsheet",
            workspace_id=workspace.id,
        )

        self.assertEqual(project.list_workspaces(), (workspace,))
        self.assertIs(workspace.get_resource(resource.id), resource)
        self.assertIs(self.projects.get(project.id), project)

    def test_workspace_service_supports_standalone_work(self) -> None:
        workspace = self.workspaces.create("Quick Cost Check", "cost-analysis")

        self.assertEqual(self.workspaces.list(), (workspace,))
        self.assertEqual(self.projects.list(), ())

    def test_search_discovers_platform_information_across_entity_types(self) -> None:
        project = self.projects.create("Manufacturing Improvement")
        workspace = self.workspaces.create(
            "Cycle Time Study", "industrial-engineering", project_id=project.id
        )
        module = Module("Cycle Time", "Analyse manufacturing cycle time.")
        module.add_tool(Tool("Observation Log", "Capture manufacturing observations."))
        workspace.add_module(module)
        self.resources.create(
            "Manufacturing process map", "drawing", workspace_id=workspace.id
        )
        self.knowledge.create(
            "Manufacturing takt time",
            "Available production time divided by demand.",
            "formula",
        )

        results = self.search.search("manufacturing")

        self.assertEqual(
            {result.entity_type for result in results},
            {"project", "module", "tool", "resource", "knowledge"},
        )

    def test_invalid_parent_does_not_register_an_orphan_workspace(self) -> None:
        with self.assertRaises(KeyError):
            self.workspaces.create(
                "Unattached", "industrial-engineering", project_id=__import__("uuid").uuid4()
            )

        self.assertEqual(self.workspaces.list(), ())

    def test_search_rejects_blank_queries(self) -> None:
        with self.assertRaises(ValueError):
            self.search.search("  ")
