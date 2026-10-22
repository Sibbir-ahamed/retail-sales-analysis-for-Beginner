import pandas as pd

# Load Dataset
df = pd.read_csv('data/Sales_transactions_2022_2025.csv')

# task 3.1 
# 1. Count Duplicate Rows
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





