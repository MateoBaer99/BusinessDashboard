"""
generate_dashboard.py

load data, call chart builders, pass HTML snippets to renderer, save file.
"""

from transactions_loader import load_transactions_csv
from pathlib import Path

import pandas as pd

