# **Medium.com ETL Pipeline**

## **Project Overview**

This project demonstrates an ETL (Extract, Transform, Load) pipeline. The data is extracted from the Medium API available on `rapidapi.com`. The goal of this project is to provide insights on user info including follower numbers. In particular, it will look at their change over time for one of the most popular authors on Medium - Tim Denning.

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
├── scripts/
│   ├── testing.py
│   └── etl.py
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## **Technologies Used**
- **Programming Language:** Python
- **Database:** PostgreSQL
- **Data Source:**
  - **Medium API:** [medium-api](https://medium2.p.rapidapi.com/)

- **Python Libraries:**
  - `requests`: For interacting with APIs.
  - `pandas`: For data manipulation and cleaning.
  - `sqlalchemy`: For database interaction.
  - `dotenv`: To handle environment variables (API keys, DB credentials).

## **ETL Pipeline Breakdown**

### **1. Data Extraction**
- User data: followers count at a given time.
  
### **2. Data Transformation**
- Handle any missing data.
- Put in a form ready to be loaded.

### **3. Data Loading**
- Store the cleaned and transformed data into the `pagila` PostgreSQL database.

To deploy the ETL pipeline, run:

```bash
python scripts/etl.py
```
## **Streamlit App**
The app can be accessed at [medium-followers](https://medium-followers.streamlit.app/):
- Get user data by typing in a username of your choice.
- Tim Dennings follower data from ETL pipeline displayed in a chart showing changes over time.
