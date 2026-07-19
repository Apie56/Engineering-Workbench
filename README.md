# Engineering Workbench

> A unified engineering workspace for calculations, project context, technical references, and decision support.

Engineering Workbench is an open-source platform designed around engineering workflows rather than disconnected calculators. Its first implementation milestone is the **Engineering Kernel**: a small, explicit domain model that represents projects, workspaces, modules, tools, resources, and knowledge.

## Current status

Pre-alpha. The project is establishing its domain model; persistence, calculations, and the user interface are intentionally out of scope for this first sprint.

## Engineering Kernel

The kernel follows the architecture described in the project documentation:

```text
Project → Workspace → Module → Tool
                       └──────→ Resource

Knowledge supports projects and workspaces across the platform.
```

- A **Project** preserves a persistent engineering context.
- A **Workspace** coordinates a particular engineering workflow.
- A **Module** groups related engineering functionality.
- A **Tool** is the smallest meaningful unit of engineering functionality.
- A **Resource** is supporting evidence such as a note, drawing, PDF, image, or datasheet.
- **Knowledge** is reusable information that exists independently of a project.

## Development

Requires Python 3.11 or newer.

```powershell
python -m unittest discover -s tests -v
```

## Git workflow

The repository uses the following branch model once Git is initialized locally:

```text
main                 Stable, releasable work
└── develop          Integration branch
    └── feature/*    Focused feature branches
```

The foundation work belongs on `feature/engineering-kernel`, which should merge into `develop` through a pull request. Use Conventional Commits, for example:

```text
feat: initialize Engineering Kernel domain model
```
