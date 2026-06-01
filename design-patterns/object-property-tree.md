# Data object property tree

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Data Object (Obj)](#data-object-obj)
  - [TableSchema](#tableschema)
  - [Prop](#prop)
  - [ObjProp](#objprop)
  - [Property resolution rules](#property-resolution-rules)
- [Processes](#processes)
  - [Object discovery](#object-discovery)
  - [Table schema discovery](#table-schema-discovery)
<!-- markdown-toc:end -->

## Purpose

Data objects have a hierarchical structure. For example: A table lives inside a schema, a schema lives inside a database and a database is hosted on a server, or a CSV file lives inside a folder that is part of a storage container that is part of a storage account.

For data engineering, we want to assign flexible properties to data objects that might also be inherited by descendants. For example, we might want to assign a source system name property to all tables and schemas that exist in a certain database. Or we might want to assign an `include for ingestion` property to all files in a certain folder except for files A, B and C. 

## Benefits

- Non redundant way to represent property object relationship (no copy-pasting), thus less errror prone. 
- Ability to specify generic properties. E.g. valid for an entire database or server. But also have the option to specify exceptions on generic rules. 
- When new data objects arrive that fall under the scope of existing properties, nothing needs to be done. 
- Using a simple boolean include properties you can easily specify the scope of your data transformation as opposed to for example having to list entire file paths several times in a json config file. 

## Summary

Objects are modeled as a tree, properties are attached and inherited. It is possible to have both inheritance and exceptions.  

## Components

### Data Object (Obj)

The `Obj` entity is the registry of data objects and containers involved in data processing. It stores each object and its parent-child relation so that datasets can be represented from broad domains down to concrete tables, files, or views.

Examples:
- A root object `sales`.
- A child object `sales.raw`.
- A leaf object `sales.raw.orders_csv`.

### TableSchema

If the object is a table (either in a database or in a file), The `TableSchema` entity stores structural metadata, like: 

- Columns and data types.
- Primary and foreign key fields.
- Nullable property
- Default values
- Partitioning or indexing metadata.

### Prop

The `Prop` entity defines properties that can be assigned to data objects.

Examples:
- Retention period in days.
- Required freshness SLA.
- Allowed load mode (`full`, `incremental`).
- Is inluded in ingestion (yes/no)
  
### ObjProp

The `ObjProp` entity links a property to an object, including value and validity metadata. Properties can be inherited from parent objects unless overridden on the child.

Examples:
- A domain-level retention rule inherited by all child objects.
- A table-level override for load mode because of source-system limitations.

### Property resolution rules

The object property tree is calculated at runtime by combining inherited and directly assigned properties.

Typical rules:
- Child properties override inherited parent properties for the same key.
- Missing properties fall back to parent values until the root is reached.

## Processes
### Object discovery

This process discovers all objects for a given parent. For example, recursively scan all databases, schemas, tables, and views on a given database server, Or scan all files and folders recursively for a given path.

### Table schema discovery 

This process extracts the table schema metadata from a relational database.

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
    - [Functional decomposition](functional-decomposition.md)
    - [Historic bitemporal table](historic-bitemporal-table.md)
    - [Data object property tree](object-property-tree.md)
    - [Prefer simple decomposition](prefer-simple-decomposition.md)
    - [Separate what and how](separate-what-and-how.md)
    - [Simplicity](simplicity.md)
  - Implementation
    - Event Based Orchestration
      - [Event-based orchestration architecture](../implementation/event-based-orchestration/architecture.md)
      - [Azure event-based orchestration architecture](../implementation/event-based-orchestration/azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](../implementation/event-based-orchestration/tool-choice.md)
- Related repositories
  - [Data Engineering 2026](https://github.com/basvdberg/data-engineering-2026)
  - [Data Solution 2026](https://github.com/basvdberg/data-solution-2026)
<!-- markdown-project-structure:end -->
