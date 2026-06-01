# Data Engineering Design Patterns

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Disclaimer](#disclaimer)
<!-- markdown-toc:end -->

## Purpose

Design patterns describe functionality in a descriptive, technology-agnostic way. They support the way of working in [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026) and are applied in the [data-solution-2026](https://github.com/basvdberg/data-solution-2026) proof of concept.

Patterns are grouped under **Data engineering** (data objects, extractors, layers, temporal storage) and **Generic** (orchestration, decomposition, simplicity, and separating specification from implementation). Generic patterns apply outside data platforms; data-engineering patterns name concepts used in data solutions.

The main reasons to document patterns this way are:

- They can be used as blueprints for AI generation of underlying code in any language or tool. Select the patterns you need for your data solution.
- They provide a vocabulary to discuss frameworks, tools, platforms, and data solutions—and to compare them.
- They help you design a technology-agnostic data solution that is more robust to technology changes.

## Disclaimer

Defining and documenting design patterns is inherently complex. Patterns evolve as practices, tools, and teams change; no catalog is ever finished on the first pass. Treat the content in this repository as a living reference: expect ongoing refactoring, clarification, and improvement rather than a fixed specification. Contributions, corrections, and sharper wording are welcome.

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](readme.md)
  - Definitions
    - [Business intelligence](definitions/business-intelligence.md)
    - [Data engineering](definitions/data-engineering.md)
  - Design patterns
    - Data engineering
      - [Data extractor](design-patterns/data-engineering/data-extractor.md)
      - [Data object container](design-patterns/data-engineering/data-object-container.md)
      - [Data object poller](design-patterns/data-engineering/data-object-poller.md)
      - [Data object tree property inheritance](design-patterns/data-engineering/data-object-tree-property-inheritance.md)
      - [Data object tree](design-patterns/data-engineering/data-object-tree.md)
      - [Data object](design-patterns/data-engineering/data-object.md)
      - [Data solution layer](design-patterns/data-engineering/data-solution-layer.md)
      - [Data solution](design-patterns/data-engineering/data-solution.md)
      - [Event-based orchestration](design-patterns/data-engineering/event-based-orchestration.md)
      - [Historic bitemporal table](design-patterns/data-engineering/historic-bitemporal-table.md)
    - Generic
      - [Functional decomposition](design-patterns/generic/functional-decomposition.md)
      - [Prefer simple decomposition](design-patterns/generic/prefer-simple-decomposition.md)
      - [Separate what and how](design-patterns/generic/separate-what-and-how.md)
      - [Simplicity](design-patterns/generic/simplicity.md)
  - Implementation
    - Event Based Orchestration
      - [Event-based orchestration architecture](implementation/event-based-orchestration/architecture.md)
      - [Azure event-based orchestration architecture](implementation/event-based-orchestration/azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](implementation/event-based-orchestration/tool-choice.md)
- Related repositories
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026) — Course and learning materials
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026) — Data solution proof of concept
<!-- markdown-project-structure:end -->
