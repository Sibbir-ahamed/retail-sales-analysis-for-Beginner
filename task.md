## Now I'm your Manager-
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-brightgreen)

| | |
|---|---|
| **Project** | Retail Sales & Profitability Analysis |
| **Department** | Data Analytics |
| **Your Position** | Junior Data Analyst |
| **Difficulty** | Beginner |
| **Tool** | Python + Pandas |
| **Dataset** | `Sales_transactions_2022_2025.csv` |
| **Estimated Time** | 30–45 minutes for a task |

---

# 📋 TASK 01 — Dataset Inspection

1. Load the CSV file using Pandas.
2. Display the first 10 rows.
3. Display the last 5 rows.
4. Find the total number of rows and columns.
5. Display all column names.
6. Inspect data types and non-null counts.
7. Generate a statistical summary of numerical columns.
8. Write your own observations based on the dataset.

# 📊 Task 02 — Missing Values Analysis

## 1. Business Scenario — Why Does Your Work Matter?

Imagine you are working as a Junior Data Analyst at a retail company.

The company has given you a sales dataset covering **2022–2025**.

Management wants to know:

- Which columns contain missing values?
- Which column has the most missing values?
- How many missing values are there in total?
- In which column could a high number of missing values affect future analysis?
- Are the missing values actually errors, or are they a result of normal business processes?

Your responsibility is to find the answers to these questions.

> [!IMPORTANT]
> You will **not** fill in any missing values or delete any rows yet. First, you will only **analyze**.

---

## 2. What Do You Need to Do in Task 02?

You need to complete a total of **6 tasks**.

| Task | Activity | What You Will Learn |
|------|----------|---------------------|
| 2.1 | Missing Values Count | How many missing values are in each column |
| 2.2 | Missing Values Percentage | What percentage of each column's values is missing |
| 2.3 | Columns with Missing Values | Which columns contain missing values |
| 2.4 | Total Missing Values | How many missing cells are in the entire dataset |
| 2.5 | Highest Missing Values | Which column has the most missing values |
| 2.6 | Business Interpretation | How missing values can affect business analysis |

---

## ✅ Progress Checklist

- [ ] 2.1 Missing Values Count
- [ ] 2.2 Missing Values Percentage
- [ ] 2.3 Columns with Missing Values
- [ ] 2.4 Total Missing Values
- [ ] 2.5 Highest Missing Values
- [ ] 2.6 Business Interpretation





```python
import pandas as pd

# Load Dataset
df = pd.read_csv('data/Sales_transactions_2022_2025.csv')

# 1. Count Duplicate Rows
duplicate_count = df.duplicated().sum()

# 2. Calculate Duplicate Percentage
total_rows = len(df)
duplicate_percentage = (duplicate_count / total_rows) * 100

# Display Output
print("Total Rows:", total_rows)
print("Total Duplicate Rows:", duplicate_count)
print(f"Duplicate Percentage: {duplicate_percentage:.2f}%")



চাইলে সব Duplicate Row দেখতে পারো:

duplicate_rows = df[df.duplicated()]
print(duplicate_rows)





















```





