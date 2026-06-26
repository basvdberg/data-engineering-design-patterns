# Data object contract

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Quality of service](#quality-of-service)
  - [Refresh contract](#refresh-contract)
  - [Contract alignment](#contract-alignment)
- [Rules](#rules)
  - [Consumer-facing commitments](#consumer-facing-commitments)
  - [Producer refresh mechanics](#producer-refresh-mechanics)
  - [Single specification per object](#single-specification-per-object)
  - [Versioned and reviewable](#versioned-and-reviewable)
- [References](#references)
<!-- markdown-toc:end -->

## Purpose

Consumers need a single, reviewable specification for what a published data object delivers and how the producer refreshes it. A `DataObjectContract` combines two complementary specifications: [data object quality of service](data-object-quality-of-service.md) states consumer-facing quality metrics; [data object refresh contract](data-object-refresh-contract.md) states when and how each refresh runs so those metrics can be met.

The contract is declarative metadata attached to a `DataObject`. Orchestration, monitoring, and catalog tools read it without embedding implementation detail.

## Benefits

- One place for consumers to read delivery commitments and refresh mechanics.
- Clear separation between *what* is promised and *how* refresh is triggered and scoped.
- Measurable alignment between `Frequency`, `Latency`, and `ArrivalWindow`.
- Auditable, versioned metadata for dependency planning and incident response.
- Reusable across platforms when implementations honour the same contract fields.

## Summary

A `DataObjectContract` pairs a quality-of-service specification with a refresh-contract specification for the same object. Quality of service defines freshness, availability, and service-level dimensions. Refresh contract defines triggers, access mode, scope, snapshot time, permitted extract windows, arrival windows, and backfill windows. Together they form the complete delivery specification for a published data object.

## Components

### Data object contract

The `DataObjectContract` is the root specification for a published `DataObject`. It references a quality-of-service block and a refresh-contract block. Catalog and orchestration metadata carry the contract version alongside object identity.

### Quality of service

The quality-of-service specification states consumer-facing delivery metrics in three dimension groups defined in [data object quality of service](data-object-quality-of-service.md):

- **Data freshness** — `Frequency` (Fy) and `Latency` (Ly).
- **Data availability** — `Availability` (Av), `GeneralAvailability` (Ga), `EndOfSupport` (Es), `EndOfLife` (El), and `Retention` (Re).
- **Data service levels** — `Throughput` (Th), `ErrorRate` (Er), `TimeToDetect` (Td), `TimeToNotify` (Tn), and `TimeToRepair` (Tr).

Examples:
- Daily `Frequency` with 90-minute `Latency` for an operational mart.
- 99.5% `Availability` with published `EndOfSupport` and `Retention` dates.

### Refresh contract

The refresh-contract specification states producer refresh mechanics in seven fields defined in [data object refresh contract](data-object-refresh-contract.md):

- `RefreshTrigger` — time-based, dependency-based, or combined start conditions.
- `AccessMode` — direct read of the live source or read from a published snapshot.
- `RefreshScope` — full, partition, or subset of data refreshed.
- `SnapshotTime` — moment the source snapshot was taken for the scope.
- `PermittedExtractWindow` — agreed window when the source may be read.
- `ArrivalWindow` — expected window from snapshot readiness to published object.
- `BackfillWindow` — how far back late or corrected partitions may be reprocessed.

Examples:
- `DependencyTrigger` on upstream **publish success** with partition-aligned `RefreshScope`.
- Midnight `TimeTrigger` with `PermittedExtractWindow` 00:00–06:00 and `ArrivalWindow` 00:30–02:00.

### Contract alignment

`ContractAlignment` binds the two specifications: refresh mechanics must support the stated quality metrics. `ArrivalWindow` and chain `Latency` must fit inside consumer `Frequency` and `Latency` targets. Downstream `PermittedExtractWindow` and `ArrivalWindow` values derive from upstream refresh contracts in dependency chains.

## Rules

### Consumer-facing commitments

The quality-of-service block states every metric consumers rely on for planning, access, and incident expectations. Publish the block at the consumer access boundary for the object.

### Producer refresh mechanics

The refresh-contract block states every field operators and orchestration need to start, scope, and time each refresh. Omit fields only when the object role makes them inapplicable (for example downstream layers with no direct source extract).

### Single specification per object

Each published `DataObject` carries one `DataObjectContract`. Dependency objects each carry their own contract; chain latency is the sum of aligned refresh and processing intervals across the chain.

### Versioned and reviewable

Store contract metadata in the solution catalog with object identity. Review contract changes with the same rigour as schema or ownership changes.

## References

- Nichols, K., Blake, S., Baker, F., & Black, D. (1998). *RFC 2475: An Architecture for Differentiated Services*. Internet Engineering Task Force. https://www.rfc-editor.org/rfc/rfc2475 — Delivery-quality dimensions adapted for data objects.

- Bitol. (2024). *Open Data Contract Standard v3.1.0: Service level agreement*. Linux Foundation. https://bitol-io.github.io/open-data-contract-standard/v3.1.0/service-level-agreement/ — `slaProperties` vocabulary for frequency, latency, availability, and retention fields.

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
