---
uid: design-pattern-generic-control-framework
---

# Design Pattern - Generic - Control Framework

> [!WARNING]
> This design pattern is a placeholder awaiting content

## Purpose

This Design Pattern describes the reasoning for, and functionality provided by, a control framework for data logistics.

## Motivation

Data solutions rely on predictable, restartable, and auditable processing. Without a common control framework, individual pipelines implement their own tracking, leading to inconsistent failure handling, gaps in auditability, and higher operational cost. A shared control framework centralizes state, logging, alerting, and restart semantics so every pipeline behaves consistently.

## Applicability

This pattern is only applicable for _every_ process in the data solution.

## Structure

The control framework typically provides:

* **Orchestration and state**: job definitions, dependencies, run states, and restart markers to guarantee idempotent runs.
* **Audit and lineage**: capture of row counts, checksums, timestamps, source/target identifiers, and lineage links for traceability.
* **Exception handling hooks**: standard outcomes for continue/reject/abort, plus routing into exception stores.
* **Observability**: centralized logging, metrics, and alerts for SLA tracking and incident response.
* **Access control**: role-based access for operators, developers, and auditors.

## Implementation guidelines

* Standardize job metadata (run id, batch/window, source/target, row counts, checksums) and persist it per load.
* Enforce restartability: every step should be idempotent and able to resume from the last committed state using the control metadata.
* Define clear outcomes (success, partial with exceptions, failed) and route exceptions to a common store with enough detail to remediate.
* Provide SLA tracking and alerting on latency, freshness, and failures; avoid bespoke alert logic per job.
* Separate control-plane storage from data-plane storage to reduce blast radius and simplify recovery.
* Keep the framework technology-agnostic where possible so it can front multiple data logistics/ELT engines.

## Considerations and consequences

* A control framework adds upfront implementation effort but reduces long-term operational toil.
* Centralization creates a dependency; design for high availability and clear fallback/runbook procedures.
* Excessive coupling to a specific engine or scheduler reduces portability; keep interfaces minimal and documented.

## Related patterns

* [Design Pattern - Generic - Using checksums](xref:design-pattern-generic-using-checksums).

## Canonical administration metadata (DE-Admin)

This repository defines a **single JSON document** that captures governance, logical data objects, contracts, connections, datasets, declarative ingest/transform intent, orchestration jobs, event-driven policies, and the control-framework concerns above. It is intended to be **declarative** (what to administer and how runs must be controlled), not imperative execution logic.

| Artifact | Purpose |
| --- | --- |
| `de-admin-metadata.schema.json` | JSON Schema (draft 2020-12); validate before codegen or catalog load |
| `de-admin-metadata.example.json` | Worked example aligned with the sales ingest / integrate flow in `readme.md` |

### Mapping to BETL (`sqldb-betl`)

The [BETL `sqldb-betl`](https://github.com/basvdberg/BETL/tree/main/sqldb-betl) project implements a concrete control and metadata database. The DE-Admin schema maps conceptually as follows:

| DE-Admin concept | BETL table(s) (conceptual) |
| --- | --- |
| `logicalObjects[]` | `Obj` (+ `static.Obj_type`, `static.Server_type`) |
| `dependencies[]` | `Obj_dep` |
| `transfers[]` | Definition-level counterpart to runtime `Transfer` (src/tgt objects + measures policy) |
| `orchestration.jobs[]` | `Job`, `Job_schedule`, `Job_step` (use `capability` + `targetRef` instead of embedding SSIS commands in the canonical doc) |
| Runtime batch / transfer execution | `Batch`, `Transfer`, `Status` |
| Errors | `Error` |
| Structured log stream | `Logging` (+ `static.Log_level`, `static.Log_type`) |
| Extensible properties per object | `Property_value` (+ `static.Property`) |
| Source/target column mapping at transform time | `Obj_map`, `Col_map`, `Transform` (implementation detail; keep references in `transformations` via `rulesRef` / `transformRef`) |

Implementations may **materialize** a validated DE-Admin document into BETL rows, or **generate** orchestration artifacts (ADF, Airflow, etc.) while persisting run state in BETL-compatible tables.