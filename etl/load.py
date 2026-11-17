"""Load a dataframe into a SQL warehouse (SQLite by default)."""
import os
import sqlite3

import pandas as pd


def _sqlite_path(database_url: str) -> str:
    if database_url.startswith("sqlite:///"):
        return database_url.replace("sqlite:///", "", 1)
    return database_url


def load(df: pd.DataFrame, table: str = "api_records", database_url: str | None = None) -> int:
    database_url = database_url or os.environ.get("DATABASE_URL", "sqlite:///data/warehouse.db")
    path = _sqlite_path(database_url)
    import pathlib

    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    try:
        df.to_sql(table, con, if_exists="replace", index=False)
    finally:
        con.close()
    return len(df)
