# **ETL Pipeline**

## **Project Overview**

This project demonstrates an ETL (Extract, Transform, Load) pipeline.

## **Project Structure**
```
etl-example/
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
├── etl/
│   ├── extract/
│   │   ├── __init__.py
│   │   ├── extract.py
│   ├── load/
│   │   ├── __init__.py
│   │   ├── load.py
│   ├── sql/
│   ├── transform/
│   │   ├── __init__.py
│   │   ├── transform.py
│   └── __init__.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   ├── __init__.py
│   └── run_etl.py
├── tests/
│   ├── __init__.py
├── .env
├── .env.dev
├── .env.test
├── .gitignore
├── README.md
├── requirements-setup.txt
├── requirements.txt
└── setup.py
```

## **Technologies Used**
- **Programming Language:** Python
- **Database:** PostgreSQL
- **Data Sources:**
  - **API:**

- **Python Libraries:**
  - `requests`: For interacting with APIs.
  - `pandas`: For data manipulation and cleaning.
  - `SQLAlchemy`: For database interaction.
  - `numpy`: For numerical computations.
  - `dotenv`: To handle environment variables (API keys, DB credentials).

## **ETL Pipeline Breakdown**

### **1. Data Extraction**
- 
  
### **2. Data Transformation**
- Handle missing data and clean the dataset.
- Create additional features.

### **3. Data Loading**
- Store the cleaned and transformed data into a PostgreSQL database.

### **4. Data Analysis**
- Basic exploratory analysis using SQL queries or in a Jupyter notebook.

## **How to Run the Project**

### **1. Prerequisites**
- **Python** (version 3.7 or above)
- **PostgreSQL** (with database and user access)
- API keys

### **2. Setup Instructions**

1. Clone the repository:
   ```bash
   git clone https://github.com/serena351/df_capstone
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file in the root directory with the following key:
     ```
    API_KEY = <your_api_key>
    DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<dbname>
     ```

5. Set up the PostgreSQL database:
   - Run the SQL script to create the schema:
     ```bash
     psql -U <username> -d <dbname> -f sql/schema.sql
     ```

6. Run the ETL pipeline:
   ```bash
   python src/extract.py
   python src/transform.py
   python src/load.py
   ```

### **3. Running Analysis**
- Explore the data using the provided Jupyter notebook:
  ```bash
  jupyter notebook notebooks/analysis.ipynb
  ```
