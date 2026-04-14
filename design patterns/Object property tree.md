# Object property tree

## Purpose

The object property tree is a metadata pattern that models data objects in a hierarchy and attaches configurable properties to each level. It provides one central structure to define object ownership, schema expectations, extraction contracts, and runtime behavior used by orchestration and processing tasks.

## Benefits

- Maintainability. Object definitions and properties are centralized, reducing duplicated configuration in pipelines and SQL code.
- Reusability. Shared properties can be defined at parent levels and inherited by child objects, minimizing repeated setup.
- Governance. Contracts and schema metadata are stored with the object model, making ownership and usage rules explicit.
- Flexibility. New behavior can be introduced by adding metadata properties instead of changing table designs or process code.

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
