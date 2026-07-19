"""Behaviour tests for the first Engineering Kernel domain model."""

import unittest

from engineering_workbench import Knowledge, Module, Project, Resource, Tool, Workspace


class EngineeringKernelTests(unittest.TestCase):
    def test_project_workspace_module_tool_hierarchy(self) -> None:
        project = Project(name="Packaging Cell Improvement")
        workspace = Workspace("Current-State Investigation", "industrial-engineering")
        module = Module("Cycle Time", "Analyse process cycle times.")
        tool = Tool("Observation Log", "Record observed cycle times.")
        module.add_tool(tool)
        workspace.add_module(module)
        project.add_workspace(workspace)
        self.assertEqual(project.list_workspaces(), (workspace,))
        self.assertIs(workspace.get_module(module.id), module)
        self.assertIs(module.get_tool(tool.id), tool)

    def test_standalone_workspace_and_resources(self) -> None:
        workspace = Workspace("Quick Cost Check", "cost-analysis")
        resource = Resource("Process map", "drawing", "process-map.pdf")
        workspace.add_resource(resource)
        self.assertIs(workspace.get_resource(resource.id), resource)
        self.assertEqual(workspace.remove_resource(resource.id), resource)

    def test_knowledge_is_independent_of_project_context(self) -> None:
        knowledge = Knowledge("Takt time", "Available production time divided by demand.", "formula")
        self.assertEqual(knowledge.knowledge_type, "formula")

    def test_blank_names_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Project(name="   ")

    def test_base_tool_requires_concrete_execution(self) -> None:
        tool = Tool("Future Tool", "A contract for future calculations.")
        with self.assertRaises(NotImplementedError):
            tool.run({})
