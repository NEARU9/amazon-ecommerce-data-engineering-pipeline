from src.data_loader import load_data
from src.data_quality import (
    profile_data,
    validate_data
)
from src.data_cleaner import clean_data
from src.data_transformer import transform_data
from src.data_modeler import create_star_schema
from src.data_exporter import save_to_csv


def run_pipeline():

    print("=" * 60)
    print("AMAZON E-COMMERCE DATA PIPELINE")
    print("=" * 60)

    # ========================================================
    # 1. DATA LOADING
    # ========================================================

    df = load_data()

    # ========================================================
    # 2. DATA PROFILING
    # ========================================================

    profile_data(df)

    # ========================================================
    # 3. DATA QUALITY VALIDATION
    # ========================================================

    df = validate_data(df)

    # ========================================================
    # 4. DATA CLEANING
    # ========================================================

    df_clean = clean_data(df)

    # ========================================================
    # 5. DATA TRANSFORMATION
    # ========================================================

    df_clean = transform_data(df_clean)

    # ========================================================
    # 6. DATA MODELING
    # ========================================================

    star_schema = create_star_schema(df_clean)

    # ========================================================
    # 7. SAVE DATA
    # ========================================================

    save_to_csv(
        df_clean,
        star_schema
    )

    # ========================================================
    # SUMMARY
    # ========================================================

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print(
        f"\nTransactions : "
        f"{len(star_schema['fact_sales']):,}"
    )

    print(
        f"Users        : "
        f"{len(star_schema['dim_user']):,}"
    )

    print(
        f"Products     : "
        f"{len(star_schema['dim_product']):,}"
    )

    print(
        f"Sellers      : "
        f"{len(star_schema['dim_seller']):,}"
    )

    print(
        f"Dates        : "
        f"{len(star_schema['dim_date']):,}"
    )

    return df_clean, star_schema


if __name__ == "__main__":
    run_pipeline()