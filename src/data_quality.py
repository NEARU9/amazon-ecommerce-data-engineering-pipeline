import pandas as pd


def profile_data(df):
    """
    Perform basic data profiling.
    """

    print("\n" + "=" * 60)
    print("2. DATA PROFILING")
    print("=" * 60)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nDataset Information:")
    df.info()

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nLast 5 Rows:")
    print(df.tail())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    categorical_columns = [
        "category",
        "subcategory",
        "brand",
        "device",
        "payment_method",
        "delivery_status"
    ]

    for col in categorical_columns:

        print(f"\n--- {col} ---")

        print("Unique values:", df[col].nunique())

        print(
            df[col]
            .value_counts()
            .head(10)
        )


def validate_data(df):
    """
    Perform data quality validation.
    """

    print("\n" + "=" * 60)
    print("3. DATA QUALITY VALIDATION")
    print("=" * 60)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nData types:")
    print(df.dtypes)

    df["purchase_date"] = pd.to_datetime(
        df["purchase_date"]
    )

    print("\n✓ purchase_date validated")

    return df