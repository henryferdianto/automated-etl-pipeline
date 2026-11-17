"""Extract records from a public API with pagination and retries."""
import time
import httpx


def fetch_all(url: str, params: dict | None = None, max_pages: int = 100) -> list[dict]:
    records, page = [], 1
    with httpx.Client(timeout=30) as client:
        while page <= max_pages:
            for attempt in range(3):
                try:
                    resp = client.get(url, params={**(params or {}), "page": page})
                    resp.raise_for_status()
                    break
                except httpx.HTTPError:
                    if attempt == 2:
                        raise
                    time.sleep(2 ** attempt)
            payload = resp.json()
            batch = payload if isinstance(payload, list) else payload.get("results", [])
            if not batch:
                break
            records.extend(batch)
            page += 1
    return records
