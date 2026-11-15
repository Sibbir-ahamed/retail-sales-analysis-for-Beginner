import pandas as pd

# Load Dataset
df = pd.read_csv('data/Sales_transactions_2022_2025.csv')

# task 3.1 
# 1. Count Duplicate Rows o total duplicate rows in the dataset
duplicate_count =df.duplicated().sum()
print(f"\nTotal number of duplicate rows: {duplicate_count}")

# total number of rows in the dataset
total_rows = df.shape[0]
print(f"\nTotal Rows: {total_rows}")

# 2. Calculate Duplicate Rows Percentage 
duplicate_percentage = (duplicate_count/total_rows)*100
print(f"\nDuplicate rows percentage: {duplicate_percentage:.2f}%")

# Show the duplicate rows
duplicate_rows = df[df.duplicated()]
print(f"\nDuplicate Rows:")
print(duplicate_rows)


# find all duplicate rows , includuing the first occurrence

all_duplicate = df[df.duplicated(keep=False)]
print(f"\nAll Duplicate rows : { all_duplicate}")

# Check for duplicates in specific columns
# allduplicate = df[df.duplicated(keep=False)]
# col_name = [
# 'Transaction_ID',
# 'Customer_ID',
# 'Order_ID',
# 'Prduct_ID',
# 'Customer_Name'
# ]
# print(allduplicate[col_name])


# TASK 3.2 — Date Validation

