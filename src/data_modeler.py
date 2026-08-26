def create_star_schema(df_clean):

    print("\n" + "=" * 60)
    print("6. DATA MODELING - STAR SCHEMA")
    print("=" * 60)

    # ========================================================
    # DIM USER
    # ========================================================

    dim_user = (
        df_clean[
            [
                "user_id",
                "location",
                "device"
            ]
        ]
        .drop_duplicates("user_id")
        .reset_index(drop=True)
    )

    dim_user.insert(
        0,
        "user_key",
        range(1, len(dim_user) + 1)
    )

    print(f"✓ dim_user: {len(dim_user):,} rows")

    # ========================================================
    # DIM PRODUCT
    # ========================================================

    dim_product = (
        df_clean[
            [
                "product_id",
                "category",
                "subcategory",
                "brand"
            ]
        ]
        .drop_duplicates("product_id")
        .reset_index(drop=True)
    )

    dim_product.insert(
        0,
        "product_key",
        range(1, len(dim_product) + 1)
    )

    print(
        f"✓ dim_product: "
        f"{len(dim_product):,} rows"
    )

    # ========================================================
    # DIM SELLER
    # ========================================================

    dim_seller = (
        df_clean[
            [
                "seller_id",
                "seller_rating",
                "seller_rating_category"
            ]
        ]
        .drop_duplicates("seller_id")
        .reset_index(drop=True)
    )

    dim_seller.insert(
        0,
        "seller_key",
        range(1, len(dim_seller) + 1)
    )

    print(
        f"✓ dim_seller: "
        f"{len(dim_seller):,} rows"
    )

    # ========================================================
    # DIM DATE
    # ========================================================

    dim_date = (
        df_clean[
            [
                "purchase_date",
                "purchase_year",
                "purchase_month",
                "purchase_month_name",
                "purchase_quarter",
                "purchase_day",
                "purchase_day_name"
            ]
        ]
        .drop_duplicates("purchase_date")
        .sort_values("purchase_date")
        .reset_index(drop=True)
    )

    dim_date.insert(
        0,
        "date_key",
        range(1, len(dim_date) + 1)
    )

    print(
        f"✓ dim_date: "
        f"{len(dim_date):,} rows"
    )

    # ========================================================
    # FACT SALES
    # ========================================================

    fact_sales = df_clean[
        [
            "user_id",
            "product_id",
            "seller_id",
            "purchase_date",
            "price",
            "discount",
            "discount_amount",
            "final_price",
            "revenue",
            "rating",
            "review_count",
            "stock",
            "shipping_time_days",
            "shipping_category",
            "payment_method",
            "device",
            "delivery_status",
            "is_returned",
            "return_flag",
            "delivered_flag",
            "delayed_flag"
        ]
    ].copy()

    # ========================================================
    # REPLACE NATURAL IDs WITH SURROGATE KEYS
    # ========================================================

    fact_sales = fact_sales.merge(
        dim_user[
            ["user_key", "user_id"]
        ],
        on="user_id",
        how="left"
    )

    fact_sales = fact_sales.merge(
        dim_product[
            ["product_key", "product_id"]
        ],
        on="product_id",
        how="left"
    )

    fact_sales = fact_sales.merge(
        dim_seller[
            ["seller_key", "seller_id"]
        ],
        on="seller_id",
        how="left"
    )

    fact_sales = fact_sales.merge(
        dim_date[
            ["date_key", "purchase_date"]
        ],
        on="purchase_date",
        how="left"
    )

    # ========================================================
    # FINAL FACT TABLE
    # ========================================================

    fact_sales = fact_sales[
        [
            "user_key",
            "product_key",
            "seller_key",
            "date_key",
            "price",
            "discount",
            "discount_amount",
            "final_price",
            "revenue",
            "rating",
            "review_count",
            "stock",
            "shipping_time_days",
            "shipping_category",
            "payment_method",
            "device",
            "delivery_status",
            "is_returned",
            "return_flag",
            "delivered_flag",
            "delayed_flag"
        ]
    ]

    fact_sales.insert(
        0,
        "sales_key",
        range(1, len(fact_sales) + 1)
    )

    print(
        f"✓ fact_sales: "
        f"{len(fact_sales):,} rows"
    )

    return {
        "dim_user": dim_user,
        "dim_product": dim_product,
        "dim_seller": dim_seller,
        "dim_date": dim_date,
        "fact_sales": fact_sales
    }