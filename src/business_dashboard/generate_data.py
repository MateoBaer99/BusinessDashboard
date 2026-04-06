"""
generate_data.py

This module generates a fake dataset of customer transactions using Faker and random data.

Main features:
- Generate customer, product, and transaction details
- Save the generated dataset to a CSV file

Dependencies:
- pandas
- faker
- random
- os

Usage:
    from enerate_data import generate_transactions
    df = generate_transactions(1000)
    df.to_csv("data/fake_transactions.csv", index=False)
"""

from faker import Faker
import random
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

fake = Faker()
#values for the columns
REGIONS = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
PAYMENT_METHODS = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash']
STATUSES = ['Completed', 'Pending', 'Cancelled']
CATEGORIES = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']


def generate_transactions(n: int) -> pd.DataFrame:
    """
    Generate a DataFrame of fake transaction data.

    Parameters:
        n (int): Number of transactions to generate.

    Returns:
        pd.DataFrame: Fake transaction dataset.
    """
    transactions = []
    for _ in range(n):  
        product_price = round(random.uniform(10, 500), 2)
        quantity = random.randint(1, 10)
        transactions.append({
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
            "date": fake.date_this_year()
        })

    return pd.DataFrame(transactions)

if __name__ == "__main__":
    df = generate_transactions(1000) # 1000 fake transactions
    df.to_csv("data/fake_transactions.csv", index=False)
