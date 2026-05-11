# Event-based orchestration

## Table of contents

<!-- toc:start -->
- [Event-based orchestration](#event-based-orchestration)
  - [Table of contents](#table-of-contents)
  - [Purpose](#purpose)
  - [Motivation](#motivation)
  - [Summary](#summary)
  - [Components](#components)
    - [Event](#event)
    - [Trigger](#trigger)
    - [Task](#task)
      - [TaskDefinition](#taskdefinition)
      - [TaskInstance](#taskinstance)
    - [Queue](#queue)
    - [Core event-driven flow](#core-event-driven-flow)
<!-- toc:end -->

## Purpose

Orchestration is the central engine that starts processes to read, transform, and write data. Many processes can run at the same time, and there can be many dependencies between processes, or between a process and external events. This design pattern lets you define these processes, dependencies, and events in a declarative way, making it easier to understand and maintain.

## Motivation

- Maintainability. Because we define orchestration in a declarative way, it is easier to maintain and understand compared to orchestration described in an imperative way (for example, encoded in pipelines or SQL code).
- Scalability. As the data platform grows, more processes and events run simultaneously, requiring more centralized control and visibility. By decoupling process administration from process execution, it becomes easier to scale and define how processes can be executed in parallel.
- Auditability. We need the ability to troubleshoot which events and processes caused data to be read, transformed, or written. This is important for explaining errors and for data-lineage analysis.

## Summary

Events trigger tasks, that are queued for execution. This way we can manage the execution of these tasks. 
E.g. by prioritizing important tasks over less important tasks, manage compute power and manage long running or failing tasks. 

## Components

### Event

The `Event` entity captures every relevant change or process signal that can trigger orchestration. It is the entry point of the pattern and stores the event type, related process lifecycle, identifying attributes of the related data object, and operational metrics.
**Event types:**  
  - File write 
  - Data object incremental update 
  - Data object rewrite
  - Data object delete
  - Data object schema change
  - Processing error   
**Process lifecycle:**
  - Start
  - Success
  - Failed
  - InProgress

Examples:
- A CSV file has finished uploading to a storage container.
- A Delta table was successfully updated with today's increment.
- A schema was changed in a production database that delivers data to us.
- A long-running ingestion emits periodic updates with a progress percentage.
- A network error caused a Parquet file write to be rolled back.
- A process finished transforming raw customer data from system A into curated/integrated data.

### Trigger

A trigger defines routing logic that maps incoming events to executable task templates. Triggers can filter on event type, process lifecycle, and related data object attributes.

Examples:
- A trigger named `trigger_ingest_raw_data_from_blob_container` matches events where data was successfully written to a blob container and routes them to the task `ingest_raw_data_from_blob_container`.
- A trigger named `trigger_transform_curated_data_when_raw_data_arrived` fires when all required raw data has arrived for a curated data object.
- A rule named `alert_on_failed_ingest` matches failure events and routes them to a notification task.

### Task

#### TaskDefinition

A task definition describes the blueprint of a task that is triggered by an event.

#### TaskInstance

A task instance is a concrete instantiation of a task definition for a specific data object, triggered by an event. It links to a trigger and an event and is put into a queue so the queue manager can execute it.

### Queue

This is a list of task instances with additional execution attributes:
- Priority
- Status
- Start timestamp
- Finish timestamp
- Retry count
- Last error message

### Core event-driven flow

1. A source or process emits an `Event`.
2. After an event is registered, a trigger manager evaluates the triggers related to that event. For each trigger, it creates task instances for all objects specified in the trigger and puts them in the queue.
3. A queue manager process runs on a heartbeat, for example every 5 minutes, or earlier when the number of new items in the queue is above a configured queue backlog threshold.

## Project table of contents

<!-- project-toc:start -->
- [Data Engineering Design Patterns](../readme.md)
  - Definitions
    - [Business intelligence](../definitions/business-intelligence.md)
    - [Data engineering](../definitions/data-engineering.md)
  - Design patterns
    - [Data solution](data-solution.md)
    - [Event-based orchestration](event-based-orchestration.md)
    - [Historic bitemporal table](historic-bitemporal-table.md)
    - [Object property tree](object-property-tree.md)
<!-- project-toc:end -->

