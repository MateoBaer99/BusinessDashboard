from faker import Faker
import random
import pandas as pd

fake = Faker()
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash']
statuses = ['Completed', 'Pending', 'Cancelled']
categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']

transactions = []

for _ in range(1000):  # 1000 fake transactions
    product_price = round(random.uniform(10, 500), 2)
    quantity = random.randint(1, 10)
    transactions.append({
        "customer": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "region": random.choice(regions),
        "country": fake.country(),
        "product": fake.word().title(),
        "category": random.choice(categories),
        "price": product_price,
        "quantity": quantity,
        "total": round(product_price * quantity, 2),
        "payment_method": random.choice(payment_methods),
        "status": random.choice(statuses),
        "date": fake.date_this_year()
    })

df = pd.DataFrame(transactions)

df.to_csv("data/fake_transactions.csv", index=False)