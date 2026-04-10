"""Generate and save fake customer transaction data."""

from pathlib import Path
import random

import pandas as pd
from faker import Faker


fake = Faker()

REGIONS = ["North America", "Europe", "Asia", "South America", "Africa"]
PAYMENT_METHODS = ["Credit Card", "PayPal", "Bank Transfer", "Cash"]
STATUSES = ["Completed", "Pending", "Cancelled"]
CATEGORIES = ["Electronics", "Clothing", "Books", "Home", "Sports"]


def generate_transactions(n: int) -> pd.DataFrame:
    """Generate a DataFrame of fake transaction data."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be greater than 0")

    transactions = []
    try:
        for _ in range(n):
            product_price = round(random.uniform(10, 500), 2)
            quantity = random.randint(1, 10)
            transactions.append(
                {
                    "customer": fake.name(),
                    "email": fake.email(),
                    "phone": fake.phone_number(),
                    "region": random.choice(REGIONS),
                    "country": fake.country(),
                    "product": fake.word().title(),
                    "category": random.choice(CATEGORIES),
                    "price": product_price,
                    "quantity": quantity,
                    "total": round(product_price * quantity, 2),
                    "payment_method": random.choice(PAYMENT_METHODS),
                    "status": random.choice(STATUSES),
                    "date": fake.date_this_year(),
                }
            )
    except Exception as exc:
        raise RuntimeError("Failed while generating fake transactions") from exc

    return pd.DataFrame(transactions)


def save_transactions_csv(
    df: pd.DataFrame, output_path: str | Path = "data/fake_transactions.csv"
) -> None:
    """Save generated transactions to CSV."""
    output = Path(output_path)
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output, index=False)
    except (OSError, PermissionError) as exc:
        raise OSError(f"Could not write CSV to {output}") from exc


if __name__ == "__main__":
    try:
        df = generate_transactions(1000)
        save_transactions_csv(df)
        print("Dataset generated successfully.")
    except (TypeError, ValueError) as exc:
        print(f"Input error: {exc}")
    except OSError as exc:
        print(f"File error: {exc}")
    except RuntimeError as exc:
        print(f"Generation error: {exc}")
