from generate_dashboards import generate_dashboards

def main():
    df = generate_dashboards()
    print(df.head())

if __name__ == "__main__":
    main()
