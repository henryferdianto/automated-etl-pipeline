"""Extract records from a local JSON file or a public API."""
from __future__ import annotations

import json
import time
import urllib.request
from pathlib import Path


def _load_local(path: str) -> list[dict]:
    payload = json.loads(Path(path).read_text())
    return payload if isinstance(payload, list) else payload.get("results", [])


def fetch_all(url: str, params: dict | None = None, max_pages: int = 100) -> list[dict]:
    if not url.startswith(("http://", "https://")):
        return _load_local(url)
    if params:
        query = urllib.parse.urlencode(params)
        sep = "&" if "?" in url else "?"
        url = f"{url}{sep}{query}"
    records, page = [], 1
    while page <= max_pages:
        for attempt in range(3):
            try:
                with urllib.request.urlopen(f"{url}&page={page}", timeout=30) as resp:
                    payload = json.load(resp)
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)
        batch = payload if isinstance(payload, list) else payload.get("results", [])
        if not batch:
            break
        records.extend(batch)
        page += 1
    return records
