# Tool choice for a data warehouse orchestration tool

## Table of contents

<!-- markdown-toc:start -->
- [Purpose](#purpose)
- [Top-level functionalities](#top-level-functionalities)
  - [1. Workflow orchestration](#1-workflow-orchestration)
  - [2. Execution model](#2-execution-model)
  - [3. Connectivity and network](#3-connectivity-and-network)
  - [4. Data movement and transformation](#4-data-movement-and-transformation)
  - [5. Metadata and schema handling](#5-metadata-and-schema-handling)
  - [6. Security and governance](#6-security-and-governance)
  - [7. Operations and observability](#7-operations-and-observability)
  - [8. Platform and engineering fit](#8-platform-and-engineering-fit)
- [Scoring legend](#scoring-legend)
- [Tool scoring matrix](#tool-scoring-matrix)
- [Self-built option (from scratch)](#self-built-option-from-scratch)
- [Interpretation notes](#interpretation-notes)
- [Recommendation](#recommendation)
<!-- markdown-toc:end -->

## Purpose

This document helps select a data warehouse orchestration tool, ETL tool, ELT tool, workflow orchestrator, pipeline engine, or data integration platform.

## Top-level functionalities

These are the top-level capabilities that matter when selecting a data warehouse orchestration or ETL tool.

### 1. Workflow orchestration

- Event-driven triggering
- Time-based scheduling
- Dependency management
- Parallelism and fan-out/fan-in
- Retry, timeout, and failure handling
- Replay, resume, and backfill support

### 2. Execution model

- Custom code execution
- Support for Python, SQL, Spark, shell, or containers
- Stateful or stateless runtime support
- Distributed execution
- Batch, micro-batch, or streaming support

### 3. Connectivity and network

- Broad connector support across files, object stores, APIs, RDBMS, SaaS tools, queues, and lakehouse platforms
- Custom connector development
- Credential and secret management
- Support for managed identity, service principals, OAuth, API keys, and certificates
- Private endpoints
- VNet or VPC integration
- Hybrid and on-premise connectivity
- Protocol support such as `HTTPS`, `SFTP`, `FTPS`, `JDBC`, `ODBC`, `REST`, and storage APIs
- Proxy, DNS, TLS, firewall, and allowlist support

### 4. Data movement and transformation

- Read and write support for common data formats
- Bulk load and unload
- Incremental loading
- CDC support
- Upsert and merge behavior
- Pushdown and partition-aware processing
- In-engine transformation or external compute integration

### 5. Metadata and schema handling

- Schema discovery
- Schema drift handling
- Parameterization and templating
- Reusable components
- Data lineage and metadata integration

### 6. Security and governance

- Role-based access control
- Audit logging
- Encryption in transit and at rest
- Policy enforcement
- Environment separation
- Compliance support

### 7. Operations and observability

- Logging and monitoring
- Alerting
- Run history
- Failure diagnostics
- SLA and freshness monitoring
- Cost visibility

### 8. Platform and engineering fit

- Managed versus self-hosted options
- CI/CD and infrastructure-as-code support
- API and SDK quality
- Extensibility
- Community and documentation maturity
- Total cost of ownership
- Team skill fit

## Scoring legend

- `++` = very good
- `+` = good
- `+/-` = moderate or mixed
- `-` = weak
- `--` = very weak

For cost rows, fewer euro signs means lower cost:

- `€` = very favorable
- `€€` = favorable
- `€€€` = moderate or mixed
- `€€€€` = unfavorable
- `€€€€€` = very unfavorable

## Tool scoring matrix

| Functionality | `Temporal` | `Azure Durable Functions` | `Dagster` | `Apache Airflow` | `Self-built` | `Azure Data Factory` / `Fabric Data Factory` | `AWS Step Functions` | `Google Cloud Workflows` | `Informatica IDMC` | `Snowflake` (Tasks/Streams/Dynamic Tables) | `dbt Cloud` | `Fivetran` | `Matillion` | `Azure Databricks Workflows` | `AWS Glue` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Workflow orchestration | `++` | `+` | `+` | `+` | `+/-` | `+` | `+` | `+/-` | `+` | `+/-` | `+/-` | `-` | `+/-` | `+` | `+` |
| Execution model flexibility | `+` | `+` | `+` | `+` | `++` | `+/-` | `+/-` | `-` | `+/-` | `+/-` | `+/-` | `--` | `+/-` | `++` | `+` |
| Connectivity and network | `+/-` | `+/-` | `+` | `+` | `+` | `++` | `+/-` | `-` | `++` | `+/-` | `+/-` | `++` | `+` | `+/-` | `+` |
| Data movement and transformation | `+/-` | `+/-` | `+` | `+` | `+` | `++` | `-` | `-` | `++` | `+` | `+` | `+/-` | `+` | `++` | `+` |
| Metadata and schema handling | `-` | `-` | `+` | `+/-` | `+/-` | `+` | `--` | `--` | `+` | `+` | `+` | `+/-` | `+/-` | `+/-` | `+/-` |
| Security and governance | `+` | `+` | `+` | `+/-` | `+/-` | `+` | `+` | `+/-` | `+` | `+` | `+/-` | `+` | `+/-` | `+` | `+` |
| Operations and observability | `++` | `+` | `+` | `+` | `-` | `+` | `+` | `+/-` | `+` | `+/-` | `+` | `+` | `+/-` | `+` | `+` |
| Platform and engineering fit | `+/-` | `+` | `+` | `+` | `+/-` | `+` | `+` | `+/-` | `+/-` | `+/-` | `+` | `+` | `+/-` | `+` | `+` |
| Open source | `Partial` | `No` | `Partial` | `Yes` | `Partial` | `No` | `No` | `No` | `No` | `No` | `Partial` | `No` | `No` | `No` | `No` |
| Engineering cost | `€€€€` | `€€€` | `€€€` | `€€€€` | `€€€€€` | `€€` | `€€` | `€€` | `€€` | `€€` | `€€` | `€` | `€€` | `€€€` | `€€€` |
| Infrastructure + license cost | `€€€` | `€€` | `€€€` | `€€€` | `€€` | `€€€` | `€€` | `€€` | `€€€€` | `€€€€` | `€€€` | `€€€€` | `€€€€` | `€€€€` | `€€€` |

## Self-built option (from scratch)

Recommended stack when building an orchestration tool yourself:

- **Primary language:** `Python` for control plane, task definitions, and connectors.
- **Optional secondary language:** `SQL` for transformations, and optionally `Scala`/`PySpark` for heavy Spark workloads.

Recommended Python libraries by concern:

- **API and control plane:** `FastAPI`, `Pydantic`, `Uvicorn`.
- **Workflow and scheduling primitives:** `APScheduler` (basic scheduling), `Celery` or `RQ` (distributed task execution).
- **Queues and events:** `Redis`, `RabbitMQ`, or `Kafka` clients (`redis`, `pika`, `confluent-kafka`).
- **Database and metadata store:** `SQLAlchemy`, `Alembic`, and a relational backend like PostgreSQL.
- **Connectivity and I/O:** `pandas`, `polars`, `pyarrow`, `duckdb`, `fsspec`, `adlfs`, `s3fs`, `gcsfs`.
- **RDBMS connectors:** `psycopg`, `pyodbc`, `pymssql`, `mysqlclient`/`pymysql`, plus JDBC/ODBC drivers where needed.
- **Lakehouse and table formats:** `deltalake` (delta-rs), `pyiceberg` (if Iceberg is needed), Spark APIs for advanced operations.
- **Data quality and contracts:** `great_expectations` or `pandera`.
- **Observability:** `structlog` (or stdlib logging), `prometheus_client`, `opentelemetry-sdk`.
- **Security and secrets:** cloud secret SDKs (`azure-keyvault-secrets`, `boto3` + Secrets Manager, `google-cloud-secret-manager`) and `cryptography`.
- **Testing and reliability:** `pytest`, `pytest-asyncio`, `tenacity` (retry), `hypothesis` (optional property-based tests).

Minimum architecture guidance:

1. Use `FastAPI` + PostgreSQL for orchestration metadata, run history, and state.
2. Use a queue-backed worker layer (`Celery` + Redis/RabbitMQ) for task execution.
3. Isolate connector logic in pluggable adapters per source type (blob files, RDBMS, APIs, lakehouse).
4. Add first-class idempotency keys, retry policy, dead-letter handling, and structured logging from day one.
5. Add secrets integration and private networking support before production rollout.

## Interpretation notes

- `Temporal` is strongest for complex workflow orchestration, but it is not a connector-rich ETL engine by itself.
- `Temporal` and `Dagster` are available in open-source form, but managed/commercial offerings are also common.
- `Self-built` is only partially open source in this matrix because Python libraries may be open, while some tooling around development may be commercial.
- `Azure Durable Functions` is strong when you are Azure-first and are willing to implement source connectivity in code.
- `Dagster` is a strong code-first choice when orchestration is closely tied to data assets and Python-based data engineering.
- `Apache Airflow` is often one of the best fits when broad source and target integration matters.
- `Self-built` can score well on flexibility, but operational maturity depends entirely on the quality of the custom implementation.
- `Azure Data Factory` / `Fabric Data Factory` is one of the strongest options when built-in connectors, network integration, and direct data movement are core requirements.
- `AWS Step Functions` and `Google Cloud Workflows` are useful orchestration services, but they are weaker as full ETL or broad data integration platforms.
- `Informatica IDMC`, `Fivetran`, and `Matillion` are strong on ready-made connectivity and lower engineering effort, but tend to have higher license costs.
- `Snowflake` and `dbt Cloud` are strong when your center of gravity is SQL-first analytics engineering, and they are commonly paired with ingestion and orchestration tools.
- `Azure Databricks Workflows` and `AWS Glue` are strong when your transformations are Spark-centric and aligned with their respective cloud ecosystems.

## Recommendation

For this use case (event-based orchestration plus broad connectivity across files, blob storage, RDBMS, and lakehouse):

1. **Primary recommendation:** choose `Apache Airflow` when you want a strong balance between connector breadth, orchestration power, and open-source flexibility.
2. **If you are Microsoft-first and prefer managed services:** choose `Azure Data Factory` / `Fabric Data Factory`.
3. **If your workloads are heavily Spark-based:** choose `Azure Databricks Workflows` (Azure) or `AWS Glue` (AWS).
4. **If reliability of long-running workflows is the top priority:** choose `Temporal`, and pair it with dedicated worker services for data I/O.
5. **If your center of gravity is already in Snowflake and transformations are SQL-first:** choose `Snowflake` (Tasks, Streams, Dynamic Tables), and pair it with an external ingestion tool for broader source connectivity.
6. **If you need fastest time-to-value with minimal engineering effort:** consider `Informatica IDMC` or `Fivetran`, accepting higher license costs.

## Project structure

<!-- markdown-project-structure:start -->
- [Data Engineering Design Patterns](../../readme.md)
  - Definitions
    - [Business intelligence](../../definitions/business-intelligence.md)
    - [Data engineering](../../definitions/data-engineering.md)
  - Design patterns
    - [Data solution](../../design-patterns/data-solution.md)
    - [Event-based orchestration](../../design-patterns/event-based-orchestration.md)
    - [Historic bitemporal table](../../design-patterns/historic-bitemporal-table.md)
    - [Data object property tree](../../design-patterns/object-property-tree.md)
    - [Separate what and how](../../design-patterns/separate-what-and-how.md)
  - Implementation
    - Event Based Orchestration
      - [Event-based orchestration architecture](architecture.md)
      - [Azure event-based orchestration architecture](azure-architecture.md)
      - [Tool choice for a data warehouse orchestration tool](tool-choice.md)
<!-- markdown-project-structure:end -->
