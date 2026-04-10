"""
transactions_loader.py

Helpers for loading the generated transaction CSV into pandas.
"""

from pathlib import Path

import pandas as pd


DEFAULT_CSV_PATH = Path(__file__).resolve().parent / "data" / "fake_transactions.csv"


def load_transactions_csv(csv_path: str | Path = DEFAULT_CSV_PATH) -> pd.DataFrame:
    """Load the transactions CSV into a pandas DataFrame."""
    return pd.read_csv(Path(csv_path))


def generate_dashboards(csv_path: str | Path = DEFAULT_CSV_PATH) -> pd.DataFrame:
    """Backward-friendly entrypoint that returns the loaded dashboard data."""
    return load_transactions_csv(csv_path)
