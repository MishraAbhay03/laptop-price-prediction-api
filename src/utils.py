import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load dataset from given path"""
    return pd.read_csv(path)


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names"""
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df
