# ObjSchema

Schema metadata table for columns belonging to objects.

## Column definitions

- `obj_schema_id`: Surrogate key for schema metadata row.
- `obj_id`: Reference to object whose schema is described.
- `column_name`: Name of source column.
- `data_type`: Source column type.
- `is_nullable`: Whether source column allows nulls.
- `is_part_of_primary_key`: Whether source column participates in PK.
- `ordinal_position`: Source column order.
