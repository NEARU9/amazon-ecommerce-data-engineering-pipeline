from pathlib import Path

# ============================================================
# PROJECT CONFIGURATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DIR = DATA_DIR / "raw"
STAGING_DIR = DATA_DIR / "staging"
WAREHOUSE_DIR = DATA_DIR / "warehouse"

RAW_FILE = RAW_DIR / "amazon_ecommerce_1M.csv"

STAGING_FILE = STAGING_DIR / "ecommerce_staging.csv"

WAREHOUSE_FILES = {
    "dim_user": WAREHOUSE_DIR / "dim_user.csv",
    "dim_product": WAREHOUSE_DIR / "dim_product.csv",
    "dim_seller": WAREHOUSE_DIR / "dim_seller.csv",
    "dim_date": WAREHOUSE_DIR / "dim_date.csv",
    "fact_sales": WAREHOUSE_DIR / "fact_sales.csv",
}

# Create directories
RAW_DIR.mkdir(parents=True, exist_ok=True)
STAGING_DIR.mkdir(parents=True, exist_ok=True)
WAREHOUSE_DIR.mkdir(parents=True, exist_ok=True)