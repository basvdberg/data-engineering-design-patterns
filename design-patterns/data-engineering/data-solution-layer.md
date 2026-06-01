# Data solution layer

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Staging layer](#staging-layer)
  - [Raw layer](#raw-layer)
  - [Integrated layer](#integrated-layer)
  - [Presentation layer](#presentation-layer)
  - [Layer flow](#layer-flow)
- [Rules](#rules)
  - [Unidirectional flow](#unidirectional-flow)
  - [Staging is ephemeral](#staging-is-ephemeral)
  - [Raw is append-only history](#raw-is-append-only-history)
  - [Source-shaped modelling stops at raw](#source-shaped-modelling-stops-at-raw)
  - [Consumers read presentation](#consumers-read-presentation)
- [Related models](#related-models)
<!-- markdown-toc:end -->

## Purpose

A data solution layer decomposes a data solution into layers with a clear, scoped boundary and purpose. Each layer depends only on the layer beneath it and acts as the source for the next.

Layering separates concerns so each layer handles its own class of issues. Staging deals with network failures, protocol errors, and source quirks. Raw deals with conversion and schema errors. Integrated deals with modelling errors. Recovery is local: an error in one layer is fixed and the layer is rebuilt from the layer below without touching upstream layers.

## Benefits

- Predictable recovery — each layer re-runs from the layer below without touching upstream sources when not required.
- Stable ingestion — staging absorbs source volatility before history and modelling.
- Durable audit — raw keeps an append-only record of everything that arrived.
- Reusable modelling — integrated holds one governed model for many use cases.
- Safe consumption — presentation exposes audience-specific views without rewriting history.

## Summary

Data flows in one direction: source → `Staging` → `Raw` → `Integrated` → `Presentation`. Staging is a transient buffer with source-to-target format translation and idempotent extraction. Raw is permanent, append-only, and modelled according to source. Integrated applies the governed business model from raw. Presentation curates integrated data for end users. Each layer answers a distinct concern; failure recovery restarts at the layer that failed, using the layer beneath as input.

## Components

### Staging layer

The `StagingLayer` is a transient buffer where extracted data first lands. Content for a given batch is replaced on each load. Extractors write here only.

Staging provides three capabilities:

- **Recoverability** — extraction is idempotent. Each logical batch maps to at most one physical payload keyed by source, dataset, and time window. A re-run overwrites that payload; promotion to raw is transactional per batch.
- **Decoupling** — only extractors contact sources. Outages, throttling, and protocol behaviour stay in ingestion; downstream layers read staging or raw.
- **Format translation** — source payloads become a canonical staging format through structural normalization (names, types, flattening, encoding). Modelling remains according to source; business rules belong in integrated.

### Raw layer

The `RawLayer` is the permanent, append-only store of every payload promoted from staging. It is never truncated. Structure and grain follow the source. It is the foundation for reprocessing integrated and presentation when transformation logic changes. It also acts as a backup of source data that may no longer exist at the source, because sources may overwrite or clean up data. For this reason, a backup of the raw layer is vital.

### Integrated layer

The `IntegratedLayer` holds modelled, transformed, query-ready data fed from raw. It applies governed keys, entities, rules, and structures for joins, metrics, and lineage. Modelling is according to the business model, not the source layout.

### Presentation layer

The `PresentationLayer` exposes consumption-facing tables, views, datasets, or exports built from integrated. Layout and aggregation follow audience or use case. It is the only layer intended for routine end-user and application access.

### Layer flow

1. Extract from source into staging (translate format, idempotent write).
2. Promote batch from staging into raw (append, clear or replace staging for that batch).
3. Transform raw into integrated (governed model).
4. Publish integrated into presentation (curated interfaces).

## Rules

### Unidirectional flow

Data moves source → staging → raw → integrated → presentation. A layer reads only from the layer directly beneath it for standard pipeline loads.

### Staging is ephemeral

Staging content for a batch may be replaced or removed after successful promotion. Long-term retention belongs in raw.

### Raw is append-only history

Raw receives new arrivals as append events. Corrections arrive as new events with lineage, not in-place overwrites of prior history.

### Source-shaped modelling stops at raw

Staging and raw model according to source. Governed business modelling begins in integrated.

### Consumers read presentation

Routine consumption uses presentation. Access to raw or integrated is for engineering, audit, and reprocessing — not for default application queries.

## Related models

This pattern aligns with established industry layering. Names vary across models; the responsibilities and the unidirectional flow are the same.

| Role | This pattern | [Matillion](https://docs.matillion.com/) reference architecture | [Data Vault 2.0](https://datavaultalliance.com/) |
|------|--------------|-----------------------------------------------------------------|--------------------------------------------------|
| Transient ingest buffer | `Staging` | `Landing` / `Stage` | `Staging Area` |
| Permanent source-shaped history | `Raw` | `Persistent stage` / `Raw vault` | `Persistent Staging Area` (PSA) / `Raw Data Vault` (RDV) |
| Governed business model | `Integrated` | `Integration` / `Transform` | `Business Data Vault` (BDV) |
| Curated consumption | `Presentation` | `Mart` / `Publish` | `Information Mart` (IM) |

Notes on mapping:

- Data Vault splits source-shaped history into two artefacts — the optional `Persistent Staging Area` and the `Raw Data Vault` (hubs, links, satellites). Both serve the `Raw` role in this pattern.
- Matillion terminology varies between its products and reference designs; the column lists the most common terms across its documentation.
- A given platform may collapse the `Raw` and `Integrated` roles into one physical store while keeping the role boundary in the model.

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
