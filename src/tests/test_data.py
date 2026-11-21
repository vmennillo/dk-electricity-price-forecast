import pandas as pd 
import data

def test_load_or_fetch_uses_cache(tmp_path, monkeypatch):
    monkeypatch.setattr(data, "RAW_DIR", tmp_path)
    calls = []

    def fake_fetch(name, start, end, price_area=None, sort=None, max_retries=3):
        calls.append(1)
        return pd.DataFrame(
            {"HourUTC": ["2025-01-01T00:00:00"], "SpotPriceEUR": [50.0]}
        )

    monkeypatch.setattr(data, "fetch_dataset", fake_fetch)

    first = data.load_or_fetch("Elspotprices", "2025-01-01", "2025-01-02", "DK1")
    second = data.load_or_fetch("Elspotprices", "2025-01-01", "2025-01-02", "DK1")

    assert len(calls) == 1
    assert first.equals(second)