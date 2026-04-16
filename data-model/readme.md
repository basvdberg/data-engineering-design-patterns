# Data Model

## DESL Schema Generation Guardrails

When generating or updating the DESL schema , apply these rules to avoid known mistakes.

1. Do not create the following tables:
   - `ControllerCheckpoint`
   - `BitemporalRecord`
   - `IngestionRecordError`
   - `IngestionBatchLog`
2. Use `Object` as the entity name. Do not use `DataObject` or pluralized forms like `DataObjects`.
3. Abbreviate Object as Obj to simplify naming in table and column names.  
4. Abbreviate Property as Prop to simplify naming in table and column names.  
4. Keep entity naming singular and consistent across table names, key names, and references.
5. All tables use the Historic bitemporal table design pattern
