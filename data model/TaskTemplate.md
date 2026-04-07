# TaskTemplate

Reusable orchestration task template definitions for ingestion execution.

## Column definitions

- `task_template_id`: Surrogate key for template row.
- `task_template_name`: Template name.
- `interface_type`: Interface/protocol class used for extraction/loading.
- `task_code`: Executable task logic or reference.
- `retry_max_attempts`: Maximum retry attempts.
- `retry_backoff_seconds`: Delay between retries in seconds.
- `idempotency_key_strategy`: Method ensuring idempotent execution.
- `target_obj_id`: Target object produced/updated by task.
- `is_active`: Active-state flag for template usage.
