
import pandas as pd
import openpyxl as xl

# Load CSV File
df = pd.read_csv('E:\\Data_Analysis sheet\\retail\\data\\Sales_transactions_2022_2025.csv')


# Task 2.1 - Count Missing Values in Each Column

print(f"Missing values: {df.isnull().sum()}")


# Task 2.2 - Calculate Total Missing Values Percentage

missing = df.isnull().sum()
total_missing = missing.sum()

total_cells = df.size
total_cr = df.shape[0] * df.shape[1]

total_missing_percent = (total_missing / total_cr) * 100

print(f"Total Missing Values: {total_missing}")
print(f"\nTotal Missing Percent: {total_missing_percent:.2f}%")


# Task 2.3 - Identify Columns with Missing Values

missing = df.isnull().sum()

print(f"\nMissing column names:\n{missing[missing > 0]}")


# Task 2.4 - Calculate Total Missing Values

missing = df.isnull().sum()
missing_value = missing.sort_values(ascending=False)

print(f"\nMissing values:\n{missing_value[missing_value > 0]}")
print("-" * 30)
print(f"Total missing values: {missing.sum()}")


# Task 2.5 - Identify the Column with the Highest Missing Values

missing = df.isnull().sum()

highest_col = missing.idxmax()
max_count = missing.max()

print("\nMissing Values Report")
print("-" * 30)
print(f"Highest missing column name: {highest_col}")
print(f"Highest missing column value: {max_count}\n")

