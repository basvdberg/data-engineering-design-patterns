# Schema Definition Language Creator

## Goal

Define a language to define database schemas that adhere to the following principles:
1. Platform agnostic. The language should not have any platform-specific dependencies. 
2. It should have enough expressiveness to be used by agents to generate a database schema in any platform.
3. Human readable

The language should describe:

1. entities (tables)
2. attributes (columns and types)
3. identifiers (PKs, unique keys)
4. relationships (FKs and cardinality)
5. constraints (nullability, checks, defaults)
6. optional physical hints (partitioning, clustering, comments)

## Definition 

### Language
Use Database Markup Language (DBML) 

### Naming Convention

1. Use singular names.
2. Prefer short names over long names.
3. Use lowercase snake_case for all identifiers.
4. Prefer base nouns/adjectives; avoid verb forms where unnecessary (for example `record_dt` instead of `recorded_dt`).
5. Avoid negation in boolean names (`is_finished` instead of `is_not_running`).
6. Do not use spaces, hyphens, or special characters.
7. Avoid SQL reserved words (for example `user`, `order`, `group`, `table`).

### Tables

1. Use CamelCase pattern: `<BusinessEntity>` (singular, descriptive)
2. Examples:
   - `customer`
   - `sales_order`
   - `ingestion_task_template`

### Columns

1. use lowercase snake_case. 
1. Primary key pattern: `<table_name>_id`
2. Foreign key pattern: `<referenced_table_name>_id`
3. Timestamp suffixes:
   - `*_dt` for timestamps (`created_dt`, `update_dt`)
   - `*_date` for dates (`delivery_date`)
5. Boolean prefix:
   - `is_*` or `has_*` (`is_active`, `has_errors`)
6. Avoid redundant prefixes in columns when table context already provides meaning.

### Constraints and index naming

1. Primary key: `pk_<table_name>`
2. Foreign key: `fk_<child_table>_<parent_table>`
3. Unique: `uq_<table_name>_<column_or_group>`
4. Index: `idx_<table_name>_<column_or_group>`

### Rationale

1. `snake_case` is broadly used and portable across engines.
2. Lowercase identifiers reduce quoting and case-sensitivity issues (especially relevant for PostgreSQL).
3. Singular table names align with entity-oriented modeling and keep naming predictable.
4. Explicit key and constraint patterns improve readability and enable deterministic code generation by agents.

