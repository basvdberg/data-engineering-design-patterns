# Data Engineering Design Patterns

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Disclaimer](#disclaimer)
<!-- markdown-toc:end -->

## Purpose 

Design patterns describe functionality in a descriptive, technology-agnostic way. The main reasons for doing this are:

- It gives you a vocabulary to discuss frameworks, tools, platforms and data solutions. Using this you can compare them.
- You can design a technology-agnostic data solution, making it more robust to technology changes.
- It can be used as a blueprint for AI generation of the underlying code in any desired language or tool. You can select the patterns that you need for your data solution.

## Disclaimer

Defining and documenting design patterns is inherently complex. Patterns evolve as practices, tools, and teams change; no catalog is ever finished on the first pass. Treat the content in this repository as a living reference: expect ongoing refactoring, clarification, and improvement rather than a fixed specification. Contributions, corrections, and sharper wording are welcome.

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](readme.md)
  - Definitions
    - [Business intelligence](definitions/business-intelligence.md)
    - [Data engineering](definitions/data-engineering.md)
  - Design patterns
    - [Data solution](design-patterns/data-solution.md)
    - [Event-based orchestration](design-patterns/event-based-orchestration.md)
    - [Historic bitemporal table](design-patterns/historic-bitemporal-table.md)
    - [Data object property tree](design-patterns/object-property-tree.md)
    - [Separate what and how](design-patterns/separate-what-and-how.md)
  - Implementation
    - Event Based Orchestration
      - [Event-based orchestration architecture](implementation/event-based-orchestration/architecture.md)
      - [Azure event-based orchestration architecture](implementation/event-based-orchestration/azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](implementation/event-based-orchestration/tool-choice.md)
<!-- markdown-project-structure:end -->
