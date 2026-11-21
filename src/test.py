import pandas as pd
df = pd.read_csv('data/Sales_transactions_2022_2025.csv')

# step 1 : Convert Order_Date to Datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

# step 2: Extract Year from Order_Date
df['Date_year'] = df['Order_Date'].dt.year

# step 3 : compare Date_Year with order_year
df['Year_Match'] = (df['Date_year']) == df['Order_Date']

# step 4: Identify Mismatch Records
mismatch = df[df['Year_Match'] == False]

# step 5 : Display Mismatch Records
print(mismatch['Order_Date', 'Date_Year','Order_Year'].to_string(index=False))

# step 6 : Count Total Mismatch
print("\nTotal Year Mismatch:", len(mismatch))


