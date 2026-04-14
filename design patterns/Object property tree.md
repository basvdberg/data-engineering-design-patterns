# Data object property tree

## Purpose

Data objects have a hierarchical structure. For example: A table lives inside a schema, a schema lives inside a database and a database is hosted on a server, or a CSV file lives inside a folder that is part of a storage container that is part of a storage account.

For data engineering, we want to assign flexible properties to data objects that might also be inherited by descendants. For example, we might want to assign a source system name property to all tables and schemas that exist in a certain database. Or we might want to assign an `include for ingestion` property to all files in a certain folder except for files A, B and C. 

## Benefits

- Non redundant way to represent property object relationship (no copy-pasting), thus fault tolerant. 
- Ability to specify generic properties. E.g. valid for an entire database or server. But also have the option to specify exceptions on generic rules. 
- When new data objects arrive that fall under the scope of existing properties, nothing needs to be done. 
- Using a simple boolean include properties you can easily specify the scope of your data transformation as opposed to for example having to list entire file paths several times in a json config file. 

## Summary

Objects are modeled as a tree, properties are attached and inherited, and orchestration reads the resolved metadata to decide how each object must be processed.

## Components

### Obj

The `Obj` entity is the registry of data objects and containers involved in data processing. It stores each object and its parent-child relation so that datasets can be represented from broad domains down to concrete tables, files, or views.

Examples:
- A root object `sales`.
- A child object `sales.raw`.
- A leaf object `sales.raw.orders_csv`.

### ObjSchema

The `ObjSchema` entity stores structural metadata for each object so orchestration and downstream tasks can validate expectations before processing.

Examples:
- Expected columns and data types for `sales.raw.orders_csv`.
- Primary key fields for curated objects.
- Optional partitioning and clustering metadata.

### Prop

The `Prop` entity defines reusable property types that represent configurable behavior.

Examples:
- Retention period in days.
- Required freshness SLA.
- Allowed load mode (`full`, `incremental`, `merge`).

### ObjProp

The `ObjProp` entity links a property to an object, including value and validity metadata. Properties can be inherited from parent objects unless overridden on the child.

Examples:
- A domain-level retention rule inherited by all child objects.
- A table-level override for load mode because of source-system limitations.

### Property resolution rules

Resolved object configuration is calculated at runtime by combining inherited and directly assigned properties.

Typical rules:
- Child properties override inherited parent properties for the same key.
- Missing properties fall back to parent values until the root is reached.
- If a required property is not resolved, orchestration raises a configuration error.

### Core object-property flow

1. An object is registered in `Obj` and linked to its parent.
2. Contracts, schema definitions, and properties are assigned at appropriate levels.
3. When orchestration prepares a task for a concrete object, it resolves inherited and local properties into one effective configuration.
4. The task executes using this resolved configuration (for example selected load mode, retention, and validation rules).
