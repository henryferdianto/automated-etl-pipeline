"""Orchestrate extract -> transform -> load."""
import os

from etl.extract import fetch_all
from etl.load import load
from etl.transform import transform


def run(source: str | None = None, database_url: str | None = None) -> int:
    source = source or os.environ.get("SOURCE_API_URL", "data/raw/records.json")
    records = fetch_all(source)
    df = transform(records)
    rows = load(df, database_url=database_url)
    print(f"loaded {rows} rows from {source}")
    return rows


if __name__ == "__main__":
    if not os.path.exists(os.environ.get("SOURCE_API_URL", "data/raw/records.json")):
        from etl.sample_data import main as make_sample

        make_sample()
    run()
