# Engineering Workbench

> **A unified engineering workspace for calculations, project management, technical references, and engineering decision support.**

Engineering Workbench is an open-source platform that brings together the tools engineers use every day into a single, interactive workspace.

Modern engineering workflows are often fragmented across spreadsheets, PDFs, browser-based calculators, notebooks, CAD software, and numerous standalone applications. Engineering Workbench aims to eliminate this fragmentation by providing a modular platform where engineering knowledge, calculations, project information, and technical workflows are connected.

Rather than replacing engineering judgement, Engineering Workbench empowers engineers by reducing context switching, improving traceability, and making engineering knowledge more accessible, reusable, and interactive.

---

## Vision

To become the open-source standard for practical engineering workflows.

---

## Mission

Engineering Workbench exists to provide engineers with a modern, modular platform that consolidates engineering calculations, project information, manufacturing tools, technical references, and engineering workflows into one cohesive environment.

---

## Who It's For

Engineering Workbench is designed around the interdisciplinary workflow of Industrial Engineers while supporting professionals across multiple engineering disciplines, including:

* Industrial Engineering
* Mechanical Engineering
* Manufacturing Engineering
* Quality Engineering
* Product Design
* Engineering Students
* Engineering Consultants
* Freelancers
* Makers

---

## Core Principles

* **Unified** – One workspace for engineering.
* **Practical** – Every feature solves a real engineering problem.
* **Interactive** – Engineering knowledge should be usable, not static.
* **Transparent** – Calculations should clearly show assumptions, inputs, and outputs.
* **Extensible** – New modules and disciplines should integrate seamlessly.
* **Open** – Community-driven and open source.
* **Professional** – Built to industry standards.

---

## Planned Features

### Core Platform

* Project management
* Engineering notebook
* Universal search
* Report generation
* User settings
* Module browser

### Mechanical Engineering

* ISO fits and tolerances
* Thread calculator
* Fastener torque
* Bearing selection
* GD&T tools
* Material selection

### Manufacturing

* Manufacturing costing
* Bill of Materials (BOM)
* Cycle time estimation
* Additive manufacturing tools
* Machining calculators
* Process planning

### Industrial Engineering

* Overall Equipment Effectiveness (OEE)
* Statistical Process Control (SPC)
* Process capability
* EOQ analysis
* ABC inventory analysis
* Line balancing
* Takt time

### Quality

* Pareto analysis
* Fishbone diagrams
* Gauge R&R
* Control charts
* Root cause analysis

### Utilities

* Unit conversion
* Engineering constants
* Scientific calculator
* Equation solver
* Material database

---

## Guiding Philosophy

Engineering Workbench is designed around engineering workflows—not disconnected calculators.

Every calculation should:

* Belong to a project
* Be automatically saved
* Be reproducible
* Be traceable
* Be reusable

The goal is to reduce friction throughout the engineering process by keeping information connected and accessible.

---

## Technology Stack

| Layer              | Technology                                |
| ------------------ | ----------------------------------------- |
| Frontend           | React, TypeScript, Vite                   |
| Backend            | Python, FastAPI                           |
| Engineering Engine | NumPy, SciPy, SymPy, Pandas               |
| Database           | SQLite (development), PostgreSQL (future) |
| Visualisation      | Plotly                                    |
| Reports            | TBD                                       |
| Version Control    | Git & GitHub                              |

> **Note:** The technology stack may evolve as the project matures. The platform architecture is intentionally designed to remain modular and adaptable.

---

## Development Status

Engineering Workbench is currently in the planning and architecture phase.

The project is being developed using a documentation-first approach, where product vision, requirements, architecture, and engineering standards are defined before implementation begins.

---

## Roadmap

* ✅ Define project vision
* 🚧 Product requirements
* ⏳ System architecture
* ⏳ Module specification
* ⏳ Design system
* ⏳ Core platform
* ⏳ Engineering modules
* ⏳ Public alpha release

For a more detailed roadmap, see `docs/development-roadmap.md`.

---

## Contributing

Engineering Workbench is being developed as an open-source project with a strong emphasis on software quality, engineering accuracy, and maintainability.

Contribution guidelines will be published as the project matures.

---

## Development Status

Engineering Workbench is now in the first Engineering Kernel sprint. The initial Python domain model represents Projects, Workspaces, Modules, Tools, Resources, and reusable Knowledge. Persistence, calculations, and the user interface intentionally follow in later milestones.

### Run the tests

Python 3.11 or newer is required.

```powershell
python -m unittest discover -s tests -v
```

---

## License

This project will be released under an open-source license. The specific license will be selected during the early stages of development.

---

## Founder's Note

_Engineering Workbench began with a simple observation: solving one engineering problem often required opening numerous applications, spreadsheets, standards, PDFs, and browser tabs before arriving at a single answer._

_We believe engineering deserves a better workspace._

_This project is our attempt to build it—not as a replacement for engineering expertise, but as a platform that allows engineers to focus on what they do best: solving problems._
