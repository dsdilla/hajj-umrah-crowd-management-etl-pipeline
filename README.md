# Hajj and Umrah Crowd Management 2024: Automated ETL Data Pipeline

## 📌 Project Overview
An automated end-to-end ETL (Extract, Transform, Load) data pipeline that 
processes large-scale Hajj and Umrah 2024 crowd management data. The pipeline 
is orchestrated using Apache Airflow and leverages PySpark for efficient 
data processing, Great Expectations for data validation, and MongoDB Atlas 
as the final NoSQL database storage.

## 🎯 Objectives
- Validate raw data quality using Great Expectations (7 Expectations, 0 errors)
- Build modular ETL scripts (Extract, Transform, Load) using PySpark
- Automate pipeline execution with Apache Airflow DAG
- Store clean data into MongoDB Atlas (NoSQL database)

## 🛠️ Tools & Technologies
- **Python** — Core programming language
- **PySpark** — Large-scale data processing and transformation
- **Apache Airflow** — Pipeline orchestration and scheduling (DAG)
- **Great Expectations** — Data validation and quality checks
- **MongoDB Atlas** — NoSQL cloud database storage
- **PyMongo** — MongoDB Python connector
- **Pandas** — Exploratory data analysis
- **Jupyter Notebook / Google Colab** — Development environment

## 🔄 ETL Workflow

### 1. Pre-Automation (Notebook)
- Loaded Hajj & Umrah 2024 Crowd Management Dataset from Kaggle (10,000 rows × 34 columns)
- Performed exploratory data analysis: missing values, duplicates, inconsistency checks
- Validated data using **7 Great Expectations** (all `success: true`):
  - Values to be unique
  - Values to be between min and max
  - Values to be in set
  - Values to be in type list
  - 3 additional custom expectations

### 2. Extract (`Extract.py`)
- Initialized PySpark `SparkSession`
- Loaded raw CSV dataset as a Spark DataFrame

### 3. Transform (`Transform.py`)
- Dropped unnecessary columns (`Unnamed: 0`)
- Removed null/missing rows using PySpark

### 4. Load (`Load.py`)
- Converted Spark DataFrame to Python dictionary
- Connected to **MongoDB Atlas** using PyMongo
- Inserted clean data into `Hajj_Project` database, `p2m3_data_clean` collection

### 5. Orchestration (`DAG.py`)
- Automated pipeline using **Apache Airflow BashOperator**
- Scheduled every **Saturday at 09:10, 09:20, and 09:30 AM**
- DAG run confirmed: **25 successful runs** ✅

## 📁 File Structure
- `P2M3_Dianah Salsha Dilla.ipynb` — Exploratory analysis & Great Expectations notebook
- `Extract.py` — PySpark data extraction script
- `Transform.py` — PySpark data transformation script
- `Load.py` — MongoDB Atlas data loading script
- `P2M3_Dianah_Salsha_Dilla_DAG.py` — Airflow DAG orchestration script
- `P2M3_Dianah_Salsha_Dilla_DAG_graph.jpg` — Screenshot of successful DAG runs
- `P2M3_Dianah_Salsha_Dilla_screenshoot_Mongodb.png` — MongoDB Atlas screenshot
- `P2M3_Dianah_Salsha_Dilla_data_raw.csv` — Raw dataset
