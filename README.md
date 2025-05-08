# 🌍 Earthquake Azure Data Engineering Pipeline

I've built a complete data engineering pipeline using Azure services. This repository showcases how I designed a scalable and modular pipeline to transform raw earthquake data into actionable insights. It leverages **Azure Data Factory**, **Databricks**, **Azure Data Lake**, and **Synapse Analytics**, following the **Medallion Architecture**.

This project highlights my hands-on experience in automating data ingestion, processing, and analytics for real-world use cases like seismic event tracking, with end-to-end orchestration and transformation.

---

## 🏗️ My Data Architecture

I followed the **Medallion Architecture** approach with three key layers:

### 🔹 Bronze Layer
- **Raw ingestion layer**
- Stores data as-is from the **USGS Earthquake API** (GeoJSON format) in **Parquet** format.
- Keeps raw historical records for traceability.

### 🔸 Silver Layer
- **Cleansed and transformed layer**
- Handles nulls, removes duplicates, and standardizes the dataset.
- Prepares the data for analytical processing.

### 🟡 Gold Layer
- **Business-ready layer**
- Data is enriched with additional attributes (e.g., country codes) and aggregated.
- Designed for fast querying, dashboarding, and reporting.

---

## 📖 What I Built

This project includes:

- **Data Architecture Design**  
  Built around Medallion Architecture: Bronze → Silver → Gold.

- **ELT Pipelines**  
  Automated using **Azure Data Factory** for ingestion and **Databricks** for transformation.

- **Data Modeling & Storage**  
  Processed and stored in **Azure Data Lake Storage (ADLS Gen2)** and modeled in **Synapse Analytics**.

- **Automation & Scheduling**  
  **ADF** pipelines run daily to fetch and load new data dynamically.

- **Reporting & Visualization**  
  **Power BI dashboards** ready to connect to **Synapse** for stakeholder reporting.

---

## 🛠️ Tech Stack

- Azure Data Factory  
- Azure Databricks (PySpark)  
- Azure Data Lake Storage Gen2  
- Azure Synapse Analytics  
- Power BI  
- Git/GitHub  

---

## 🎯 Why This Project Matters

This project demonstrates my capabilities as a:

- 🔁 ELT Pipeline Developer  
- 📊 Data Modeler  
- 🧠 PySpark Developer  
- ⚙️ Cloud Data Engineer  
- 📈 Analytics-Oriented Engineer  

Whether you're a recruiter, hiring manager, or data enthusiast, I hope this project shows how I solve real-world data problems using modern cloud tools.


![pipe](https://github.com/user-attachments/assets/b06ef2d5-38de-4a46-8cc6-edd39485fb01)

