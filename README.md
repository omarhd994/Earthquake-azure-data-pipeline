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
- Ingestion is orchestrated in **batch mode** using **Azure Data Factory**, which is scheduled to pull the latest earthquake data from the API at regular intervals.

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
  Ingestion is done in **batch** via **Azure Data Factory**, pulling data from the **USGS Earthquake API** on a defined schedule. Transformation is handled in **Azure Databricks** using PySpark.

- **Data Modeling & Storage**  
  Processed data is stored in **Azure Data Lake Storage Gen2** and modeled in **Azure Synapse Analytics** for advanced querying.

- **Automation & Scheduling**  
  Data ingestion is fully automated and scheduled to run periodically via **ADF**, ensuring continuous integration of fresh data into the pipeline.

- **Reporting & Visualization**  
  The refined, gold-layer data is connected to **Power BI dashboards** for real-time stakeholder insights and reporting.

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
![Captura de pantalla 2025-05-08 153521](https://github.com/user-attachments/assets/c9fadc95-18ab-4ecc-a5e5-5bebf4671885)
