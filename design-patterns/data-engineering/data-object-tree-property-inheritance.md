# Data object tree property inheritance

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Prop](#prop)
  - [ObjProp](#objprop)
  - [Property resolution](#property-resolution)
- [Rules](#rules)
  - [Child overrides parent](#child-overrides-parent)
  - [Fallback to parent](#fallback-to-parent)
<!-- markdown-toc:end -->

## Purpose

Data engineering needs flexible properties on data objects in a [data object tree](data-object-tree.md), with values inherited by descendants. A source-system name can apply to every table and schema in a database; an `include for ingestion` flag can cover every file in a folder except named exceptions.

## Benefits

- Non-redundant property assignment — no copy-pasting values onto every descendant.
- Generic rules at a parent scope with optional overrides on children.
- New objects under an existing parent pick up applicable properties automatically.
- Boolean include flags scope transformation without repeating full paths in configuration.

## Summary

Properties attach to objects in the tree and flow to descendants. Direct assignments and inherited values combine at runtime; a child may override a parent value for the same property key.

## Components

### Prop

The `Prop` entity defines properties that can be assigned to data objects.

Examples:
- Retention period in days.
- Required freshness SLA.
- Allowed load mode (`full`, `incremental`).
- Included in ingestion (yes/no).

### ObjProp

The `ObjProp` entity links a property to an object, including value and validity metadata. Values inherit from parent objects unless overridden on the child.

Examples:
- A domain-level retention rule inherited by all child objects.
- A table-level override for load mode because of source-system limitations.

### Property resolution

Effective properties are calculated at runtime from inherited and directly assigned `ObjProp` entries.

## Rules

### Child overrides parent

A property set on a child replaces the inherited parent value for the same key.

### Fallback to parent

When a property is missing on a child, resolution walks up the [data object tree](data-object-tree.md) until a value is found or the root is reached.

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
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026)
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026)
<!-- markdown-project-structure:end -->
