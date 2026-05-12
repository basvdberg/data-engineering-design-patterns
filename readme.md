# Data Engineering Design Patterns

Design patterns describe functionality in a descriptive, technology-agnostic way. The main reasons for doing this are:

- It gives you a vocabulary to discuss frameworks, tools, platforms and data solutions. Using this you can compare them.
- You can design a technology-agnostic data solution, making it more robuust to technology changes.
- It can be used as a blueprint for AI generation of the underlying code in any desired language or tool. You can select the patterns that you need for your data solution.

## Project table of contents

<!-- project-toc:start -->
- [Data Engineering Design Patterns](readme.md)
  - Definitions
    - [Business intelligence](definitions/business-intelligence.md)
    - [Data engineering](definitions/data-engineering.md)
  - Design patterns
    - [Data solution](design-patterns/data-solution.md)
    - [Event-based orchestration](design-patterns/event-based-orchestration.md)
    - [Historic bitemporal table](design-patterns/historic-bitemporal-table.md)
    - [Data object property tree](design-patterns/object-property-tree.md)
  - Implementation
    - Event based orchestration
      - [Event-based orchestration architecture](implementation/event-based-orchestration/architecture.md)
      - [Azure event-based orchestration architecture](implementation/event-based-orchestration/azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](implementation/event-based-orchestration/tool-choice.md)
    - Full data solution
      - [Phase one: CBS OData extraction with event-based orchestration](implementation/full-data-solution/plan1.md)
      - [Phase two: minimal Dutch government OData ingestion with event-based orchestration](implementation/full-data-solution/plan2.md)
      - [Phase three: JSON-configured Dutch government OData ingestion](implementation/full-data-solution/plan3.md)
<!-- project-toc:end -->
