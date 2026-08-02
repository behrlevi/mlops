import pandas as pd


def load_data(path: str = "data/raw/transactions.csv") -> pd.DataFrame:
    """Load raw data from a CSV file."""
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates and null values."""
    df = df.drop_duplicates()
    df = df.dropna()
    return df
