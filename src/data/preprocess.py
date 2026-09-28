import os

import pandas as pd

os.makedirs("data/processed", exist_ok=True)
df = pd.read_csv("data/raw/transactions.csv")
df = df.drop_duplicates()
df = df.dropna()
df.to_csv("data/processed/clean.csv", index=False)
print(f"Processed {len(df)} rows")
