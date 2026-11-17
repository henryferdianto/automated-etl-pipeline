"""Load a dataframe into a SQL warehouse (upsert on primary key)."""
import os
from sqlalchemy import create_engine, text
import pandas as pd


def load(df: pd.DataFrame, table: str = "api_records") -> int:
    engine = create_engine(os.environ["DATABASE_URL"])
    with engine.begin() as conn:
        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id TEXT PRIMARY KEY
            )
        """))
    df.to_sql(table, engine, if_exists="append", index=False, method="multi")
    return len(df)
