import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('E:\\Data_Analysis sheet\\retail\\data\\Sales_transactions_2022_2025.csv')

# Display the first 10 rows of the DataFrame
print("First 10 rows of the DataFrame:")
print(df.head(10))

# Display the last 5 rows of the DataFrame
print("\nLast 5 rows of the DataFrame:")
print(df.tail(5))

# total number of rows and columns 
# axis=1 means column wise and axis=0 means row wise
print(f"Total rows: {df.shape[0]}")
print(f"Total columns: {df.shape[1]}") 

# All the columns name
print("\nAll the columns name")
print(df.columns.tolist())

# Display the data types
print("\nData types:")
print(df.dtypes)

# Display the summary statistics of the DataFrame
print("\nSummary statistics:")
print(df.describe())

# information about the DataFrame
print("\nInformation :")
print(df.info())










