import sqlite3

import pandas as pd
import pytest

from etl.pipeline import run
from etl.sample_data import make
from etl.transform import SchemaError, transform


def test_transform_dedupes_and_lowercases():
    out = transform([{"ID": 1, "Value": 2}, {"ID": 1, "Value": 2}])
    assert list(out.columns) == ["id", "value"]
    assert len(out) == 1


def test_transform_requires_id():
    with pytest.raises(SchemaError):
        transform([{"name": "x"}])


def test_pipeline_loads_sqlite(tmp_path):
    import json

    src = tmp_path / "records.json"
    src.write_text(json.dumps(make(5)))
    db = tmp_path / "wh.db"
    assert run(source=str(src), database_url=f"sqlite:///{db}") == 5
    con = sqlite3.connect(db)
    assert con.execute("SELECT COUNT(*) FROM api_records").fetchone()[0] == 5
    con.close()
