# Specification driven documentation

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Source schema specification](#source-schema-specification)
  - [Target schema specification](#target-schema-specification)
  - [Mapping specification](#mapping-specification)
  - [Element description](#element-description)
  - [Generated documentation](#generated-documentation)
  - [Specification gate](#specification-gate)
  - [Documentation flow](#documentation-flow)
- [Use cases](#use-cases)
  - [1. Business meaning of a derived column](#1-business-meaning-of-a-derived-column)
  - [2. Multi-layer mapping with lineage](#2-multi-layer-mapping-with-lineage)
  - [3. Agent generates transform code](#3-agent-generates-transform-code)
  - [4. Gate blocks code without an updated specification](#4-gate-blocks-code-without-an-updated-specification)
- [Rules](#rules)
  - [Define each fact once](#define-each-fact-once)
  - [Schemas carry meaning](#schemas-carry-meaning)
  - [Mappings are declarative](#mappings-are-declarative)
  - [Humans read generated views](#humans-read-generated-views)
  - [Specification before implementation](#specification-before-implementation)
- [References](#references)
<!-- markdown-toc:end -->

## Purpose

Stakeholders need clear definitions of tables, columns, derived values, and lineage. Coding agents need an unambiguous specification of intent before they generate implementation. Both audiences need those definitions to stay aligned with every delivery change.

`SpecificationDrivenDocumentation` treats documentation as the declarative specification of a data solution: source schemas, target schemas, and the mappings between them. Human-facing pages and lineage visuals are generated from that single source. Related: [Separate what and how](../generic/separate-what-and-how.md) and [Simplicity](../generic/simplicity.md).

## Benefits

- Business and technical readers share one definition of each table and column.
- Coding agents receive machine-readable intent with enough structure to generate transforms.
- Lineage stays consistent with the mapping artefacts that agents and orchestrators use.
- Redundant copies of schema or mapping facts are avoided by defining each fact once.
- CI enforces that the specification is complete before implementation work starts.

## Summary

A change to a data solution starts with three declarative artefacts: a `SourceSchemaSpecification`, a `TargetSchemaSpecification`, and a `MappingSpecification` that links them across one or more layers. Every schema element carries an `ElementDescription` that states business meaning and how the element is constructed. `GeneratedDocumentation` renders clickable pages and lineage visuals from those artefacts. A `SpecificationGate` in the delivery pipeline requires the artefacts to pass review before code is generated or merged.

## Components

### Source schema specification

The `SourceSchemaSpecification` lists every source data object, its data items, logical types, and an `ElementDescription` per object and item. It states what the source means, not how extraction is implemented.

Examples:
- An API payload object with items for station identity, observation time, and measured value.
- A source ledger table with items for account, booking date, and amount.

### Target schema specification

The `TargetSchemaSpecification` lists every target data object, its data items, logical types, domains, and an `ElementDescription` per object and item. Construction of derived items is explained in the description and traced through the mapping.

Examples:
- A staging object that mirrors source grain after format normalisation.
- A presentation mart object with a derived margin item built from revenue and cost items.

### Mapping specification

The `MappingSpecification` declares how source items become target items across one or more solution layers. Each mapping references source and target objects by identity, lists item-level mappings, and may chain through intermediate objects. Mapping edges are the design-time lineage used by agents and by generated visuals.

Examples:
- One source object mapped one-to-one into a staging object.
- Raw items mapped through an integrated entity into a presentation fact.

### Element description

An `ElementDescription` is the human-readable meaning of a data object or data item. It states business intent and, for derived items, how the value is constructed so both stakeholders and engineers understand the element without reading implementation code.

Examples:
- Target item `value`: daily mean 2 m air temperature in degrees Celsius for the station and day.
- Target item `margin`: revenue minus cost for the order line, excluding tax.

### Generated documentation

`GeneratedDocumentation` is a view derived from the three artefacts: navigable pages for objects and items, and a `LineageView` that visualises object and item mappings. Authors maintain the structured artefacts; readers browse the generated view.

Examples:
- A documentation site page per data object with linked upstream and downstream objects.
- A column-level lineage diagram rendered from item mappings.

### Specification gate

The `SpecificationGate` is a delivery checkpoint after design and before coding. It requires source schema, target schema, and mapping artefacts to be present, internally consistent, and reviewed for the change under delivery.

Examples:
- A pull-request check that fails when a new target item has no mapping and no description.
- A pipeline stage that blocks code generation until the mapping for the target object is approved.

### Documentation flow

1. Design the change and identify affected source objects, target objects, and layers.
2. Update source and target schema specifications, including element descriptions.
3. Update the mapping specification and confirm lineage coverage for every target item.
4. Pass the specification gate; generate documentation views from the artefacts.
5. Generate or write implementation from the approved specification.

## Use cases

### 1. Business meaning of a derived column

A finance owner needs to trust a presentation margin before using it in a forecast. The target schema carries the construction rule; the mapping points at the contributing items so the owner can confirm meaning without reading SQL.

```json
{
  "targetDataObjectId": "presentation/sales/order-line",
  "dataItem": {
    "id": "presentation/sales/order-line/margin",
    "dataType": "decimal",
    "description": "Revenue minus cost for the order line, excluding tax."
  },
  "dataItemMapping": {
    "targetDataItem": "presentation/sales/order-line/margin",
    "sourceDataItems": [
      "integrated/sales/order-line/revenue",
      "integrated/sales/order-line/cost"
    ],
    "construction": "revenue - cost"
  }
}
```

### 2. Multi-layer mapping with lineage

An engineer traces a presentation temperature value back through integrated and raw to the source observation. Each layer has its own objects; mappings between layers form the lineage path rendered in the generated view.

```text
source/weather/observation
  → staging/weather/observation
  → raw/weather/observation
  → integrated/weather/daily-temperature
  → presentation/weather/daily-temperature
```

Item `value` maps identity-style through staging and raw, then aggregates by station and day in integrated before the presentation object exposes it.

### 3. Agent generates transform code

A coding agent receives the approved source schema, target schema, and mapping for a staging load. The artefacts name every item, type, and item mapping, so the agent can emit a transform that preserves grain and types without inventing undocumented columns.

```json
{
  "id": "data-object-mapping/staging/weather/daily-temperature",
  "sourceDataObjectIds": ["source/weather/daily-temperature"],
  "targetDataObjectId": "staging/weather/daily-temperature",
  "dataItemMappings": [
    {
      "sourceDataItems": ["source/weather/daily-temperature/station_id"],
      "targetDataItem": "staging/weather/daily-temperature/station_id"
    },
    {
      "sourceDataItems": ["source/weather/daily-temperature/value"],
      "targetDataItem": "staging/weather/daily-temperature/value"
    }
  ]
}
```

### 4. Gate blocks code without an updated specification

A pull request adds a presentation column without a target schema description or mapping edge. The specification gate fails the check; implementation is deferred until the artefacts are complete and reviewed.

```text
check: every target data item has description + mapping
result: fail — presentation/sales/order-line/discount has no mapping
```

## Rules

### Define each fact once

Store each schema fact and each mapping edge in one authoritative artefact. Generated documentation and implementations read that artefact by reference.

### Schemas carry meaning

Every published data object and data item includes an `ElementDescription` that a business reader can understand. Derived items state construction in the description and link it through the mapping.

### Mappings are declarative

A `MappingSpecification` states source identities, target identities, item mappings, and construction intent. Platform-specific code belongs in the implementation that realises the mapping.

### Humans read generated views

Publish navigable documentation and lineage visuals generated from the artefacts. Prefer regenerating the view over hand-maintaining a second copy of the same facts.

### Specification before implementation

Run the `SpecificationGate` after design and before coding or code generation for the change. Implementation proceeds only from an approved, consistent specification.

## References

- Bitol. (2024). *Open Data Contract Standard* (v3.1.0). Linux Foundation. https://bitol-io.github.io/open-data-contract-standard/ — Schema elements, business names, and property-level transform fields that inform source and target specifications.

- OpenLineage. (n.d.). *Column Level Lineage Dataset Facet*. https://openlineage.io/docs/spec/facets/dataset-facets/column-lineage-facet — Column-level lineage vocabulary adapted for design-time mapping edges and generated lineage views.

- Priebe, T., & Reisser, A. (n.d.). *Reinventing the Wheel?! Why Harmonization and Reuse Require a Business Information Model*. https://epub.uni-regensburg.de/19781/1/WI_Preibe_Reisser.pdf — Business information model as the semantic anchor for mappings between physical representations.

- Data Engineering Design Patterns. (2026). *Separate what and how* [Design pattern]. https://github.com/basvdberg/data-engineering-design-patterns/blob/main/design-patterns/generic/separate-what-and-how.md — Declarative specification versus imperative implementation; one specification, many implementations.

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
      - [Specification driven documentation](specification-driven-documentation.md)
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
