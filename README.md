# End-to-End Automated ETL Data Pipeline & Live BI Reporting

> **Scheduled API ingestion, validation, warehouse load and zero-touch dashboards**

## Overview

An automated Extract-Transform-Load pipeline that ingests real-time public API datasets, validates and cleans records, loads them into PostgreSQL/MySQL, and powers live dashboards via scheduled GitHub Actions.

## Approach

1. **Extract** from public APIs with pagination and retries.
2. **Transform** with schema validation and data cleaning.
3. **Load** into a relational warehouse (PostgreSQL/MySQL).
4. **Orchestrate** with GitHub Actions on a schedule.
5. **Report** through Power BI / Looker Studio connected to the warehouse.

## Repository Structure

```
automated-etl-pipeline/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
├── .github/workflows/etl.yml
├── .env.example
├── requirements.txt
└── README.md
```

## Tech Stack

`Python` · `httpx` · `pandas` · `SQLAlchemy` · `PostgreSQL` · `GitHub Actions`

## Getting Started

```bash
git clone https://github.com/henryferdianto/automated-etl-pipeline.git
cd automated-etl-pipeline
pip install -r requirements.txt
```

```bash
cp .env.example .env   # set DATABASE_URL
python -m etl.pipeline
```

## Project Status

This repository contains the project documentation and a runnable implementation
skeleton. Scripts are structured so that each pipeline stage can be executed and
extended independently. Update the configuration and data paths to run against
your own datasets.

## License

MIT License — see [LICENSE](LICENSE).


---

**Author:** Rifky Henry Ferdianto — Data Science undergraduate at ITERA  
GitHub: [@henryferdianto](https://github.com/henryferdianto) · Portfolio: [rifky-henry-ferdianto](https://github.com/henryferdianto/rifky-henry-ferdianto)
