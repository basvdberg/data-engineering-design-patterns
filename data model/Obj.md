# Obj

Object repository table that stores hierarchical data and container objects.

## Column definitions

- `obj_id`: Surrogate object identifier.
- `obj_type`: Object class (table, file, schema, database, folder).
- `obj_name`: Logical object name.
- `obj_path`: Qualified object location/path.
- `parent_obj_id`: FK to parent object.
