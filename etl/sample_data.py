"""Write a local JSON source so the pipeline runs without network access."""
import json
from pathlib import Path


def make(n: int = 20) -> list[dict]:
    return [
        {"id": f"rec-{i:03d}", "name": f"item-{i}", "value": round(i * 1.5, 2)}
        for i in range(n)
    ]


def main() -> Path:
    out = Path("data/raw/records.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(make()))
    print(f"wrote sample records -> {out}")
    return out


if __name__ == "__main__":
    main()
