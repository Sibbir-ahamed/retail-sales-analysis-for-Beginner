import pandas as pd

# Load CSV File
df = pd.read_csv('E:\\Data_Analysis sheet\\retail\\data\\Sales_transactions_2022_2025.csv')

# Task2.1
# missing values- 

print(f"missing values: {df.isnull().sum()}")

# Total missing values 
print(f"\nTotal missing values: {df.isnull().sum().sum()}")

# Missing values each columns names
missing = df.isnull().sum()
print(f"\nMissing column names:\n{missing[missing > 0]}")


# highest missing values column name 

missing = df.isnull().sum()

highest_col = missing.idxmax()
max_count = missing.max()

print("\nMissing Values Report")
print("-"* 30 )
print(f"Highest missing column name: {highest_col}")
print(f"Highest missing column value : {max_count.max()}")

# Task2.2
#Missing percentage for each column
missing = df.isnull().sum()
total_col = df.shape[0]
return_reson = ((missing / total_col )*100)
print(f"Each column persentese is: {return_reson}")







