# DataContract

Contract metadata between data owner and data consumer for source ingestion.

## Column definitions

- `data_contract_id`: Surrogate key for contract row.
- `contract_name`: Human-readable contract name.
- `source_obj_id`: Source object governed by the contract.
- `data_owner`: Owner responsible for granting access.
- `data_consumer`: Consumer allowed to use the data.
- `allowed_purpose`: Allowed business purpose for usage.
- `delivery_window`: Allowed delivery/extraction time window.
- `allowed_frequency`: Allowed extraction frequency.
- `sla_minutes`: SLA for delivery timeliness.
- `active_from_dt`: Contract start timestamp.
- `active_to_dt`: Contract end timestamp.
- `is_active`: Active-state flag.
