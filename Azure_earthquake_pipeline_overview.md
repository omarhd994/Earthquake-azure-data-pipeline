# Earthquake Azure Data Engineering Pipeline 🌍

## Overview and Architecture

I’m building a modular and scalable data pipeline in Azure to automate the ingestion, processing, and analysis of earthquake data. The goal is to turn raw seismic event data into structured insights that can be used by agencies, researchers, and insurance companies.

---

## Why I’m Building This

Earthquake data plays a critical role in understanding seismic activity and preparing for natural disasters. This project helps automate the entire flow from fetching the data to making it ready for reports and dashboards saving time and improving response strategies.

---

## 🏗️ Architecture Overview

I’ve designed the pipeline using key Azure services to ensure performance, flexibility, and maintainability:

- **Data Ingestion**: Azure Data Factory orchestrates the daily fetch from the USGS Earthquake API  
- **Data Processing**: I use Azure Databricks to transform the raw data into structured formats using a medallion architecture  
- **Data Storage**: Azure Data Lake Storage (ADLS Gen2) is where I store the data at each stage (bronze, silver, gold)  
- **Data Analysis**: Azure Synapse Analytics is used for querying and aggregating data  
- **Visualization**: Power BI (or other BI tools) to build dashboards for stakeholders  

---

## 📊 Data Modeling with Medallion Architecture

I’m structuring the pipeline into three layers to separate concerns and improve data quality over time:

- **Bronze Layer**: Raw data as received from the API, stored in Parquet format kept intact for traceability  
- **Silver Layer**: Cleaned and normalized data with duplicates removed and null values handled ready for analytics  
- **Gold Layer**: Aggregated and enriched data (e.g., country codes added) customized for business reporting  

---

## 🔍 Understanding the Earthquake API

The pipeline is built around the [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/), which provides detailed information about seismic events within a specified date range.

- **Start & End Dates**: Set dynamically using Azure Data Factory for automated daily ingestion  
- **Output Format**: GeoJSON  

---

## ✅ Key Benefits of This Project

- **Full Automation**: No more manual data collection or transformation  
- **Scalability**: Built to handle large volumes of earthquake data with Azure services  
- **Insight-Driven**: Outputs structured, ready-to-use datasets that drive real-world decisions  


