# QueuedTask

Execution queue table for tasks created from incoming events.

## Column definitions

- `queued_task_id`: Surrogate key for queued task row.
- `source_event_id`: Event that created the task.
- `task_template_id`: Template executed by this task.
- `task_status`: Current execution state.
- `priority`: Queue priority used by scheduler.
- `expected_capacity`: Capacity units consumed by task.
- `late_time_seconds`: Delay between expected and actual arrival.
- `queued_dt`: Time task entered queue.
- `started_dt`: Time execution started.
- `finished_dt`: Time execution finished.
- `retry_count`: Number of retries performed.
- `error_message`: Last error details.
