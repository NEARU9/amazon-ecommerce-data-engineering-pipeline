import pandas as pd

from src.config import RAW_FILE


def load_data():
    """
    Load the raw Amazon e-commerce dataset.
    """

    print("=" * 60)
    print("1. DATA LOADING")
    print("=" * 60)

    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw dataset not found: {RAW_FILE}"
        )

    df = pd.read_csv(RAW_FILE)

    print(f"Rows    : {df.shape[0]:,}")
    print(f"Columns : {df.shape[1]}")

    return df