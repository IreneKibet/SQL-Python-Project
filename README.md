# SQL-Python-Project

## Order Data Analysis Project

This project involves the analysis of retail order data using SQL and Python. The main objective was to derive meaningful insights from the dataset and demonstrate the use of various data processing and analysis techniques.

### Overview

The analysis process included the following key steps:

- **Data Acquisition**:
  - Downloaded the dataset from Kaggle using the Kaggle API.
  - Extracted the required files from the downloaded archive.

- **Data Preprocessing**:
  - Loaded the dataset into a pandas DataFrame.
  - Handled missing values and standardized column names.
  - Created new columns for discount, sale price, and profit.
  - Converted date columns to appropriate datetime formats.
  - Dropped unnecessary columns to optimize the dataset for analysis.

- **Database Integration**:
  - Created a table in a SQL Server database to store the processed data.
  - Loaded the data from the pandas DataFrame into the SQL Server database.

- **SQL Analysis**:
  - Conducted various SQL queries to extract insights, such as:
    - Top 10 highest revenue-generating products.
    - Top 5 highest-selling products in each region.
    - Month-over-month sales growth comparison for 2022 and 2023.
    - The month with the highest sales for each category.
    - The subcategory with the highest growth in profit from 2022 to 2023.

### Technologies Used

- **Python**: For data preprocessing and integration with the SQL Server database.
- **SQL**: For querying and analyzing the processed data.
- **Pandas**: For data manipulation and cleaning.
- **SQLAlchemy**: For database connection and data loading.

