"""Orchestrate extract -> transform -> load."""
import os
from .extract import fetch_all
from .transform import transform
from .load import load


def run() -> int:
    url = os.environ.get("SOURCE_API_URL", "https://api.example.com/records")
    records = fetch_all(url)
    df = transform(records)
    rows = load(df)
    print(f"loaded {rows} rows")
    return rows


if __name__ == "__main__":
    run()
