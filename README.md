Task-1: Data Immersion & Wrangling

This repository contains my Task-1 submission for the AppexPlanet Data Analytics Internship

📂 Project Overview

This project is part of the ApexPlanet Data Analytics Internship (Task-1). It demonstrates the ability to take raw, messy data and move it through a professional data-wrangling pipeline to ensure it is accurate and usable for business intelligence.


🎯 Objective

The primary goal is to understand a raw dataset, identify data quality issues, and prepare a clean, analysis-ready dataset for further exploration and visualization.


📊 Dataset Details

Source: Raw data provided for analysis.
Structure: Tabular data containing various features that required standardization.
State: Initially contained missing values, duplicates, and inconsistent formatting.


⚠️ Data Issues Found

Missing Values: Several entries were incomplete.
Duplicate Records: Redundant data rows that could skew analysis.
Inconsistent Formatting: Mixed date formats and inconsistencies across string-based columns.


🧹 Data Cleaning Steps

Deduplication: Identified and removed all duplicate records.
Null Handling: Addressed missing values to maintain data integrity.
Standardization: Converted all date columns to a uniform format.
Feature Engineering: Transformed raw data into more useful variables for analysis.
Validation: Created a Data Dictionary to define and describe each cleaned column.


🛠️ Tools Used

Python: The primary programming language for automation.
Pandas: For high-performance data manipulation and cleaning.


📁  Project Files

raw_data.csv: The original, unedited dataset.
cleaned_data.csv: The final output file after processing.
data_dictionary.xlsx: A reference file explaining the cleaned data attributes.
data_cleaning.py (or Task1.py): The script containing the cleaning logic.


🏁 Final Output

A refined, high-quality CSV file (cleaned_data.csv) that is structured, consistent, and ready for immediate use in data visualization tools or statistical models.
