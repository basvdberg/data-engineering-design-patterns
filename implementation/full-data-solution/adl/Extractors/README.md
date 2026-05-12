# Extractors

This folder contains the runtime extraction logic for pulling data from
external source systems into the bronze landing zone under `adl/Data/`. Each
sub-folder targets a specific protocol or API type, plus a `common/` folder
for shared utilities.

## Structure

```text
Extractors/
├── __init__.py
├── README.md
├── requirements.txt
├── .gitignore
├── common/                Shared utilities
│   ├── __init__.py
│   ├── config.py          Load and query DWA-style metadata JSON files
│   └── parquet.py         Templated Parquet file writer
├── odata/                 OData v4 extractor
│   ├── __init__.py
│   ├── __main__.py        CLI driver (python -m adl.Extractors.odata)
│   └── client.py          HTTP client — pagination via @odata.nextLink
└── wfs/                   OGC WFS 2.0 extractor
    ├── __init__.py
    ├── __main__.py        CLI driver (python -m adl.Extractors.wfs)
    ├── client.py          HTTP client — GetCapabilities, GetFeature, startIndex pagination
    ├── gml_parser.py      GML 3.2 response parser — flattens XML into tabular records
    └── README.md
```

## Design principles

- **One sub-folder per protocol.** Each extractor is self-contained: a client
  module that handles the HTTP and protocol specifics, plus optional parser
  modules for response formats that need flattening.
- **Config-driven.** Extractors don't hardcode endpoints or table names. They
  read DWA-style JSON mappings from `adl/DataObjectMappings/` which specify the
  connection URL, feature type, output format, page size, and landing path.
- **Parquet output to `adl/Data/`.** Every extractor produces `list[dict]`
  records written to Parquet under the `adl/Data/` directory (gitignored).
- **Runnable as Python modules.** Each extractor has a `__main__.py` so it can
  be invoked with `python -m adl.Extractors.<protocol>` from the
  `full-data-solution/` directory.

## Quickstart

From the `full-data-solution/` directory:

```powershell
pip install -r adl/Extractors/requirements.txt

# OData: smoke test against public Northwind v4 reference
python -m adl.Extractors.odata --config adl/DataObjectMappings/odata-demo.json --mapping odata-demo-regions

# WFS: extract KNMI daily temperature (2 stations, capped at 100 records)
python -m adl.Extractors.wfs --mapping knmi-daggegevens-temperature --page-size 2 --max-features 2 --limit 100
```

Output lands under `adl/Data/bronze/...` as defined by the `landing_path_template`
extension in each mapping JSON.

## Adding a new extractor

1. Create a new sub-folder (e.g. `rest/`, `sftp/`).
2. Add a `client.py` with the protocol-specific fetch logic.
3. Add parser modules if the raw response needs flattening.
4. Expose the public API from the sub-folder's `__init__.py`.
5. Add a `__main__.py` CLI driver.
6. Create a DWA-style mapping JSON in `adl/DataObjectMappings/`.

## Available extractors

| Sub-folder | Protocol | Status |
| --- | --- | --- |
| `odata/` | OData v4 | Implemented — CBS + Northwind demo |
| `wfs/` | OGC WFS 2.0 | Implemented — KNMI INSPIRE daily climate data |
