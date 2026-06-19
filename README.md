## **Name:** Matthew McGilvery
**Date:** June 18, 2026
**Topic:** Life Systems Architecture

# Life Systems

Life Systems is a general methodology for everyday decision architecture. It helps people diagnose friction, map complexity, choose responses, execute within real limits, and audit whether the original issue was resolved.

It was developed through creative practice, independent work, and personal systems design, but it is not limited to those contexts. The framework can be used for personal decisions, creative projects, academic planning, operations, project management, and any situation where unclear friction needs to become structured action.

## Core Workflow

`Diagnose → Map → Decide → Execute → Audit`

The repository is organized into five linked modules:

### 1. [Problem Diagnosis (`/problem`)](problem/README.md)

Defines friction clearly before trying to solve it.

A problem is treated as a structured relationship between four variables:

`Problem = f(Trigger, Context, Conflict, Impact)`

Use this module to identify the cause, baseline, obstacle, and stakes of a situation.

### 2. [Complexity Mapping (`/cynefin`)](cynefin/README.md)

Maps the situation before choosing a response.

Some situations need best practices. Some need expert analysis. Some need experiments. Some need immediate stabilization. This module helps classify the operating environment so the response matches reality.

### 3. [Decision Analysis (`/decision`)](decision/README.md)

Turns diagnosis into a defended choice.

This module provides a structured document format for comparing alternatives, weighing pros and cons, selecting a path, and explaining why that path is the best available response.

### 4. [Execution Logistics (`/execution`)](execution/README.md)

Translates the chosen path into action within real limits.

This module protects bandwidth by turning implementation steps into scoped tasks with capacity constraints. It prevents overcommitment by treating time, attention, energy, and available resources as finite.

### 5. [System Audit (`/audit`)](audit/README.md)

Checks whether the original issue was resolved.

This module closes the loop by reviewing whether the original trigger was neutralized, what changed in the context, and what new friction appeared during execution.

## What This Repository Is

Life Systems is a documentation-first methodology with optional Python reference models. The Markdown files explain the framework. The Python files demonstrate how parts of the logic can be represented programmatically.

This is not an installable software package. It is a general framework for making everyday decisions more explicit, structured, realistic, and reviewable.

## Who It Is For

Life Systems can be used by:

- Students managing school, work, projects, and personal logistics
- Artists and creative operators managing ideas, releases, constraints, and output
- Independent workers balancing multiple responsibilities
- Project managers and operations thinkers seeking a lightweight decision structure
- Anyone trying to turn recurring friction into a clearer action loop

## Repository Structure

```text
life_systems/
├── README.md
├── methodology.md
├── lean_canvas.md
├── problem/
│   ├── README.md
│   ├── problem_framework.md
│   ├── internal_problem.md
│   └── problem_framework.py
├── cynefin/
│   ├── README.md
│   └── cynefin_framework.py
├── decision/
│   ├── README.md
│   └── decision_framework.py
├── execution/
│   ├── README.md
│   └── execution_framework.py
├── audit/
│   ├── README.md
│   └── audit_framework.py
└── templates/
    ├── problem_template.md
    ├── decision_template.md
    ├── execution_sprint_template.md
    └── audit_template.md
```

## Use Rule

Use the full framework when a problem is recurring, costly, confusing, emotionally loaded, or strategically important.

For small decisions, use only the part of the system that fits the situation.

## References and Influences

Life Systems is an original methodology, but it openly credits external frameworks used as references.

The Complexity Mapping module adapts concepts from the Cynefin framework associated with Dave Snowden, Cognitive Edge, and The Cynefin Company.

The `lean_canvas.md` file uses the Lean Canvas format created by Ash Maurya as a planning structure.

See [references.md](references.md) for attribution details.
