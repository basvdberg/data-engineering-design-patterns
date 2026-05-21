# Event-based orchestration implementation

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Documents](#documents)
<!-- markdown-toc:end -->

## Purpose

This folder contains implementation guidance for the [event-based-orchestration](../../design-patterns/event-based-orchestration.md) design pattern. Where the design pattern describes the concepts in a technology-agnostic way, the documents here provide concrete architectural decisions, technology choices, and platform-specific reference architectures.

## Documents

| Document | Description |
| --- | --- |
| [Tool choice](tool-choice.md) | Compares orchestration tools across eight capability areas and provides a scored matrix to guide tool selection. Covers managed platforms, open-source options, and a self-built approach with a recommended Python stack. |
| [Architecture](architecture.md) | Defines a platform-independent reference architecture for event-based orchestration, including core components (event bus, rules engine, execution queue, workers), event contracts, reliability patterns, and a phased rollout plan. |
| [Azure architecture](azure-architecture.md) | Maps the reference architecture to a concrete Azure stack using Event Hubs, Service Bus, Airflow on AKS, Databricks, and PostgreSQL. Includes network and security baseline, deployment model, and an implementation backlog. |

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](../../readme.md)
  - Definitions
    - [Business intelligence](../../definitions/business-intelligence.md)
    - [Data engineering](../../definitions/data-engineering.md)
  - Design patterns
    - [Data solution](../../design-patterns/data-solution.md)
    - [Event-based orchestration](../../design-patterns/event-based-orchestration.md)
    - [Historic bitemporal table](../../design-patterns/historic-bitemporal-table.md)
    - [Data object property tree](../../design-patterns/object-property-tree.md)
    - [Separate what and how](../../design-patterns/separate-what-and-how.md)
  - Implementation
    - Event Based Orchestration
      - [Event-based orchestration architecture](architecture.md)
      - [Azure event-based orchestration architecture](azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](tool-choice.md)
- Related repositories
  - [cursor-config](https://github.com/basvdberg/cursor-config)
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026)
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026)
<!-- markdown-project-structure:end -->
