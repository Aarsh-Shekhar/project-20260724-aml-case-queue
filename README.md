# AML Case Queue

Prioritizes synthetic monitoring cases for analysts.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m aml_case_queue.cli --input data/sample_cases.json
```

## Test

```bash
python3 -m unittest discover tests
```
