# Event

Event log used for change tracking and event-driven orchestration.

## Column definitions

- `event_id`: Unique event identifier.
- `event_dt`: Event timestamp including milliseconds.
- `event_type`: Type of event (Write, Read, InternalProcess, SchemaChange).
- `event_lifecycle`: Event lifecycle (Start, EndSuccessful, EndFailed, InProgress).
- `obj_id`: FK to a known object from Obj (when found).  
- `obj_type`: Type of related object.
- `obj_name`: Name of related object.
- `obj_path`: Path of related object.
- `container_type`: Storage/system technology type.
- `container_name`: Storage/system instance name.
- `increment_identifier`: Increment marker for partitioned/incremental events.
- `record_count`: Record count in event payload.
- `progress_indicator`: Progress value for in-progress events.
