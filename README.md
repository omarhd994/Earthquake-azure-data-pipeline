# 🌍 Earthquake Azure Data Engineering Pipeline

I've built a complete data engineering pipeline using Azure services. This repository showcases how I designed a scalable and modular pipeline to transform raw earthquake data into actionable insights. It leverages **Azure Data Factory**, **Databricks**, **Azure Data Lake**, and **Synapse Analytics**, following the **Medallion Architecture**.

This project highlights my hands-on experience in automating data ingestion, processing, and analytics for real-world use cases like seismic event tracking, with end-to-end orchestration and transformation.

---

## 🏗️ My Data Architecture

I followed the **Medallion Architecture** approach with three key layers:

### 🔹 Bronze Layer
- **Raw ingestion layer**
- Stores data as-is from the **USGS Earthquake API** in **GeoJSON** format.
- Keeps raw historical records for traceability.
- Data is fetched from the API endpoint:  
  `https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=...`
- Ingestion is orchestrated in **batch mode** using **Azure Data Factory**, which is scheduled to run **daily at midnight**.
- Each run performs an **incremental load**, extracting only earthquake data from the **last 24 hours**, ensuring freshness while optimizing performance and storage.

### 🔸 Silver Layer
- **Cleansed and transformed layer**
- Handles null values, removes duplicates, and applies standard formatting.
- Converts semi-structured fields into a normalized format.

### 🟡 Gold Layer
- **Business-ready layer**
- Data is enriched and aggregated to provide more clarity and usability.
- Using **Databricks with PySpark**, the pipeline applies the **`reverse_geocoder`** Python library to detect the **country code** for each earthquake based on its latitude and longitude.
- This step makes the data more interpretable for downstream analytics by mapping seismic events to countries.

---

## 📖 What I Built

This project includes:

- **Data Architecture Design**  
  Built around Medallion Architecture: Bronze → Silver → Gold.

- **ELT Pipelines**  
  - Ingestion is done in **batch** via **Azure Data Factory**, pulling data from the [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/) on a **daily schedule**.
  - The pipeline is configured to extract data incrementally for the **last 24 hours** only, optimizing data movement and cost.
  - Transformation and enrichment are handled in **Azure Databricks** using **PySpark**, including country identification with `reverse_geocoder`.

- **Data Modeling & Storage**  
  - All data is stored in **Azure Data Lake Storage Gen2** in **Parquet** format.
  - Data is then modeled in **Azure Synapse Analytics** for efficient querying and integration with reporting tools.

- **Automation & Scheduling**  
  - The **ADF pipeline** is fully automated and scheduled to run **every midnight**.
  - Ensures continuous integration of up-to-date earthquake data into the pipeline.

- **Reporting & Visualization**  
  - Final enriched data is exposed via **Power BI dashboards**.
  - Stakeholders can track global seismic activity and trends in near-real time.

---

## 🛠️ Tech Stack

- Azure Data Factory  
- Azure Databricks (PySpark + reverse_geocoder)  
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
