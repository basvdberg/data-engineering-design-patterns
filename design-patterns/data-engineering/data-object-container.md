# Data object container

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Components](#components)
  - [Identity](#identity)
  - [Container type](#container-type)
  - [Hierarchy](#hierarchy)
  - [Container scope](#container-scope)
  - [Discovery](#discovery)
- [Rules](#rules)
  - [Single parent](#single-parent)
  - [Scope is inherited](#scope-is-inherited)
  - [Containers group, they do not carry payload](#containers-group-they-do-not-carry-payload)
  - [Key reflects position](#key-reflects-position)
<!-- markdown-toc:end -->

## Purpose

A data object container groups [data objects](data-object.md) and other containers in a hierarchy. A container represents the physical or logical scope that data objects live in — a server, database, schema, folder, storage account, source system, domain, or solution layer.

Containers let scope be set once and inherited. Without containers, every data object repeats its source system, connection, owner, retention, and classifications on its own. With containers, those facts attach to the smallest enclosing scope and reach all descendants.

The hierarchy and the inheritance mechanism are defined by the [data object property tree](object-property-tree.md). This pattern focuses on the container node itself.

## Components

### Identity

A `DataObjectContainer` has a unique `Key` that names it within the hierarchy. The key matches the container's position in the tree (a path or a dotted namespace).

Examples:
- `staging` (a solution-layer container).
- `staging/inventory` (a source-system container under a layer).

### Container type

The `ContainerType` declares the kind of grouping the container represents. Type drives which properties make sense to attach.

Examples:
- Storage scope: server, database, schema, storage account.
- Filesystem scope: folder, file system.
- Namespace scope: domain, source system, solution layer.

### Hierarchy

A container has at most one `Parent` and any number of `Children`. Children are other containers or `DataObject` leaves. The full tree is rooted at the solution.

Examples:
- `staging` → `staging/inventory` → `staging/inventory/daily-stock`.
- `domain/sales` → `domain/sales/orders`.

### Container scope

The `ContainerScope` is the set of properties and references the container carries on behalf of its children: a default `DataConnection`, owner, classifications, retention, or load mode. Children inherit the scope and may override individual entries.

Examples:
- A storage container declares the database connection used by all its tables.
- A source-system container declares the source classification applied to every object below.

### Discovery

The `ContainerDiscovery` process enumerates the immediate children of a container, or the full subtree on demand. Discovery feeds the registry used by orchestration and cataloging.

Examples:
- List all schemas, tables, and views under a database.
- List all files and folders under a storage path.

## Rules

### Single parent

A `DataObjectContainer` has at most one `Parent`. The hierarchy is a tree.

### Scope is inherited

Properties attached to a container reach every descendant by inheritance, following the resolution rules in [data object property tree](object-property-tree.md). Any descendant may override an inherited value.

### Containers group, they do not carry payload

A container is a grouping artefact. Schema, materialization, batch window, and lifecycle belong to the `DataObject` leaves — see [data object](data-object.md).

### Key reflects position

A container's `Key` reflects its position in the tree. Renames and moves update the keys of all descendants; references are updated by explicit mapping.

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
      - [Data object](data-object.md)
      - [Data solution layer](data-solution-layer.md)
      - [Data solution](data-solution.md)
      - [Event-based orchestration](event-based-orchestration.md)
      - [Historic bitemporal table](historic-bitemporal-table.md)
      - [Data object property tree](object-property-tree.md)
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
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026)
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026)
<!-- markdown-project-structure:end -->
