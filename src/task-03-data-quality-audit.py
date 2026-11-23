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

allduplicate= df[df['Customer_ID'].duplicated(keep=False)]
print(f"\nAll Duplicate rows in Customer_ID: {allduplicate}")

### TASK 3.2 — Date Validation

#1 check Order_Date data type
print(f"\nOrder_Date data type: {df['Order_Date'].dtype}")

#2 check date formate
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors = 'coerce', format='%Y-%m-%d')

df['Order_Year'] = pd.to_datetime(df['Order_Year'], errors='coerce')

# print(f"\nOrder_date formate:{df['Order_Date'].dtypes}")
# print(f"\nOrder_date after conversion:\n{df['Order_Date'].head(10)}")

#2 check for invalid dates
invalid_dates = df[df['Order_Date'].isnull()]
print(f"\nInvalid Dates:\n{invalid_dates}")

# 3

# 4 & 5 Date range analysis and First and Last Order Dates 

min_date = df['Order_Date'].min()
max_date = df['Order_Date'].max()
date_range =  max_date - min_date
print("Date Range Analysis")
print("=====================")
print("First Order Date: ", min_date) 
print("Last Order Date: ", max_date)
print("Date Range: ", date_range.days, "days" )
print("Date Range in Years: " , round(date_range.days/365.25, 2), "years")

### TASK 3.3 — Numerical Value Validation single way
# 1. Check numerical Columns
numeric_columns = [
    'Customer_Age',
    'Quantity',
    'Unit_Price',
    'Discount_Percentage',
    'Sales_Amount',
    'Cost_Amount',
    'Profit',
    'Delivery_Days',
    'Customer_Rating'
]
print("------------Minimum Values--------------------\n")
for col in numeric_columns:
    print(col, "Minimum:", df[col].min())
print("-------------Maximum Values-------------------\n")
for col in numeric_columns:
    print(col, "Maximum:", df[col].max())

# 3. Negative Value Count
for col in numeric_columns:
    negative_count = (df[col] <0).sum()
    print(f"\nNegative Value Count in {col} : {negative_count}")
# 4. Zero Value Count
print("\n-------------Zero Values-------------------\n")
for col in numeric_columns:
    zero_count = (df[col]==0).sum()
    print(f"\nZero Value Count in {col} : {zero_count}")


### Task 3.3 — Numerical Value Validation - Try another way to get all results in one table
# ----------- all result in one table -----------

numeric_columns = [
    'Customer_Age',
    'Quantity',
    'Unit_Price',
    'Discount_Percentage',
    'Sales_Amount',
    'Cost_Amount',
    'Profit',
    'Delivery_Days',
    'Customer_Rating'
]

results = []

for col in numeric_columns:
    results.append({
        'Column': col,
        'Minimum':df[col].min(),
        'Maximum':df[col].max(),
        'Negative':(df [col] < 0 ).sum(),
        'Zero Count': (df[col] == 0).sum()

    })

report = pd.DataFrame(results)
print(report.to_string(index=False))

### TASK 3.4 — Date Range ও Order Year 

# Step 1: Convert Order_Date to Datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Step 2: Extract Year from Order_Date
df['Date_year'] = df['Order_Date'].dt.year

# Step 3: Compare Date_year with Order_Year
df['Result'] = df['Date_year'].eq(df['Order_Date']).map({
    True:'Match',
    False:'Mismatch'
})

# Step 4: Display Result
print(df[['Result', 'Order_Date','Order_Year']])


