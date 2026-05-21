# Separate what and how

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Specification](#specification)
  - [Implementation](#implementation)
  - [Contract](#contract)
  - [One-to-many relationship](#one-to-many-relationship)
- [Rules](#rules)
  - [Specification is declarative](#specification-is-declarative)
  - [Implementation is imperative](#implementation-is-imperative)
  - [No implementation details in the specification](#no-implementation-details-in-the-specification)
  - [One specification, many implementations](#one-specification-many-implementations)
<!-- markdown-toc:end -->

## Purpose

Any non-trivial solution can be described on two levels: *what* it does, and *how* it does it. These two levels change for different reasons, on different timescales, and are best understood by different audiences. This design pattern keeps them separated. The *what* is captured in a declarative specification that states intent. The *how* is captured in an imperative implementation that realises that intent on a concrete platform.

The reason this separation is worthwhile is that the relationship between the two is one-to-many: a specific functionality can be implemented in many ways, on many platforms, with many trade-offs. Treating the two as one thing forces every change in either to ripple into the other.

## Benefits

- Substitutability. Multiple implementations can satisfy the same specification, so an implementation can be replaced (because of cost, performance, deprecation, or licensing) without changing the specification or anything that depends on it.
- Longevity. Specifications tend to outlive implementations. A clear specification keeps its value across generations of tooling, while the implementation behind it can be rewritten when needed.
- Comparability. With an explicit specification, competing implementations can be evaluated on the same criteria instead of described in their own vocabularies.
- Parallel evolution. Because the contract between specification and implementation is explicit, the two can evolve in parallel: a new implementation can be developed against the current specification, and a new specification can be drafted before any implementation exists.
- Reasoning at the right level. Stakeholders who care about behaviour can read the specification; engineers who care about mechanism can read the implementation. Neither has to understand the other's level to understand their own.

## Summary

A solution is described twice. Once as a specification that says *what* it does, in declarative terms. Once as an implementation that says *how* it does it, in imperative terms. The two are connected by an explicit contract. Because a single specification can be realised by many implementations, the separation lets each side change independently.

## Components

### Specification

The `Specification` describes a solution in declarative terms. It states required behaviour, inputs, outputs, constraints, and quality attributes, without prescribing how any of these are achieved.

Examples:
- An API description that lists endpoints, parameters, and response shapes.
- A data contract that defines the columns, types, and freshness of a dataset.
- A requirement that states a function must return the median of a list of numbers.
- A policy that states authentication must use a time-limited token.

### Implementation

The `Implementation` realises a specification on a concrete platform. It contains the imperative steps, the chosen tools, and the operational details that make the specified behaviour actually happen.

Examples:
- A Python service that exposes the API described by a specification.
- A SQL pipeline that produces the dataset described by a data contract.
- A specific algorithm (quickselect, sorting, histogram-based) that returns the median.
- A library call that issues and validates time-limited tokens.

### Contract

The `Contract` is the explicit link between a specification and its implementations. It defines what an implementation must accept, produce, and guarantee in order to be considered a valid realisation of the specification.

Examples:
- A schema (JSON Schema, OpenAPI, Avro) that any conforming implementation must honour.
- A test suite that any implementation must pass.
- A formal interface or abstract type in a programming language.
- A service-level objective that every implementation must meet.

### One-to-many relationship

The `OneToManyRelationship` is the structural reason this pattern exists. A single specification can be satisfied by many implementations that differ in technology, performance, cost, or operational profile. Conversely, when an implementation is the only way to express the intent, the specification is missing or incomplete.

Examples:
- The same REST API specification implemented by services in different languages or hosted on different platforms.
- The same data contract produced by a batch job today and a streaming job tomorrow.
- The same sorting specification implemented by quicksort, mergesort, or a database operator.

## Rules

### Specification is declarative

A specification states *what* must be true, not *how* it is achieved. It uses nouns and properties (data shapes, invariants, quality attributes) rather than verbs and steps.

### Implementation is imperative

An implementation describes the sequence of operations that produce the specified outcome. It is bound to a platform, a language, and a deployment context.

### No implementation details in the specification

A specification must not name specific tools, libraries, vendors, or algorithms. If a constraint matters at the specification level (for example, a regulatory algorithm), it is restated as a property of the outcome, not as a directive about *how* to compute it.

### One specification, many implementations

If the same specification cannot, in principle, be realised by more than one implementation, the specification is too tightly coupled to a single platform. Either the specification leaks implementation details, or what looks like a specification is really an implementation in disguise.

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](../readme.md)
  - Definitions
    - [Business intelligence](../definitions/business-intelligence.md)
    - [Data engineering](../definitions/data-engineering.md)
  - Design patterns
    - [Data solution](data-solution.md)
    - [Event-based orchestration](event-based-orchestration.md)
    - [Historic bitemporal table](historic-bitemporal-table.md)
    - [Data object property tree](object-property-tree.md)
    - [Separate what and how](separate-what-and-how.md)
  - Implementation
    - Event Based Orchestration
      - [Event-based orchestration architecture](../implementation/event-based-orchestration/architecture.md)
      - [Azure event-based orchestration architecture](../implementation/event-based-orchestration/azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](../implementation/event-based-orchestration/tool-choice.md)
- Related repositories
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026)
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026)
<!-- markdown-project-structure:end -->
