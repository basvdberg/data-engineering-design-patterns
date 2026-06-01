# Data object poller

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Benefits](#benefits)
- [Summary](#summary)
- [Components](#components)
  - [Registry and schedule](#registry-and-schedule)
  - [Change detection](#change-detection)
  - [Poll run and event bus signal](#poll-run-and-event-bus-signal)
  - [Observability](#observability)
  - [Poll flow](#poll-flow)
<!-- markdown-toc:end -->

## Purpose

A data object poller is a lightweight component that checks whether a data object has changed since the last time we looked. It can be used when the system containing the data object does not push change notifications. 

`DataObjectPoller` watches configured objects on a schedule, detects marker changes without reading full payloads, and publishes events for [event-based orchestration](../generic/event-based-orchestration.md). 

## Benefits

- Separates change detection from extraction.
- Avoids redundant full reads when nothing changed.
- **Data object unchanged** events prove the poller ran even when the source is unchanged.
- Records data object changes even when we are not extracting it. This can be usefull for estimating the data object change frequency.

## Summary

The poller maintains a `PollRegistry` and `Schedule`, applies each object's `ChangeDetectionRule`, compares the current marker to `LastKnownState`, records a `PollRun`, and publishes exactly one **data object change** or **data object unchanged** event per completed poll on the event bus.

## Components

### Registry and schedule

`PollRegistry` lists which data objects are monitored; `Schedule` defines when each entry is due.

Examples:
- All enabled leaf objects under a parent container.
- Hourly check for one high-priority object.

### Change detection

`ChangeDetectionRule` defines what counts as a change; `LastChangeMarker` stores the previous marker (timestamp, etag, file name, listing fingerprint).

Examples:
- Compare last-modified metadata to stored value.
- Detect a new file name in a catalog listing.

### Poll run and event bus signal

`PollRun` is one check for one object (identity, timestamps, outcome). Every successful poll emits exactly one bus event:

| Event type | When |
|------------|------|
| **data object change** | Marker differs from previous marker (or no previous marker yet) |
| **data object unchanged** | Marker unchanged — poll succeeded, source quiet |

Downstream triggers react to **data object change** only (for example to queue an extractor task). **Data object unchanged** informs monitoring and audit without starting extraction.

### Observability

`OperationalLog` and `AuditTrail` record due objects, skips, failures, warnings, and who or what initiated the poll.

Examples:
- Scheduled batch: 40 polled, 38 unchanged, 2 change.
- Manual poll referenced by operator id.

### Poll flow

1. Select due objects from the registry per `Schedule`.
2. Probe the source per `ChangeDetectionRule`; compare marker to `LastKnownState`.
3. Publish **data object change** or **data object unchanged** on the event bus.
4. Update `LastKnownState` only when the marker changed and the signal path succeeded.
5. Record the `PollRun` in operational and audit logs.

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
