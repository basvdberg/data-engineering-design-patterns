# Data object tree

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Data object (Obj)](#data-object-obj)
  - [TableSchema](#tableschema)
  - [Object discovery](#object-discovery)
  - [Table schema discovery](#table-schema-discovery)
<!-- markdown-toc:end -->

## Purpose

Data objects have a hierarchical structure. A table lives inside a schema, a schema inside a database on a server; a CSV file inside a folder inside a storage container. The data object tree registers each object and its parent-child relation so datasets can be represented from broad domains down to concrete tables, files, or views.

Property assignment and inheritance on nodes in this tree are defined by [data object tree property inheritance](data-object-tree-property-inheritance.md).

## Benefits

- Single registry for all objects and containers in a solution.
- Parent-child links support discovery and cataloging without duplicating paths.
- New objects under an existing parent are registered when discovery runs.

## Summary

Objects form a tree rooted at the solution. Each `Obj` records identity and parent-child links; table-shaped leaves may carry `TableSchema` metadata discovered from the source.

## Components

### Data object (Obj)

The `Obj` entity is the registry of data objects and containers involved in data processing. It stores each object and its parent-child relation.

Examples:
- A root object `sales`.
- A child object `sales.raw`.
- A leaf object `sales.raw.orders_csv`.

### TableSchema

When the object is a table in a database or file, the `TableSchema` entity stores structural metadata: columns and data types, primary and foreign keys, nullability, defaults, and partitioning or indexing metadata.

### Object discovery

Object discovery enumerates all objects for a given parent — for example, schemas, tables, and views under a database server, or files and folders under a storage path.

### Table schema discovery

Table schema discovery extracts structural metadata from a relational table or file-backed table object.

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](../../readme.md)
  - Definitions
    - [Business intelligence](../../definitions/business-intelligence.md)
    - [Data engineering](../../definitions/data-engineering.md)
    - [Data](../../definitions/data.md)
  - Design patterns
    - Data engineering
      - [Data extractor](data-extractor.md)
      - [Data object container](data-object-container.md)
      - [Data object contract](data-object-contract.md)
      - [Data object poller](data-object-poller.md)
      - [Data object quality of service](data-object-quality-of-service.md)
      - [Data object quality](data-object-quality.md)
      - [Data object refresh contract](data-object-refresh-contract.md)
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
    - Data Object Refresh Contract
      - [Data object refresh contract alternatives](../../implementation/data-object-refresh-contract/alternatives.md)
    - Event Based Orchestration
      - [Event-based orchestration architecture](../../implementation/event-based-orchestration/architecture.md)
      - [Azure event-based orchestration architecture](../../implementation/event-based-orchestration/azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](../../implementation/event-based-orchestration/tool-choice.md)
- Related repositories
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026) — Course and learning materials
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026) — Data solution proof of concept
<!-- markdown-project-structure:end -->
