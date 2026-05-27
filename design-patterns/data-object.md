# Data object

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Components](#components)
  - [Identity](#identity)
  - [Data object container](#data-object-container)
  - [Physical location](#physical-location)
  - [Schema](#schema)
  - [Classification](#classification)
<!-- markdown-toc:end -->

## Purpose

A data object is an almost atomic element of a data solution. It is composed of data items (or columns). It carries a location where the data is stored and a protocol for how to reach that location.

Examples of data objects are:

- A SQL database table.
- A CSV file on a Windows network share.
- A dataset accessed via a REST API.

A data object consists of data and metadata. Data is evidence of past activity — frozen moments in time waiting to be uncovered and analyzed [Data Engine Thinking]. Metadata describes the properties and structure of the data object.

## Components

### Identity

A `DataObject` identity is used to uniquely identify the object across metadata, mappings, and lineage. The preferred form is a relative path that doubles as a logical location:

```text
staging/openmeteo/daily-temperature
<solution-layer>/<source-system>/<data-object-name>
```

Identity carries three fields:

- `id` — the unique key (logical path).
- `name` — the human-facing label.
- `notes` — free-form description.

### Data object container

A data object always exists in a [data object container](data-object-container.md). Common containers are:

- A database schema.
- A Windows file share folder.
- A local file path.
- A public REST API URL parent.

The container provides inherited properties (connection, owner, classifications) per the [data object property tree](object-property-tree.md).

### Physical location

A data object always has a physical location — where the data is actually stored or reachable. Location is part of the identity: copying the object to another location creates another data object, even if the bytes are identical. Moving an object to another layer makes it a new object.

The physical location is referenced through a `DataConnection`:

- `dataConnectionId` — path-based reference to a connection artefact.
- The connection carries protocol, base URL, file path, format, and authentication metadata.

Multiple data objects share the same `DataConnection` by reference; the connection is not duplicated inside each object.

### Schema

The `Schema` lists the `DataItems` (columns, fields) of the data object. Each `DataItem` carries:

- `name` — field name.
- `ordinalPosition` — position in the record (1-based).
- `dataType` — logical type (`string`, `double`, `int`, `date`, …).
- `notes` — optional free-form description.
- Optional sizing — `characterLength`, `numericPrecision`, `numericScale`.
- Optional key flag — `isPrimaryKey`.

Source data objects may declare an empty `dataItems` list when the source is opaque (for example a REST endpoint whose response is normalized downstream). Hierarchy and inherited structural properties are covered by [data object property tree](object-property-tree.md).

### Classification

A `Classification` is a `(group, classification)` pair attached to a data object. Classifications support routing, filtering, lineage, and reporting without changing the schema.

Examples:

- `(Solution Area, Landing Area)` — places the object in the staging landing zone.
- `(Solution Layer, Staging Layer)` — names the layer.
- `(source, inventory_api)` — declares the originating source system.
- `(protocol, parquet)` — declares the on-disk format.

A data object may carry any number of classifications; orchestration and ADL templates read them to decide what to do with the object.

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](../readme.md)
  - Definitions
    - [Business intelligence](../definitions/business-intelligence.md)
    - [Data engineering](../definitions/data-engineering.md)
  - Design patterns
    - [Data extractor](data-extractor.md)
    - [Data object container](data-object-container.md)
    - [Data object poller](data-object-poller.md)
    - [Data object](data-object.md)
    - [Data solution layer](data-solution-layer.md)
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
