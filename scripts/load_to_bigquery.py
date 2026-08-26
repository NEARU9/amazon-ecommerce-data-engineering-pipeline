from google.cloud import bigquery
from google.auth import default
import os
import pandas as pd

# ============================================================
# CONFIGURATION
# ============================================================

PROJECT_ID = "hopeful-adapter-506707-f8"
DATASET_RAW = "data_enggineering_project_01_raw"
DATASET_STAGING = "data_enggineering_project_01_staging"
DATASET_WAREHOUSE = "data_enggineering_project_01_warehouse"

# Local CSV file (sesuai dengan notebook)
CSV_FILE = r"D:\#Portofolio\Amazon Data Engineering Pipeline\data\raw\amazon_ecommerce_1M.csv"

# BigQuery table name (sesuai dengan SQL)
TABLE_RAW = "amazon_raw"


# ============================================================
# LOAD CSV TO BIGQUERY - RAW TABLE
# ============================================================

def load_raw_to_bigquery():
    """Load raw CSV to BigQuery raw table"""
    
    # Check authentication
    credentials, project = default()
    print(f"✅ Authentication successful.")
    print(f"📁 Google Cloud Project: {PROJECT_ID}")

    # Create BigQuery client
    client = bigquery.Client(
        project=PROJECT_ID,
        credentials=credentials
    )

    table_ref = f"{PROJECT_ID}.{DATASET_RAW}.{TABLE_RAW}"

    # Configure CSV loading
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # Overwrite
    )

    print("\n🚀 Starting upload...")
    print(f"📄 File  : {CSV_FILE}")
    print(f"📊 Table : {table_ref}")

    # Check file size
    file_size = os.path.getsize(CSV_FILE) / (1024 * 1024)  # Convert to MB
    print(f"📦 File size: {file_size:.2f} MB")

    if file_size > 100:
        print("\n⚠️  WARNING: File size > 100MB!")
        print("💡 For files > 100MB, use Google Cloud Storage (GCS) instead.")
        print("   See alternative method below.\n")
        
        response = input("Continue with direct upload? (yes/no): ").lower()
        if response != 'yes':
            print("❌ Upload cancelled.")
            return

    # Upload file
    try:
        with open(CSV_FILE, "rb") as source_file:
            load_job = client.load_table_from_file(
                source_file,
                table_ref,
                job_config=job_config,
            )

        # Wait for job to complete
        load_job.result()
        
        # Get table info
        table = client.get_table(table_ref)
        
        print("\n" + "=" * 50)
        print("✅ UPLOAD SUCCESSFUL!")
        print("=" * 50)
        print(f"📊 Table   : {table_ref}")
        print(f"📈 Rows    : {table.num_rows:,}")
        print(f"📋 Columns : {len(table.schema)}")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Alternative: Use GCS method")
        print("   LOAD DATA INTO ... FROM FILES (uris = ['gs://your-bucket/file.csv'])")



# ============================================================
# LOAD STAGING TO BIGQUERY (Alternative)
# ============================================================

def load_staging_to_bigquery(staging_csv_path):
    """Load staging CSV to BigQuery staging table"""
    
    credentials, project = default()
    client = bigquery.Client(project=PROJECT_ID, credentials=credentials)
    
    table_ref = f"{PROJECT_ID}.{DATASET_STAGING}.ecommerce_staging"
    
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )
    
    with open(staging_csv_path, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file,
            table_ref,
            job_config=job_config,
        )
    
    load_job.result()
    table = client.get_table(table_ref)
    
    print(f"✅ Staging loaded: {table.num_rows:,} rows")


# ============================================================
# LOAD WAREHOUSE TABLES TO BIGQUERY
# ============================================================

def load_warehouse_to_bigquery():
    """Load all warehouse dimension and fact tables to BigQuery"""
    
    credentials, project = default()
    client = bigquery.Client(project=PROJECT_ID, credentials=credentials)
    
    # Map table name to CSV file path
    warehouse_files = {
        'dim_user': r'D:\#Portofolio\Amazon Data Engineering Pipeline\data\warehouse\dim_user.csv',
        'dim_product': r'D:\#Portofolio\Amazon Data Engineering Pipeline\data\warehouse\dim_product.csv',
        'dim_seller': r'D:\#Portofolio\Amazon Data Engineering Pipeline\data\warehouse\dim_seller.csv',
        'dim_date': r'D:\#Portofolio\Amazon Data Engineering Pipeline\data\warehouse\dim_date.csv',
        'fact_sales': r'D:\#Portofolio\Amazon Data Engineering Pipeline\data\warehouse\fact_sales.csv',
    }
    
    print("\n🚀 Loading warehouse tables to BigQuery...")
    
    for table_name, csv_path in warehouse_files.items():
        if not os.path.exists(csv_path):
            print(f"⚠️  File not found: {csv_path}")
            continue
            
        table_ref = f"{PROJECT_ID}.{DATASET_WAREHOUSE}.{table_name}"
        
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=True,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        )
        
        with open(csv_path, "rb") as source_file:
            load_job = client.load_table_from_file(
                source_file,
                table_ref,
                job_config=job_config,
            )
        
        load_job.result()
        table = client.get_table(table_ref)
        print(f"✅ {table_name}: {table.num_rows:,} rows")
    
    print("\n✅ All warehouse tables loaded successfully!")


# ============================================================
# LOAD USING GCS (Recommended for large files)
# ============================================================

def load_from_gcs_to_bigquery(gcs_uri):
    """Load data from Google Cloud Storage to BigQuery"""
    
    credentials, project = default()
    client = bigquery.Client(project=PROJECT_ID, credentials=credentials)
    
    table_ref = f"{PROJECT_ID}.{DATASET_RAW}.{TABLE_RAW}"
    
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )
    
    load_job = client.load_table_from_uri(
        gcs_uri,
        table_ref,
        job_config=job_config,
    )
    
    load_job.result()
    table = client.get_table(table_ref)
    
    print(f"✅ Loaded from GCS: {table.num_rows:,} rows")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    
    print("=" * 50)
    print("AMAZON E-COMMERCE DATA LOADER")
    print("=" * 50)
    
    print("\n📋 Available options:")
    print("1. Load raw CSV to BigQuery (direct upload)")
    print("2. Load raw CSV from GCS (for large files)")
    print("3. Load all warehouse tables")
    print("4. Load staging table")
    print("5. Exit")
    
    choice = input("\nSelect option (1-5): ")
    
    if choice == '1':
        load_raw_to_bigquery()
    
    elif choice == '2':
        gcs_uri = input("Enter GCS URI (e.g., gs://bucket/file.csv): ")
        load_from_gcs_to_bigquery(gcs_uri)
    
    elif choice == '3':
        load_warehouse_to_bigquery()
    
    elif choice == '4':
        staging_path = input("Enter staging CSV path: ")
        load_staging_to_bigquery(staging_path)
    
    else:
        print("Exiting...")