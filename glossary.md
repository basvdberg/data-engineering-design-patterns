# Project Glossary

This glossary consolidates non-trivial terms used across this repository.

Status legend:
- `canonical`: preferred term to use in docs and design discussions.
- `alias`: acceptable synonym or physical/schema naming form.
- `deprecated`: legacy term found in older artifacts; avoid for new work.

## Core orchestration terms

| Term | Status | Definition |
| --- | --- | --- |
| `Event` | canonical | Recorded signal that a relevant data/process state change happened. |
| `Trigger` | canonical | Declarative routing rule that matches events and selects work. |
| `TaskTemplate` | canonical | Reusable execution blueprint with implementation reference and retry policy. |
| `QueueItem` | canonical | Runnable work item created when a trigger matches an event. |
| `Queue` | alias | Physical queue table that stores queue items and execution state. |
| `ControllerRule` | alias | Schema/entity name for routing rules; conceptually equivalent to trigger. |
| `TaskDefinition` | deprecated | Older wording for task template; use `TaskTemplate`. |
| `Event lifecycle` | canonical | Event phase classification, e.g. `Start`, `InProgress`, `EndSuccessful`, `EndFailed`. |
| `Retry policy` | canonical | Retry behavior for failed executions (`retry_max_attempts`, `retry_backoff_seconds`). |
| `Idempotent orchestration` | canonical | Execution behavior where reruns do not create unintended duplicate effects. |
| `Event-driven control loop` | canonical | Flow of event capture, trigger evaluation, template selection, queueing, execution, and follow-up events. |

## Data and metadata modeling terms

| Term | Status | Definition |
| --- | --- | --- |
| `Object` | canonical | Conceptual governed data object in the platform. |
| `Obj` | alias | Physical/schema abbreviation for `Object`. |
| `Property` | canonical | Configurable metadata attribute attached to objects. |
| `Prop` | alias | Physical/schema abbreviation for `Property`. |
| `ObjProp` | canonical | Assignment of a property value to an object, including inheritance behavior. |
| `ObjSchema` | canonical | Structural metadata for object columns and key/nullability attributes. |
| `DataContract` | canonical | Agreement between data owner and consumer for usage constraints and delivery conditions. |
| `Delivery window` | canonical | Time interval in which extraction/delivery is allowed. |
| `Allowed frequency` | canonical | Allowed recurrence for extraction/delivery actions. |
| `Allowed purpose` | canonical | Approved business purpose for using a data source. |
| `Logical object` | canonical | Metadata-level object representation independent of physical runtime engine. |
| `Hierarchy` | canonical | Parent-child relationship among objects/containers. |

## Temporal, audit, and control-framework terms

| Term | Status | Definition |
| --- | --- | --- |
| `Historic bitemporal table` | canonical | Pattern combining validity interval with recorded timestamp history. |
| `Valid time` | canonical | Time period in which a record is considered true in business/operations reality. |
| `Recording time` / `recorded_at` | canonical | Timestamp when the platform persisted the record version. |
| `BOT` | canonical | Beginning of time sentinel timestamp (low bound). |
| `EOT` | canonical | End of time sentinel timestamp (high bound). |
| `Audit trail` | canonical | Traceable record of events, state changes, and outcomes. |
| `Lineage` | canonical | Relationship between source inputs, processing steps, and produced outputs. |
| `Restartability` | canonical | Ability to resume processing safely from a known committed state. |
| `Observability` | canonical | Centralized logging, metrics, and alerting for operational visibility. |
| `Exception store` | canonical | Standardized storage for failed or exceptional processing outcomes. |
| `Control plane` | canonical | Metadata/control state layer separate from data payload processing. |
| `Data plane` | canonical | Runtime data processing and movement layer. |
| `SLA` | canonical | Service-level target for freshness, latency, or reliability. |
| `Runbook` | canonical | Operational procedure for incident handling and recovery. |
| `Blast radius` | canonical | Scope of impact from a failure or change. |

## DESL and schema language terms

| Term | Status | Definition |
| --- | --- | --- |
| `DESL` | canonical | Data Engineering Specification Language: declarative intent model for generation/execution adapters. |
| `DBML` | canonical | Database Markup Language used to define schema models. |
| `Declarative` | canonical | Describes what should happen, not imperative execution steps. |
| `Intermediate execution plan` | canonical | Platform-neutral plan compiled from DESL before adapter translation. |
| `Adapter` | canonical | Translator from DESL plan to tool-specific orchestration artifacts. |
| `Platform agnostic` | canonical | Designed to avoid lock-in to one runtime/orchestration platform. |
| `Entity` | canonical | Logical table-level concept in schema modeling. |
| `Attribute` | canonical | Column-level property in an entity/table. |
| `Identifier` | canonical | Key construct such as PK or unique key. |
| `PK` | canonical | Primary key. |
| `FK` | canonical | Foreign key. |
| `Cardinality` | canonical | Relationship multiplicity (one-to-one, one-to-many, etc.). |
| `Nullability` | canonical | Whether a column permits null values. |
| `snake_case` | canonical | Preferred lowercase underscore naming convention for identifiers. |
| `CamelCase` | alias | Mentioned in one guideline section; not preferred for column identifiers. |

## Canonical administration metadata terms

| Term | Status | Definition |
| --- | --- | --- |
| `DE-Admin` | canonical | Canonical administration metadata model for governance, objects, contracts, orchestration, and policies. |
| `de-admin-metadata.schema.json` | canonical | JSON Schema used to validate DE-Admin documents. |
| `de-admin-metadata.example.json` | canonical | Worked example DE-Admin metadata document. |
| `BETL` / `sqldb-betl` | canonical | Concrete control/metadata database implementation used as mapping reference. |
| `logicalObjects[]` | canonical | DE-Admin collection for logical object definitions. |
| `dependencies[]` | canonical | DE-Admin collection for dependency definitions. |
| `transfers[]` | canonical | DE-Admin collection for transfer intent definitions. |
| `orchestration.jobs[]` | canonical | DE-Admin collection for orchestration job definitions. |
| `Batch` | canonical | Runtime grouping/execution context for transfer processing. |
| `Transfer` | canonical | Runtime transfer execution record and status context. |
| `Status` | canonical | Runtime state label for processing entities. |
| `Logging` | canonical | Structured runtime log stream entity. |
| `Error` | canonical | Error record entity for runtime failures. |
| `Obj_map` / `Col_map` / `Transform` | canonical | Mapping/transform implementation entities for source-to-target transformation logic. |
| `rulesRef` / `transformRef` | canonical | References linking metadata definitions to transformation rule assets. |

## Legacy terms found in repository artifacts

| Term | Status | Definition |
| --- | --- | --- |
| `DataObject` | deprecated | Legacy object naming; use `Object`/`Obj`. |
| `DataObjectSchema` | deprecated | Legacy schema-entity naming; use `ObjSchema`. |
| `DataObjectProperty` | deprecated | Legacy property-assignment naming; use `ObjProp`. |
| `Property` (physical table) | deprecated | Legacy physical naming; use `Prop` as table/entity abbreviation. |
| `QueuedTask` | deprecated | Legacy queue item naming; use `QueueItem` concept and `Queue` table. |
| `ControllerCheckpoint` | deprecated | Explicitly blocked by generation guardrails. |
| `IngestionBatchLog` | deprecated | Explicitly blocked by generation guardrails. |
| `IngestionRecordError` | deprecated | Explicitly blocked by generation guardrails. |
| `BitemporalRecord` | deprecated | Explicitly blocked by generation guardrails. |
