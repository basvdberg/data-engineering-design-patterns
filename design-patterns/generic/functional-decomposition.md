# Functional decomposition

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Functional unit](#functional-unit)
  - [Generic pipeline](#generic-pipeline)
  - [Configuration](#configuration)
  - [Composition](#composition)
  - [Decomposition quality](#decomposition-quality)
- [Rules](#rules)
  - [Decompose by responsibility](#decompose-by-responsibility)
  - [Generalize repeated behavior](#generalize-repeated-behavior)
  - [Express variation in configuration](#express-variation-in-configuration)
  - [Refactor when duplication appears](#refactor-when-duplication-appears)
<!-- markdown-toc:end -->

## Purpose

`FunctionalDecomposition` decomposes a system into focused `FunctionalUnit` parts with clear responsibilities. The pattern improves reuse and reduces repeated implementations.

It is a practical mechanism to realize `Simplicity` in concrete system structures.

## Benefits

- Reduces duplication across similar flows.
- Improves reuse of shared logic.
- Makes behavior changes more consistent.
- Keeps orchestration explicit and understandable.
- Makes scaling across many data objects cheaper.

## Summary

A decomposed design builds a solution from reusable `FunctionalUnit` components, then applies `Configuration` to express variations. Instead of creating a dedicated pipeline for each data object, the pattern prefers one generic pipeline for one kind of data object and executes it with different configurations.

## Components

### Functional unit

A `FunctionalUnit` performs one well-defined responsibility and exposes a clear interface.

### Generic pipeline

A `GenericPipeline` orchestrates reusable units for one class of work. It is invoked many times with different configurations.

### Configuration

`Configuration` defines per-case inputs and parameters for a generic pipeline. It carries variation without creating parallel implementations.

### Composition

`Composition` combines units into a full flow with clear handoffs and minimal overlap.

### Decomposition quality

`DecompositionQuality` reflects how well boundaries reduce duplication and cognitive load over time.

## Rules

### Decompose by responsibility

Split the system into units by function, not by incidental file grouping or team ownership.

### Generalize repeated behavior

When similar behavior appears across flows, promote it into a shared unit or generic pipeline.

### Express variation in configuration

Use configuration to describe differences per data object instance or kind.

Example:
- Prefer one generic pipeline for all data objects of the same kind, with configuration per object.
- Avoid one separate pipeline for each individual data object when behavior is the same.

### Refactor when duplication appears

If multiple near-identical pipelines exist, refactor toward reusable units and one configurable pipeline.

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](../../readme.md)
  - Definitions
    - [Business intelligence](../../definitions/business-intelligence.md)
    - [Data engineering](../../definitions/data-engineering.md)
  - Design patterns
    - Data engineering
      - [Data extractor](../data-engineering/data-extractor.md)
      - [Data object container](../data-engineering/data-object-container.md)
      - [Data object poller](../data-engineering/data-object-poller.md)
      - [Data object tree property inheritance](../data-engineering/data-object-tree-property-inheritance.md)
      - [Data object tree](../data-engineering/data-object-tree.md)
      - [Data object](../data-engineering/data-object.md)
      - [Data solution layer](../data-engineering/data-solution-layer.md)
      - [Data solution](../data-engineering/data-solution.md)
      - [Event-based orchestration](../data-engineering/event-based-orchestration.md)
      - [Historic bitemporal table](../data-engineering/historic-bitemporal-table.md)
    - Generic
      - [Functional decomposition](functional-decomposition.md)
      - [Prefer simple decomposition](prefer-simple-decomposition.md)
      - [Separate what and how](separate-what-and-how.md)
      - [Simplicity](simplicity.md)
  - Implementation
    - Event Based Orchestration
      - [Event-based orchestration architecture](../../implementation/event-based-orchestration/architecture.md)
      - [Azure event-based orchestration architecture](../../implementation/event-based-orchestration/azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](../../implementation/event-based-orchestration/tool-choice.md)
- Related repositories
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026)
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026)
<!-- markdown-project-structure:end -->
