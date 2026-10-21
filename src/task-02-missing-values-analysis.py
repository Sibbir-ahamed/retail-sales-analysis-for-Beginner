import pandas as pd
import openpyxl as xl 

# Load CSV File
df = pd.read_csv('E:\\Data_Analysis sheet\\retail\\data\\Sales_transactions_2022_2025.csv')

# Task2.1
# প্রতিটি Column-এ কতটি Missing Value আছে, তা বের করবে।
# missing values- 

print(f"missing values: {df.isnull().sum()}")


# Task2.2
#Missing percentage for each column
missing = df.isnull().sum()
total_col = df.shape[0]
total_row = df.shape[1]
persent = ((missing / total_col )*100)
print(f"Each column persentese is: {persent}")

total_missing_percentage = missing.sum()
total_idx = total_col * total_row
print(f"\nTotal percentage :{(total_missing_percentage / total_idx)*100 } % ")


# task 2.3 
# Missing values each columns names - কোন Column-এ Missing Values আছে?
missing = df.isnull().sum()
print(f"\nMissing column names:\n{missing[missing > 0]}")

# task 2.4
# Calculate Total Missing Values - মোট কতটি Missing cell আছে?
missing = df.isnull().sum()
missing_value = missing.sort_values(ascending=False)
print(f"\nMissing values: \n{missing_value[missing_value > 0]}")
print("-" * 30)
print(f"Total missing values: {missing.sum()}")


#task 2.5
# highest missing values column name - কোন Column-এ সবচেয়ে বেশি Missing Values রয়েছে?

missing = df.isnull().sum()

highest_col = missing.idxmax()
max_count = missing.max()

print("\nMissing Values Report")
print("-"* 30 )
print(f"Highest missing column name: {highest_col}")
print(f"Highest missing column value : {max_count}\n")






