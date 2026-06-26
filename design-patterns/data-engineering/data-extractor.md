# Data extractor

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Properties](#properties)
- [Components](#components)
  - [FormatAdapter](#formatadapter)
  - [TransferProtocol](#transferprotocol)
  - [NetworkLogistics](#networklogistics)
  - [Integrity](#integrity)
  - [Observability](#observability)
  - [Extraction metadata](#extraction-metadata)
<!-- markdown-toc:end -->

## Purpose

A `DataExtractor` reads data using a specific `TransferProtocol` at a `SourceLocation` in a specific format using a `FormatAdapter` and writes at a `TargetLocation` in a specific format. The `TransferProtocol` uses `NetworkLogistics` to make sure that data gets from A to B. It uses `IntegrityControls` to deal with any sort of issues, like network issues, storage issues, service failures.

## Properties

- Knows the ins and outs of a specific data format and protocol. 
- Validates whether the sources data conforms to the data format specification
- Deal with errors in the source data
- Reliable transfer through chunking, validation, and recovery.
- Observable runs via progress, warning, and error logging.
- Auditable lineage of what was moved, when, and with what outcome.
- Scalable handling of large payloads without loading everything at once.
- Portable design across formats and transfer mechanisms.


## Components

### FormatAdapter

The `FormatAdapter` interprets the source format on read and produces the target format on write. It owns format-specific concerns (structure, encoding, compression, schema mapping) but not how bytes are moved.

Examples:
- Parse delimited text and write a columnar file.
- Read paginated hierarchical responses and write a single record-oriented file.

### TransferProtocol

The `TransferProtocol` is the mechanism that moves bytes between source and target. It covers connection setup, authentication, and protocol-level options such as timeouts and transport-layer retries.

Examples:
- File transfer over a secure file protocol.
- Authenticated HTTP request and response.

### NetworkLogistics

`NetworkLogistics` applies when source and target are not co-located. It addresses bandwidth, latency, proxy or egress rules, and resumption across interrupted sessions.

Examples:
- Resume a large download from a byte offset after a timeout.
- Throttle parallel chunk transfers to stay within an egress policy.

### Integrity

`TransferValidation` and `RecoveryState` prove completeness and correctness (checksums, counts, structural checks) and allow retry from the last successful chunk without redoing finished work.

Examples:
- Checksum match per chunk and for the full run.
- Resume run after chunk 7 fails without rewriting chunks 1–6.

### Observability

`OperationalLog` and `AuditTrail` capture run lifecycle, progress, warnings, errors, and a durable record of who or what ran, which locations were used, and final status.

Examples:
- Progress: 12 of 20 chunks complete.
- Audit entry linking run id to source, target, and validation result.

### Extraction metadata

`ExtractionMetadata` describes the landed payload separately from the bytes: size, chunk summary, format, and schema-related descriptors when known.

Examples:
- Total size in megabytes and record count.
- Schema version token attached to the run.

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
