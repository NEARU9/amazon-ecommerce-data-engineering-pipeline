def transform_data(df_clean):
    """
    Transform cleaned data and create derived columns.
    """

    print("\n" + "=" * 60)
    print("5. DATA TRANSFORMATION")
    print("=" * 60)

    df_clean = df_clean.copy()

    # ========================================================
    # DATE ATTRIBUTES
    # ========================================================

    df_clean["purchase_year"] = (
        df_clean["purchase_date"].dt.year
    )

    df_clean["purchase_month"] = (
        df_clean["purchase_date"].dt.month
    )

    df_clean["purchase_month_name"] = (
        df_clean["purchase_date"]
        .dt.month_name()
    )

    df_clean["purchase_quarter"] = (
        df_clean["purchase_date"].dt.quarter
    )

    df_clean["purchase_day"] = (
        df_clean["purchase_date"].dt.day
    )

    df_clean["purchase_day_name"] = (
        df_clean["purchase_date"]
        .dt.day_name()
    )

    print("✓ Date attributes created")

    # ========================================================
    # REVENUE & DISCOUNT
    # ========================================================

    df_clean["discount_amount"] = (
        df_clean["price"]
        - df_clean["final_price"]
    )

    df_clean["revenue"] = (
        df_clean["final_price"]
    )

    print("✓ Revenue and discount_amount created")

    # ========================================================
    # SHIPPING CATEGORY
    # ========================================================

    def classify_shipping(days):

        if days <= 2:
            return "Fast"

        elif days <= 4:
            return "Standard"

        else:
            return "Slow"

    df_clean["shipping_category"] = (
        df_clean["shipping_time_days"]
        .apply(classify_shipping)
    )

    # ========================================================
    # RATING CATEGORY
    # ========================================================

    def classify_rating(rating):

        if rating < 3:
            return "Low"

        elif rating < 4:
            return "Medium"

        else:
            return "High"

    df_clean["rating_category"] = (
        df_clean["rating"]
        .apply(classify_rating)
    )

    df_clean["seller_rating_category"] = (
        df_clean["seller_rating"]
        .apply(classify_rating)
    )

    print("✓ Rating and shipping categories created")

    # ========================================================
    # FLAGS
    # ========================================================

    df_clean["return_flag"] = (
        df_clean["is_returned"]
        .astype(int)
    )

    df_clean["delivered_flag"] = (
        df_clean["delivery_status"]
        == "Delivered"
    ).astype(int)

    df_clean["delayed_flag"] = (
        df_clean["delivery_status"]
        == "Delayed"
    ).astype(int)

    print("✓ Return, delivered, and delayed flags created")

    print(
        f"\nFinal transformed shape: "
        f"{df_clean.shape[0]:,} rows × "
        f"{df_clean.shape[1]} columns"
    )

    return df_clean