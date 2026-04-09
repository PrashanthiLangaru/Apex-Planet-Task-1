import pandas as pd
import numpy as np
df = pd.read_csv("sampledata.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

numeric_columns = df.select_dtypes(include=np.number).columns
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

categorical_columns = df.select_dtypes(include="object").columns
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    df = df[(df[col] >= lower) & (df[col] <= upper)]


if "Salary" in df.columns:
    df["Annual_Salary"] = df["Salary"] * 12

df.to_csv("cleaned_data.csv", index=False)

print("\nData Cleaning Completed Successfully!")