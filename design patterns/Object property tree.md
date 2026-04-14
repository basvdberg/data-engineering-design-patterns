# Event based orchestration

## Purpose

## Benefits


## Components

- `Obj`: Registry of data objects and containers involved in orchestration (sources, targets, and hierarchy).
- `DataContract`: Specifies extraction permissions and constraints (owner/consumer, allowed frequency, delivery window, active period).
- `ObjSchema`: Stores structural metadata for objects so orchestration and downstream tasks can validate schema expectations.
- `Prop` and `ObjProp`: Provide flexible, inheritable metadata on objects to support configurable behavior without schema redesign.





