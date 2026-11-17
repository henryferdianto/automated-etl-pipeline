"""Validate and clean extracted records."""
import pandas as pd

REQUIRED = {"id"}


class SchemaError(ValueError):
    pass


def transform(records: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(records)
    df.columns = [c.strip().lower() for c in df.columns]
    missing = REQUIRED - set(df.columns)
    if missing:
        raise SchemaError(f"missing required columns: {missing}")
    return df.drop_duplicates(subset=["id"]).dropna(how="all")
