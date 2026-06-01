# Data solution

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Components](#components)
- [Requirements](#requirements)
  - [Lineage](#lineage)
  - [Auditability](#auditability)
  - [Self service environment](#self-service-environment)
<!-- markdown-toc:end -->

## Purpose

A data solution is a very generic high level concept that defines the total architecture that allows you to turn raw data into valuable insights. 

## Components

- Data logistics: the transport of data from source systems into a consolidated location where it can be used for analytics and reporting.
- Data modelling: transforming the structure of data, or in other words the data schema.
- Data cleaning and enriching: transforming data so that data quality improves.
- Data provisioning: making data available for consumption by end users.

Layering is specified in [Data solution layer](data-solution-layer.md): staging, raw, integrated, and presentation.

## Requirements

A data element is the smallest part of a data object. E.g. a column value of a specific row in a table. 

### Lineage
It should be possible to show how every data element is constructed, by showing all transformations and logistic processes that are applied on top of the raw source data. 

### Auditability
Every read and write of a data element should be logged together with the related user, process and timestamp, so that it's purpose and authority can be verified. 

### Self service environment

**Synonym:** Sandbox environment
An environment that is less strict and hereby allows you to quickly load and use data. This can be used for ad hoc analysis of a new dataset or for research and development. Because of the lower requirements, this environment cannot be used for non R&D use cases.

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](../../readme.md)
  - Definitions
    - [Business intelligence](../../definitions/business-intelligence.md)
    - [Data engineering](../../definitions/data-engineering.md)
  - Design patterns
    - Data engineering
      - [Data extractor](data-extractor.md)
      - [Data object container](data-object-container.md)
      - [Data object poller](data-object-poller.md)
      - [Data object tree property inheritance](data-object-tree-property-inheritance.md)
      - [Data object tree](data-object-tree.md)
      - [Data object](data-object.md)
      - [Data solution layer](data-solution-layer.md)
      - [Data solution](data-solution.md)
      - [Event-based orchestration](event-based-orchestration.md)
      - [Historic bitemporal table](historic-bitemporal-table.md)
    - Generic
      - [Functional decomposition](../generic/functional-decomposition.md)
      - [Prefer simple decomposition](../generic/prefer-simple-decomposition.md)
      - [Separate what and how](../generic/separate-what-and-how.md)
      - [Simplicity](../generic/simplicity.md)
  - Implementation
    - Event Based Orchestration
      - [Event-based orchestration architecture](../../implementation/event-based-orchestration/architecture.md)
      - [Azure event-based orchestration architecture](../../implementation/event-based-orchestration/azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](../../implementation/event-based-orchestration/tool-choice.md)
- Related repositories
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026) — Course and learning materials
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026) — Data solution proof of concept
<!-- markdown-project-structure:end -->
