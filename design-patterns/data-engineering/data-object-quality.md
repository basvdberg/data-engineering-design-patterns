# Data object quality

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Dimensions](#dimensions)
  - [Accuracy](#accuracy)
    - [Accuracy vs. the real world](#accuracy-vs-the-real-world)
    - [Accuracy vs. source system](#accuracy-vs-source-system)
  - [Completeness](#completeness)
  - [Conformity](#conformity)
  - [Consistency](#consistency)
  - [Coverage](#coverage)
  - [Uniqueness](#uniqueness)
<!-- markdown-toc:end -->

## Purpose

Defines the quality of a data object in several dimensions:

| Dimension | Question it answers |
|-----------|---------------------|
| **accuracy** | Does the value match the authoritative source? |
| **completeness** | Are required values populated? |
| **conformity** | Does content follow the required format, type, or domain? |
| **consistency** | Do values and definitions match across stores? |
| **coverage** | Are all expected records present? |
| **uniqueness** | Is each record and attribute recorded once? |
| **referential integrity** | Do foreign keys refer to existing items? | 
## Dimensions

### Accuracy

Accuracy (Ac) measures how truthfully a value represents what it claims to describe. It has two reference points — the real world and the source system. 

#### Accuracy vs. the real world

Measures correctness of the value against the real world. 

Examples:
- A source system records that a customer lives at address A at a certain point in time, while in fact they live at address B.
- A customer is 24 years old but the source systems records 42.

#### Accuracy vs. source system

Measures correctness of the data against its authorative source system at a certain point in time. The source is treated as the authority, even if the source itself is wrong about the real world.

Examples:
- The data solution says a customer lives at address C at a point in time, while the source said address D.
- The data solution says a customer lives at address A at a point in time, which matches the source system, but not the real world.
- A data solution says a customer is 42 years old while the source says 41 years.

### Completeness

Completeness (Cp) requires that an attribute is populated with a value where one is required (not null). It checks that all necessary attributes are present in the record.

Examples:
- A required invoice number is missing.
- A credit card number is missing its expiration month.

### Conformity

Conformity (Cf) requires content to align with required standards, syntax (format, type, range), or permitted domain values. It measures how closely data adheres to internal, external, or industry standards.

Examples:
- A customer identifier must be five characters long.
- An address type must come from the governed list of address types.

### Consistency

Consistency (Cs) requires that content stays the same across data stores. Values, formats, and definitions in one place should match those in another.

Examples:
- Revenue is calculated differently in two data stores.
- A string is truncated from 255 to 32 characters between the website and the warehouse.

### Coverage

Coverage (Cv) requires that all expected records are present in the store or source. It concerns records that should exist but are absent from the dataset.

Examples:
- Every customer must exist in the customer database.
- A replicated table is missing rows present in the source.

### Uniqueness

Uniqueness (Uq) requires that no record or attribute is recorded more than once. Each entity should appear as a single entry.

Examples:
- The same customer exists under two identifiers or spellings.
- A share is recorded as both equity and debt in the same database.

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
