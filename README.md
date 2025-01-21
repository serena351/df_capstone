# **Medium.com ETL Pipeline**

## **Project Overview**

This project demonstrates an ETL (Extract, Transform, Load) pipeline. The data is extracted from the Medium API available on `rapidapi.com`. The goal of this project is to provide insights on user following numbers and their change over time for one of the most popular authors on Medium - Tim Denning.

## **Project Structure**
```
medium_etl/
├── config/
│   ├── __init__.py
│   └── db_config.py
├── data/
│   ├── output/
│   ├── processed/
│   └── raw/
├── docs/
│   └── flowcharts/
│       └── etl_flowchart.md
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   └── etl.py
├── tests/
│   └── __init__.py
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## **Technologies Used**
- **Programming Language:** Python
- **Database:** PostgreSQL
- **Data Source:**
  - **Medium API:**

- **Python Libraries:**
  - `requests`: For interacting with APIs.
  - `pandas`: For data manipulation and cleaning.
  - `sqlalchemy`: For database interaction.
  - `dotenv`: To handle environment variables (API keys, DB credentials).

## **ETL Pipeline Breakdown**

### **1. Data Extraction**
- Article data: article responses, response count, voter count, last modified date and time. 
- User data: followers count.
  
### **2. Data Transformation**
- Handle missing data and clean the dataset.
- Create additional features / add insights.

### **3. Data Loading**
- Store the cleaned and transformed data into the `pagila` PostgreSQL database.

### **4. Data Analysis**
- Basic exploratory analysis using SQL queries or in a Jupyter notebook.

