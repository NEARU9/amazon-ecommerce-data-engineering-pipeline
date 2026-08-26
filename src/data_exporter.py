from src.config import (
    STAGING_FILE,
    WAREHOUSE_FILES
)


def save_to_csv(df_clean, star_schema):

    print("\n" + "=" * 60)
    print("7. SAVE DATA")
    print("=" * 60)

    # ========================================================
    # STAGING
    # ========================================================

    df_clean.to_csv(
        STAGING_FILE,
        index=False
    )

    print(
        f"✓ Staging saved: "
        f"{STAGING_FILE}"
    )

    # ========================================================
    # DIMENSION TABLES
    # ========================================================

    for name in [
        "dim_user",
        "dim_product",
        "dim_seller",
        "dim_date"
    ]:

        table = star_schema[name]

        filepath = WAREHOUSE_FILES[name]

        table.to_csv(
            filepath,
            index=False
        )

        print(
            f"✓ {name} saved: "
            f"{filepath}"
        )

    # ========================================================
    # FACT TABLE
    # ========================================================

    fact_sales = star_schema["fact_sales"]

    fact_sales.to_csv(
        WAREHOUSE_FILES["fact_sales"],
        index=False
    )

    print(
        f"✓ fact_sales saved: "
        f"{WAREHOUSE_FILES['fact_sales']}"
    )

    print("\n✓ All data exported successfully.")