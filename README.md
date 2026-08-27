# Amazon E-Commerce Data Engineering Pipeline

An end-to-end data engineering portfolio project that processes an Amazon e-commerce dataset from raw CSV data into a structured analytical data warehouse using Python, Pandas, and Google BigQuery.

The project demonstrates the fundamental stages of a data engineering workflow, including data loading, profiling, data quality validation, cleaning, transformation, data modeling, and data warehouse loading.

---

## 📋 Project Overview

This project uses an Amazon e-commerce dataset as the source data.

The objective is to build a reproducible data pipeline that transforms raw transactional data into a structured star schema consisting of dimension tables and a fact table.

The processed datasets are stored locally as CSV files and can then be loaded into Google BigQuery as a cloud data warehouse.

---

## 📊 Dataset

This project uses the **Amazon E-Commerce Dataset** with 1,000,000 transaction records.

### Data Sources

| Source | Link | Description |
|--------|------|-------------|
| **Kaggle (Original)** | [Amazon E-Commerce Dataset](https://www.kaggle.com/datasets/sharmajicoder/amazon-e-commerce/data) | Original raw dataset (20 columns) |
| **Google Drive (Processed)** | [Processed Dataset](https://drive.google.com/file/d/1k1WXrUTdVjUDP6RV6NdRlXBmlCzjEUGH/view?usp=drive_link) | Cleaned and transformed dataset (34 columns), ready for staging |

### Dataset Information

- **Total Rows:** 1,000,000
- **Total Columns:** 20 (raw) / 34 (processed)
- **File Size:** ~130 MB
- **Format:** CSV
- **Date Range:** 2024-03-31 to 2026-03-31

> **Note:** The dataset is not stored in this repository due to GitHub's file size limit (25 MB per file). Please download from the links above.

---

## 🏗️ Data Engineering Workflow

The project follows these main stages:

```text

 Raw CSV Data
      |
      v
1.  Data Loading
      |
      v
2.  Data Profiling
      |
      v
3.  Data Quality Validation
      |
      v
4.  Data Cleaning
      |
      v
5.  Data Transformation
      |
      v
6.  Data Modeling
      |
      v
7.  Data Warehouse
      |
      v
8.  Google BigQuery
      |
      v
9.  Power BI
      |
      v
10. Analytics Dashboard
