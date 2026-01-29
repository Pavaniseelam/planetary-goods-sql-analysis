# Planetary Goods SQL Analysis Project

## Project Overview
This project analyzes sales and customer data from the Planetary Goods dataset using SQL and Python.  
The goal is to answer real business questions such as top-selling products, premium customers, and product demand.

## Tools Used
- MySQL
- Python
- MySQL Connector
- VS Code
- Git & GitHub

## Project Structure
planetarygoods_project/
├── sql/
│   └── analysis_queries.sql
├── src/
│   ├── db_connection.py
│   └── run_analysis.py
├── output/
│   └── query_results
└── README.md

## SQL Analysis Performed
- Total sales per product
- Top 3 best-selling products
- Customers with total orders over $1000
- Product sales with product names
- Total quantity ordered per product including products never ordered
- Customers living in the same city

## Automation Using Python
Python is used to:
- Connect to the MySQL database
- Execute SQL queries automatically
- Fetch and display results in the terminal

This removes the need to manually run queries in MySQL Workbench and demonstrates basic automation skills.

## How to Run the Project
1. Update database credentials in `db_connection.py`
2. Run the analysis script


## What I Learned
- Writing optimized SQL queries using joins and aggregations
- Automating database queries using Python
- Structuring a data analysis project professionally
- Using Git and GitHub for version control

