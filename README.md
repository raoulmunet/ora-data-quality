# ora-data-quality

[![tests](https://github.com/raoulmunet/ora-data-quality/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-data-quality/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Generate practical Oracle data-quality checks from table DDL.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Supported for generated SQL checks |
> | Oracle Database 23ai | ✅ Supported for generated SQL checks |
> | Oracle AI Database 26ai | ✅ Supported for generated SQL checks |
>
> The generated baseline checks use SQL syntax common to all three releases. Any future rule that depends on a newer Oracle feature will be marked by version in this section.

## What it generates

From common `CREATE TABLE` DDL, the tool proposes two classes of checks:

- **deterministic checks** derived directly from DDL, such as NOT NULL;
- **heuristic candidates** inferred from column names, such as email-like or country-code columns.

Heuristic rules are clearly labelled and should be reviewed before production use.

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-data-quality.git"

ora-data-quality examples/customer.sql
ora-data-quality examples/customer.sql --format json
```

Example DDL:

```sql
CREATE TABLE customer (
  customer_id NUMBER NOT NULL,
  email VARCHAR2(200),
  country_code CHAR(2)
);
```

Example generated checks include:

```sql
SELECT COUNT(*) AS violations
FROM CUSTOMER
WHERE CUSTOMER_ID IS NULL;
```

and candidate checks for email / country-code shape.

## Philosophy

The tool never claims that a name-based heuristic is a business rule. It generates reviewable candidates, with a rationale and confidence class.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
