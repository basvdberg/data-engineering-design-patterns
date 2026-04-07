# ObjProp

Link table assigning properties to objects, including inheritance and overrides.

## Column definitions

- `obj_prop_id`: Surrogate key for assignment row.
- `obj_id`: Target object receiving the prop.
- `prop_id`: Referenced prop definition.
- `prop_value`: Effective prop value for the object.
- `inherited_from_obj_id`: Source object where inherited value originated.
- `is_override`: Indicates value overrides inherited/default value.
