# Information Architecture

## Purpose

Engineering Workbench is designed around engineering workflows rather than isolated tools. This document defines how information is organised throughout the platform to ensure consistency, traceability, and an intuitive user experience.

The goal is to ensure that information has a clear home, a clear purpose, and a single source of truth.

---

# Core Entities

Engineering Workbench is built around three primary entities:

## Projects

Projects represent persistent engineering efforts.

A project stores:
- Workspaces
- Notes
- Files
- Reports
- Engineering decisions
- Images
- References
- Calculations
- Supporting documentation

Projects provide the long-term context for engineering work.

---

## Workspaces

Workspaces represent engineering activities.

A workspace guides an engineer through a complete workflow rather than presenting isolated calculators.

Examples include:
- Reverse Engineering
- Product Development
- Manufacturing
- Quality
- Process Improvement

Each workspace contains one or more engineering modules that support the workflow.

A workspace may be:

- Attached to a project
- Used independently for quick calculations or investigations

---

## Knowledge

Knowledge represents reusable engineering information that exists independently of projects.

Examples include:
- Material databases
- Engineering standards
- Formula libraries
- Templates
- Preferred suppliers
- Personal engineering references

Knowledge is available across all projects and workspaces.

---

# Relationships

Engineering Workbench follows the hierarchy:

Engineering Workbench

→ Projects
→ Workspaces
→ Modules

Projects provide context.

Workspaces provide workflow.

Modules provide capability.

Knowledge supports all three.

---

# Information Flow

A typical workflow is:

Home
↓

Open Project
or
Create Workspace
↓

Complete Engineering Workflow
↓

Generate Results
↓

Save to Project
or
Store as Knowledge
or
Discard

---

# Design Principles

The information architecture follows these principles:
- Understanding before calculation.
- Information has a single source of truth.
- Every calculation belongs to a workflow.
- Projects preserve engineering context.
- Knowledge is reusable.
- Workspaces reduce engineering friction.
- Modules support workflows rather than replace them.

---

# Home Workspace

The home screen should feel like an engineer's workspace rather than a traditional software dashboard.

It should provide immediate access to:
- Recent projects
- Continue working
- Start a new workspace
- Templates
- Knowledge resources
- Recent reports
- Saved references

The emphasis is on continuing engineering work rather than navigating software.
