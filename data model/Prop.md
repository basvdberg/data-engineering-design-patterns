# Prop

Prop dictionary for normalized object property definitions.

## Column definitions

- `prop_id`: Surrogate key for prop definition.
- `prop_name`: Unique prop name.
- `data_type`: Expected property value type.
- `root_obj_type`: Root object type where prop inheritance starts.
- `levels_deep`: Inheritance depth for prop propagation. -1 for all levels, 0 for no inheritance. 
