# ControllerRule

Routing rules that map incoming events to executable task templates.

## Column definitions

- `controller_rule_id`: Surrogate key for rule row.
- `rule_name`: Rule name.
- `filter_event_type`: Optional filter for event type.
- `filter_event_status`: Optional filter for event status.
- `filter_obj_type`: Optional filter for object type.
- `filter_obj_name`: Optional filter for object name.
- `filter_obj_path`: Optional filter for object path.
- `filter_container_type`: Optional filter for container type.
- `filter_container_name`: Optional filter for container name.
- `task_template_id`: Task template to run on match.
- `priority`: Rule processing priority.
- `is_active`: Active-state flag.
