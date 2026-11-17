from pathlib import Path

from etl.pipeline import run
from etl.sample_data import main as make_sample


def main():
    if not Path("data/raw/records.json").exists():
        make_sample()
    run(source="data/raw/records.json", database_url="sqlite:///data/warehouse.db")
    print("demo complete: data/warehouse.db")


if __name__ == "__main__":
    main()
