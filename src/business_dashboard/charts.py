"""
`Pandas/plotly chart generation module (pure functions: dataframe in -> go.Figure out, or HTML fragment out)
"""
from transactions_loader import load_transactions_csv

DF = load_transactions_csv()

if __name__ == "__main__" :
    print(DF)