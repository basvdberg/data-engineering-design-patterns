# ADL — Agnostic Data Labs

Agnostic Data Labs (ADL) is a metadata-driven code-generation tool for data
teams. Instead of hand-writing repetitive SQL, ETL scripts, or deployment
artefacts for every table, you define your metadata once, pair it with
templates, and generate everything you need.

Full documentation: <https://docs.agnosticdatalabs.com/docs/>

## How it works

ADL is built around three ideas:

1. **Metadata — describe what you have.**
   Define your data connections (where data lives), data objects (tables, views,
   queries), and how they relate through mappings. All metadata is stored as
   plain JSON files using an open-source schema — no proprietary format, no
   database, just files in your repository.

2. **Templates — describe what you want.**
   Templates are written in Handlebars and define the output to generate: SQL
   `CREATE TABLE` statements, stored procedures, documentation pages, deployment
   scripts, etc. ADL ships with a library of ready-made templates for common
   patterns, and you can author your own.

3. **Output — generate and deploy.**
   Combining metadata with templates produces output files — SQL scripts, docs,
   config files — one per mapped metadata object. The generated files land in
   your repository, ready to be reviewed, committed, and deployed through your
   normal CI/CD pipeline.

## Folder layout in this project

```text
adl/
├── Classifications/         Tag-based labels applied to data objects
├── Configurations/          Project-level ADL configuration
├── Connections/             Data connection definitions (sources, targets)
├── Conventions/             Naming conventions and standards
├── DataObjects/             Table / view / query definitions (one JSON per object)
│   ├── 000_Source/
│   ├── 100_Landing_Area/
│   └── 150_Persistent_Staging_Area/
├── DataObjectMappings/      Source-to-target mappings that drive code generation
│   ├── PersistentStaging/
│   └── Staging/
├── Data/                    Extracted data landing zone (gitignored)
│   └── bronze/              Raw Parquet files from source extractors
├── Extractors/              Runtime extraction logic (Python), by protocol
│   ├── common/              Shared utilities (config loader, Parquet writer)
│   ├── odata/               OData v4 HTTP client + CLI driver
│   └── wfs/                 OGC WFS 2.0 client + GML parser + CLI driver
├── Output/                  Generated artefacts (SQL, scripts, docs)
├── Perspectives/            Custom views / filters over the metadata
├── Schemas/                 JSON Schema definitions for the metadata format
├── Settings/                ADL application settings
└── Templates/               Handlebars templates for code generation
```

## Why ADL?

- **Save time** — stop writing the same SQL patterns for every table.
- **Stay consistent** — every script generated from the same template follows
  the same standards.
- **Stay flexible** — metadata and templates are plain files; no vendor lock-in.
- **Work with any platform** — SQL Server, Snowflake, PostgreSQL, and more.
- **Evolve with confidence** — need to change a pattern across 200 tables?
  Update the template and regenerate.

## Reference

- [ADL Documentation](https://docs.agnosticdatalabs.com/docs/)
- [Schema Reference](https://docs.agnosticdatalabs.com/docs/schema-reference/dwa-model/)
- [Sample Designs](https://docs.agnosticdatalabs.com/docs/sample-designs/overview/)
