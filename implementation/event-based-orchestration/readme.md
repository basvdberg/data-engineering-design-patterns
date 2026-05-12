# Event-based orchestration implementation

## Table of contents

<!-- toc:start -->
- [Purpose](#purpose)
- [Documents](#documents)
<!-- toc:end -->

## Purpose

This folder contains implementation guidance for the [event-based-orchestration](../../design-patterns/event-based-orchestration.md) design pattern. Where the design pattern describes the concepts in a technology-agnostic way, the documents here provide concrete architectural decisions, technology choices, and platform-specific reference architectures.

## Documents

| Document | Description |
| --- | --- |
| [Tool choice](tool-choice.md) | Compares orchestration tools across eight capability areas and provides a scored matrix to guide tool selection. Covers managed platforms, open-source options, and a self-built approach with a recommended Python stack. |
| [Architecture](architecture.md) | Defines a platform-independent reference architecture for event-based orchestration, including core components (event bus, rules engine, execution queue, workers), event contracts, reliability patterns, and a phased rollout plan. |
| [Azure architecture](azure-architecture.md) | Maps the reference architecture to a concrete Azure stack using Event Hubs, Service Bus, Airflow on AKS, Databricks, and PostgreSQL. Includes network and security baseline, deployment model, and an implementation backlog. |

## Project table of contents

<!-- project-toc:start -->
- [Data Engineering Design Patterns](../../readme.md)
  - Definitions
    - [Business intelligence](../../definitions/business-intelligence.md)
    - [Data engineering](../../definitions/data-engineering.md)
  - Design patterns
    - [Data solution](../../design-patterns/data-solution.md)
    - [Event-based orchestration](../../design-patterns/event-based-orchestration.md)
    - [Historic bitemporal table](../../design-patterns/historic-bitemporal-table.md)
    - [Data object property tree](../../design-patterns/object-property-tree.md)
  - Implementation
    - Event based orchestration
      - [Event-based orchestration architecture](architecture.md)
      - [Azure event-based orchestration architecture](azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](tool-choice.md)
    - Full data solution
      - [Phase one: CBS OData extraction with event-based orchestration](../full-data-solution/plan1.md)
      - [Phase two: minimal Dutch government OData ingestion with event-based orchestration](../full-data-solution/plan2.md)
      - [Phase three: JSON-configured Dutch government OData ingestion](../full-data-solution/plan3.md)
<!-- project-toc:end -->
