# Simplicity

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Simple solution](#simple-solution)
  - [Simplicity preference](#simplicity-preference)
  - [System boundary](#system-boundary)
  - [Complexity pressure](#complexity-pressure)
- [Rules](#rules)
  - [Prefer the simpler correct design](#prefer-the-simpler-correct-design)
  - [Keep the system boundary small](#keep-the-system-boundary-small)
  - [Remove non-essential assets](#remove-non-essential-assets)
  - [Use functional decomposition when it reduces complexity](#use-functional-decomposition-when-it-reduces-complexity)
<!-- markdown-toc:end -->

## Purpose

`Simplicity` prefers simpler approaches over more complex approaches in system design. A simpler design has fewer concepts, fewer moving parts, and clearer boundaries.

The pattern protects maintainability by keeping the system small enough to understand and change safely.

## Benefits

- Lower cognitive load for readers and maintainers.
- Faster delivery because fewer parts must be coordinated.
- Lower defect risk from smaller change surface.
- Clearer boundaries around core functionality.
- Easier cleanup because non-essential parts stay visible.

## Summary

A `SimpleSolution` uses the minimum structure needed for the required outcome. Complexity is introduced only when it is required for correctness or constraints. `FunctionalDecomposition` is one way to achieve this simplicity, but simplicity is the higher-level preference.

## Components

### Simple solution

A `SimpleSolution` satisfies the requirement with the smallest reliable structure. It keeps the number of concepts and files low.

### Simplicity preference

`SimplicityPreference` is the decision rule between valid options. If two options are correct, select the one that is easier to understand and maintain.

### System boundary

`SystemBoundary` defines what is part of the core system and what is optional. Protecting this boundary keeps growth controlled.

### Complexity pressure

`ComplexityPressure` is the tendency to add files, paths, and special cases over time. The pattern counters this with regular cleanup and simplification.

## Rules

### Prefer the simpler correct design

When multiple designs are correct, choose the design with fewer concepts and less operational overhead.

### Keep the system boundary small

Keep only what is needed for core functionality inside the main boundary. Move optional material outside or remove it.

### Remove non-essential assets

Prefer a GitHub repository with fewer files over one with many more files when both satisfy the same goal. Delete or clean up artifacts that are not mandatory for core functionality.

### Use functional decomposition when it reduces complexity

Apply `FunctionalDecomposition` when it reduces duplication and operational complexity. For example, prefer one generic pipeline configured per data object kind over one pipeline per data object.

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
