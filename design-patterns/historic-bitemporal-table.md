# Historic bitemporal table

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Definitions](#definitions)
  - [Valid time](#valid-time)
  - [Recording time](#recording-time)
  - [Synonyms](#synonyms)
  - [BOT and EOT](#bot-and-eot)
- [Assumptions](#assumptions)
  - [The always valid assumption](#the-always-valid-assumption)
  - [Latest knowledge assumption](#latest-knowledge-assumption)
- [Summary](#summary)
- [Components](#components)
  - [Primary key and payload](#primary-key-and-payload)
  - [Valid time](#valid-time)
  - [Recording time](#recording-time)
  - [Read views](#read-views)
  - [Core bitemporal flow](#core-bitemporal-flow)
    - [Example](#example)
<!-- markdown-toc:end -->

## Purpose

A historic bitemporal table stores both valid time and recording time. Instead
of updating rows in place, each change is captured as a new row so we can
reconstruct what was valid at a given business time and what was known in the
system at a given recording time.

## Benefits

- Auditability. Every change is preserved, making it possible to explain how and when data changed.
- Historic reporting. It is always possible to reproduce a derived fact. For
  example, report monthly sales as seen on the first day of the next month,
  instead of recalculating that same month with today's knowledge.
- Time-travel analysis. Consumers can query both "what is valid now" and "what
  was valid at a chosen point in time."
- Data correction support. Late-arriving or corrected records can be appended without destructive updates.
- Traceability. Recording time and validity intervals make source-to-target reconciliation easier.

## Definitions

### Valid time 
This is the time period during which a fact is true in the modeled reality —
independent of when that fact was recorded in the database. It represents the
real-world timeline and is typically supplied by the business or source system.

**Example:** An employee's salary change is effective from 1 January, regardless
of when HR entered it into the system.

**Sources:**
- Snodgrass, R.T. & Ahn, I. (1985). *A taxonomy of time in databases.* ACM SIGMOD Record, 14(4), 236–246.
- ISO/IEC 9075 (SQL:2011) — introduced native valid time (PERIOD FOR) support.
- Date, C.J., Darwen, H. & Lorentzos, N. (2002). *Temporal Data and the Relational Model.* Morgan Kaufmann.

### Recording time

Recording time is the time period during which a fact is stored and considered
current in the database. It is system-generated, immutable, and reflects when the
database "knew" something — regardless of when it was true in reality. 

**Example:** HR entered the salary change on January 10; the transaction time
starts at that moment and cannot be altered retroactively.

**Sources:**
- Snodgrass, R.T. (1999). *Developing Time-Oriented Database Applications in SQL.* Morgan Kaufmann. (freely available at cs.arizona.edu)
- ISO/IEC 9075 (SQL:2011) — introduced native transaction time (SYSTEM_TIME) support.
- Jensen, C.S. & Snodgrass, R.T. (1999). *Temporal data management.* IEEE Transactions on Knowledge and Data Engineering, 11(1), 36–44.

**Quick mapping**
- *Valid time*: when something was true in the real world (approximately positing time).
- *Recording time*: when something was recorded in the database (approximately asserting time).

Both valid time and recording time are source-system dependent. A fact can be
recorded at a different time in the source system than in the data warehouse,
and valid times in the warehouse can also differ after standardization or
correction.

### Synonyms
| Concept | Synonyms |
|---|---|
| **Valid time** | Positing time, effective time, business time, real-world time, event time |
| **Recording time** | Transaction time, asserting time, load time, system time, record time, audit time, LDTS (load date timestamp) |

### BOT and EOT

`BOT` (beginning of time) and `EOT` (end of time) are fixed boundary timestamps
used for open intervals, for example `1900-01-01` and `2099-01-01`. Fixed
timestamps are preferred over nulls because they simplify temporal predicates
and range comparisons.

## Assumptions  

### The always valid assumption
Unless the data tells us otherwise, a record is considered always valid. This
results in a `valid_from_dt` equal to `BOT` and a `valid_to_dt` equal to `EOT`.

### Latest knowledge assumption
By default, it is assumed that a user always wants to see what is valid according to the latest knowledge. This means that we want to see the record with a max recording timestamp. So although we record two time dimensions, the recording time dimension is rarely used. 

Examples where recording time is used:
- To troubleshoot why and when a value changed.
- To freeze historic reports by disregarding late-arriving changes. For
  example, report customer base at the beginning of each month for the previous
  month, while ignoring updates recorded after the report timestamp.

## Summary

Each primary key keeps a sequence of non-overlapping valid intervals, and every interval version is recorded with its own recording timestamp.

## Components

### Primary key and payload

The table contains:
- A stable business key (`bk`) that identifies the real-world entity.
- A payload (descriptive attributes) that may change over time.
- Temporal metadata (`valid_from_dt`, `valid_to_dt`, `recorded_dt`) used to
  track both business validity and database knowledge.

### Valid time

The time when a fact is true in the modeled domain (business reality).

`valid_from_dt` and `valid_to_dt` define the interval in which the payload is
considered true from a business perspective.

Rules:
- For a single business key, valid intervals may not overlap.
- A newly inserted record usually starts with an open-ended interval (`BOT` to
  `EOT`) unless a specific interval is known (the always valid assumption).

### Recording time
The time when a statement about a fact is recorded in the database.

`recorded_dt` stores this time, meaning when the version was asserted by the
platform. A single timestamp is sufficient because it defines the start of a
recording-time interval. The interval ends at the next chronological version for
the same business key with a higher `recorded_dt`; if no later version exists,
the interval is considered open-ended (valid untill EOT).

### Read views

- Valid-now view. Returns records where `CURRENT_TIMESTAMP` is within `[valid_from_dt, valid_to_dt)`. This is the default view.
- Point-in-time view. Returns records where a supplied timestamp is within `[valid_from_dt, valid_to_dt)`.
- As-recorded view (optional). Returns records as they were known at a given
  recording timestamp.

### Core bitemporal flow

1. Insert the first version for a business key with `valid_from_dt = BOT`,
   `valid_to_dt = EOT`, and `recorded_dt = now()`.
2. When a change occurs at timestamp `t`, close the active row by setting
   `valid_to_dt = t`.
3. Insert a new row with `valid_from_dt = t`, `valid_to_dt = EOT`, and
   `recorded_dt = now()`.

#### Example

At `2026-01-01 09:00`, we insert:

| id | value | valid_from_dt | valid_to_dt | recorded_dt |
| --- | --- | --- | --- | --- |
| 1 | A | 1900-01-01 | 2099-01-01 | 2026-01-01 09:00 |

At `2026-02-01 10:00`, value changes from `A` to `B`:

| id | value | valid_from_dt | valid_to_dt | recorded_dt |
| --- | --- | --- | --- | --- |
| 1 | A | 1900-01-01 | 2026-02-01 10:00 | 2026-01-01 09:00 |
| 1 | B | 2026-02-01 10:00 | 2099-01-01 | 2026-02-01 10:00 |

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
