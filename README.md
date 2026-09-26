# ora-data-quality

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

## License

MIT.
