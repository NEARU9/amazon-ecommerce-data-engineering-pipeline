# Amazon E-Commerce Data Engineering Pipeline

An end-to-end data engineering portfolio project that processes an Amazon e-commerce dataset from raw CSV data into a structured analytical data warehouse using Python, Pandas, and Google BigQuery.

The project demonstrates the fundamental stages of a data engineering workflow, including data loading, profiling, data quality validation, cleaning, transformation, data modeling, and data warehouse loading.

---

## 📋 Project Overview

This project uses an Amazon e-commerce dataset as the source data.

The objective is to build a reproducible data pipeline that transforms raw transactional data into a structured star schema consisting of dimension tables and a fact table.

The processed datasets are stored locally as CSV files and can then be loaded into Google BigQuery as a cloud data warehouse.

---

## 🏗️ Data Engineering Workflow

The project follows these main stages:

```text
Raw CSV Data
     |
     v
1. Data Loading
     |
     v
2. Data Profiling
     |
     v
3. Data Quality Validation
     |
     v
4. Data Cleaning
     |
     v
5. Data Transformation
     |
     v
6. Data Modeling
     |
     v
7. Data Warehouse
     |
     v
Google BigQuery