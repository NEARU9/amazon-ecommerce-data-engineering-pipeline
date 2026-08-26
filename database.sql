-- ============================================================
-- AMAZON E-COMMERCE DATA ENGINEERING PROJECT
-- Project: data_enggineering_project_01
-- Platform: Google BigQuery
-- Project ID: hopeful-adapter-506707-f8
-- ============================================================

-- ============================================================
-- 1. CREATE DATASETS
-- ============================================================

-- Buat dataset untuk raw data (sesuai dengan Python script)
CREATE SCHEMA IF NOT EXISTS `hopeful-adapter-506707-f8.data_enggineering_project_01_raw`;

-- Dataset untuk staging
CREATE SCHEMA IF NOT EXISTS `hopeful-adapter-506707-f8.data_enggineering_project_01_staging`;

-- Dataset untuk warehouse (star schema)
CREATE SCHEMA IF NOT EXISTS `hopeful-adapter-506707-f8.data_enggineering_project_01_warehouse`;


-- ============================================================
-- 2. RAW TABLE (Data mentah dari CSV)
-- ============================================================

CREATE TABLE IF NOT EXISTS
`hopeful-adapter-506707-f8.data_enggineering_project_01_raw.amazon_raw`
(
    user_id STRING,
    product_id STRING,
    category STRING,
    subcategory STRING,
    brand STRING,
    price FLOAT64,
    discount FLOAT64,
    final_price FLOAT64,
    rating FLOAT64,
    review_count INT64,
    stock INT64,
    seller_id STRING,
    seller_rating FLOAT64,
    purchase_date DATE,
    shipping_time_days INT64,
    location STRING,
    device STRING,
    payment_method STRING,
    is_returned BOOL,
    delivery_status STRING
);


-- ============================================================
-- 3. STAGING TABLE (Data setelah cleaning & transformation)
-- ============================================================

CREATE TABLE IF NOT EXISTS
`hopeful-adapter-506707-f8.data_enggineering_project_01_staging.ecommerce_staging`
(
    user_id STRING,
    product_id STRING,
    category STRING,
    subcategory STRING,
    brand STRING,
    price FLOAT64,
    discount FLOAT64,
    final_price FLOAT64,
    rating FLOAT64,
    review_count INT64,
    stock INT64,
    seller_id STRING,
    seller_rating FLOAT64,
    purchase_date DATE,
    shipping_time_days INT64,
    location STRING,
    device STRING,
    payment_method STRING,
    is_returned BOOL,
    delivery_status STRING,
    purchase_year INT64,
    purchase_month INT64,
    purchase_month_name STRING,
    purchase_quarter STRING,
    purchase_day INT64,
    purchase_day_name STRING,
    revenue FLOAT64,
    discount_amount FLOAT64,
    shipping_category STRING,
    rating_category STRING,
    seller_rating_category STRING,
    return_flag INT64,
    delivered_flag INT64,
    delayed_flag INT64
);


-- ============================================================
-- 4. DIMENSION: USER
-- ============================================================

CREATE TABLE IF NOT EXISTS
`hopeful-adapter-506707-f8.data_enggineering_project_01_warehouse.dim_user`
(
    user_key INT64,
    user_id STRING,
    location STRING,
    device STRING
);


-- ============================================================
-- 5. DIMENSION: PRODUCT
-- ============================================================

CREATE TABLE IF NOT EXISTS
`hopeful-adapter-506707-f8.data_enggineering_project_01_warehouse.dim_product`
(
    product_key INT64,
    product_id STRING,
    category STRING,
    subcategory STRING,
    brand STRING
);


-- ============================================================
-- 6. DIMENSION: SELLER
-- ============================================================

CREATE TABLE IF NOT EXISTS
`hopeful-adapter-506707-f8.data_enggineering_project_01_warehouse.dim_seller`
(
    seller_key INT64,
    seller_id STRING,
    seller_rating FLOAT64,
    seller_rating_category STRING
);


-- ============================================================
-- 7. DIMENSION: DATE
-- ============================================================

CREATE TABLE IF NOT EXISTS
`hopeful-adapter-506707-f8.data_enggineering_project_01_warehouse.dim_date`
(
    date_key INT64,
    full_date DATE,
    year INT64,
    month INT64,
    month_name STRING,
    quarter STRING,
    day INT64,
    day_name STRING
);


-- ============================================================
-- 8. FACT TABLE: SALES
-- ============================================================

CREATE TABLE IF NOT EXISTS
`hopeful-adapter-506707-f8.data_enggineering_project_01_warehouse.fact_sales`
(
    sales_key INT64,
    user_key INT64,
    product_key INT64,
    seller_key INT64,
    date_key INT64,
    price FLOAT64,
    discount FLOAT64,
    discount_amount FLOAT64,
    final_price FLOAT64,
    revenue FLOAT64,
    rating FLOAT64,
    review_count INT64,
    stock INT64,
    shipping_time_days INT64,
    shipping_category STRING,
    rating_category STRING,
    location STRING,
    device STRING,
    payment_method STRING,
    is_returned BOOL,
    delivery_status STRING,
    return_flag INT64,
    delivered_flag INT64,
    delayed_flag INT64
);


-- ============================================================
-- 9. LOAD DATA FROM GCS (Alternatif untuk file > 100MB)
-- ============================================================

-- Cara 1: Load dari Google Cloud Storage (Rekomendasi untuk file besar)
-- Upload CSV ke GCS dulu, lalu jalankan query ini

LOAD DATA INTO `hopeful-adapter-506707-f8.data_enggineering_project_01_raw.amazon_raw`
FROM FILES (
    uris = ['gs://your-bucket-name/amazon_ecommerce_1M.csv'],
    format = 'CSV',
    skip_leading_rows = 1,
    autodetect = TRUE
);


-- ============================================================
-- 10. VERIFY DATA
-- ============================================================

-- Cek jumlah data di raw table
SELECT COUNT(*) AS total_rows 
FROM `hopeful-adapter-506707-f8.data_enggineering_project_01_raw.amazon_raw`;

-- Cek sample data
SELECT * 
FROM `hopeful-adapter-506707-f8.data_enggineering_project_01_raw.amazon_raw` 
LIMIT 10;