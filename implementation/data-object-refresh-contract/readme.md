# Data object refresh contract implementation

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Documents](#documents)
<!-- markdown-toc:end -->

## Purpose

This folder contains implementation guidance for the [data object refresh contract](../../design-patterns/data-engineering/data-object-refresh-contract.md) design pattern. Where the design pattern states functional requirements and use cases in a technology-agnostic way, the documents here compare industry standards and toolchains for implementing refresh contracts.

## Documents

| Document | Description |
| --- | --- |
| [Alternatives](alternatives.md) | Compares ODCS, dbt freshness, and catalog assertion contracts against the refresh contract pattern. Includes a side-by-side summary and practical combination recommendations. |

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](../../readme.md)
  - Definitions
    - [Business intelligence](../../definitions/business-intelligence.md)
    - [Data engineering](../../definitions/data-engineering.md)
    - [Data](../../definitions/data.md)
  - Design patterns
    - Data engineering
      - [Data extractor](../../design-patterns/data-engineering/data-extractor.md)
      - [Data object container](../../design-patterns/data-engineering/data-object-container.md)
      - [Data object contract](../../design-patterns/data-engineering/data-object-contract.md)
      - [Data object poller](../../design-patterns/data-engineering/data-object-poller.md)
      - [Data object quality of service](../../design-patterns/data-engineering/data-object-quality-of-service.md)
      - [Data object quality](../../design-patterns/data-engineering/data-object-quality.md)
      - [Data object refresh contract](../../design-patterns/data-engineering/data-object-refresh-contract.md)
      - [Data object tree property inheritance](../../design-patterns/data-engineering/data-object-tree-property-inheritance.md)
      - [Data object tree](../../design-patterns/data-engineering/data-object-tree.md)
      - [Data object](../../design-patterns/data-engineering/data-object.md)
      - [Data solution layer](../../design-patterns/data-engineering/data-solution-layer.md)
      - [Data solution](../../design-patterns/data-engineering/data-solution.md)
      - [Event-based orchestration](../../design-patterns/data-engineering/event-based-orchestration.md)
      - [Historic bitemporal table](../../design-patterns/data-engineering/historic-bitemporal-table.md)
    - Generic
      - [Functional decomposition](../../design-patterns/generic/functional-decomposition.md)
      - [Prefer simple decomposition](../../design-patterns/generic/prefer-simple-decomposition.md)
      - [Separate what and how](../../design-patterns/generic/separate-what-and-how.md)
      - [Simplicity](../../design-patterns/generic/simplicity.md)
  - Implementation
    - Data Object Refresh Contract
      - [Data object refresh contract alternatives](alternatives.md)
    - Event Based Orchestration
      - [Event-based orchestration architecture](../event-based-orchestration/architecture.md)
      - [Azure event-based orchestration architecture](../event-based-orchestration/azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](../event-based-orchestration/tool-choice.md)
- Related repositories
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026) — Course and learning materials
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026) — Data solution proof of concept
<!-- markdown-project-structure:end -->
