import pandas as pd

# Load Dataset
df = pd.read_csv('data/Sales_transactions_2022_2025.csv')

# A list of report items that will be combined and written into a single file at the end
report_lines = []

def add(text=""):
    """add one line in report"""
    report_lines.append(text)

def add_table(dataframe, max_rows=None):
    """Add the DataFrame as a Markdown table."""
    if max_rows:
        dataframe = dataframe.head(max_rows)
    try:
        add(dataframe.to_markdown(index=False))
    except ImportError:
        # If the `tabulate` package is not installed, display the DataFrame as plain text.
        add("```")
        add(dataframe.to_string(index=False))
        add("```")
    add()

add("# Sales Transactions Data Quality Report")
add()
add(f"**Dataset:** `data/Sales_transactions_2022_2025.csv`")
add()
add("---")
add()

# =========================================================
# TASK 3.1 — Duplicate Row Checking
# =========================================================
add("## Task 3.1 — Duplicate Row Checking")
add()

# 1. Count Duplicate Rows & total duplicate rows in the dataset
duplicate_count = df.duplicated().sum()
total_rows = df.shape[0]
duplicate_percentage = (duplicate_count / total_rows) * 100

add(f"- **Total Rows:** {total_rows}")
add(f"- **Total Duplicate Rows:** {duplicate_count}")
add(f"- **Duplicate Rows Percentage:** {duplicate_percentage:.2f}%")
add()

# Show the duplicate rows
duplicate_rows = df[df.duplicated()]
add("### Duplicate Rows (first occurrence excluded)")
add()
if duplicate_rows.empty:
    add("_No duplicate rows found._")
    add()
else:
    add_table(duplicate_rows, max_rows=20)

# find all duplicate rows, including the first occurrence
all_duplicate = df[df.duplicated(keep=False)]
add("### All Duplicate Rows (including first occurrence)")
add()
if all_duplicate.empty:
    add("_No duplicate rows found._")
    add()
else:
    add_table(all_duplicate, max_rows=20)

# Check for duplicates in specific column: Customer_ID
allduplicate = df[df['Customer_ID'].duplicated(keep=False)]
add("### Duplicate `Customer_ID` Rows")
add()
if allduplicate.empty:
    add("_No duplicate Customer_ID found._")
    add()
else:
    add_table(allduplicate, max_rows=20)

add("---")
add()

# =========================================================
# TASK 3.2 — Date Validation
# =========================================================
add("## Task 3.2 — Date Validation")
add()

add(f"- **Order_Date original dtype:** `{df['Order_Date'].dtype}`")
add()

# convert to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce', format='%Y-%m-%d')

# check for invalid dates
invalid_dates = df[df['Order_Date'].isnull()]
add(f"- **Invalid / Unparseable Dates found:** {invalid_dates.shape[0]}")
add()
if not invalid_dates.empty:
    add("### Invalid Date Rows")
    add()
    add_table(invalid_dates, max_rows=20)

# Date range analysis and First and Last Order Dates
min_date = df['Order_Date'].min()
max_date = df['Order_Date'].max()
date_range = max_date - min_date

add("### Date Range Analysis")
add()
add(f"- **First Order Date:** {min_date}")
add(f"- **Last Order Date:** {max_date}")
add(f"- **Date Range:** {date_range.days} days")
add(f"- **Date Range in Years:** {round(date_range.days / 365.25, 2)} years")
add()
add("---")
add()

# =========================================================
# TASK 3.3 — Numerical Value Validation
# =========================================================
add("## Task 3.3 — Numerical Value Validation")
add()

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
        'Minimum': df[col].min(),
        'Maximum': df[col].max(),
        'Negative Count': (df[col] < 0).sum(),
        'Zero Count': (df[col] == 0).sum()
    })

report_table = pd.DataFrame(results)
add("### Summary Table (Min / Max / Negative / Zero Counts)")
add()
add_table(report_table)

add("---")
add()

# =========================================================
# TASK 3.4 — Date Range and Order Year
# =========================================================
add("## Task 3.4 — Date Range & Order Year")
add()

# Convert Order_Date to Datetime (mixed format safety net)
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='mixed', errors='coerce')

# Extract Year from Order_Date
df['Date_year'] = df['Order_Date'].dt.year

add("### Order_Date and Extracted Year (First 10 Rows)")
add()
add_table(df[['Order_Date', 'Date_year']], max_rows=10)

add("---")
add()
add("_Report generated automatically from `generate_report.py`._")

# =========================================================
# writing the file
# =========================================================
with open('report.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(report_lines))

print("report.md is ready। Please check your folder.")
