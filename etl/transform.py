"""Validate and clean extracted records."""
import pandas as pd

REQUIRED = {"id"}


class SchemaError(ValueError):
    pass


def transform(records: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(records)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise SchemaError(f"missing required columns: {missing}")
    df = df.drop_duplicates(subset=["id"]).dropna(how="all")
    df.columns = [c.strip().lower() for c in df.columns]
    return df
