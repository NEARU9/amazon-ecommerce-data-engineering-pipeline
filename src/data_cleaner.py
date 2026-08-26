import pandas as pd


def clean_data(df):
    """
    Clean the raw dataset.
    """

    print("\n" + "=" * 60)
    print("4. DATA CLEANING")
    print("=" * 60)

    df_clean = df.copy()

    # Convert purchase_date
    df_clean["purchase_date"] = pd.to_datetime(
        df_clean["purchase_date"]
    )

    print("✓ purchase_date converted to datetime")

    # Strip whitespace from string columns
    string_columns = (
        df_clean
        .select_dtypes(include=["object"])
        .columns
    )

    for column in string_columns:

        df_clean[column] = (
            df_clean[column]
            .str.strip()
        )

    print(
        f"✓ Whitespace removed from "
        f"{len(string_columns)} string columns"
    )

    return df_clean