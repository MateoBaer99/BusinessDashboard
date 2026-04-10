from transactions_loader import load_transactions_csv


def main():
    df = load_transactions_csv()
    print(df.head())


if __name__ == "__main__":
    main()
