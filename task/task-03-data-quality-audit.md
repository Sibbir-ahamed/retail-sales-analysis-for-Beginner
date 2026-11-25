# 📊 TASK 03 — Data Quality Audit & Validation

**Project:** Retail Sales & Profitability Analysis  
**Position:** Junior Data Analyst  
**Difficulty:** Intermediate 🟠  
**Tools:** Python, Pandas, VS Code  
**Dataset:** `Sales_transactions_2022_2025.csv`  
**Submission:** Python Script + Excel Report + GitHub Documentation

---

## 🎯 Business Scenario

The company manager has noticed some unusual values in the sales dataset.

During the initial inspection, the following observations were found:

- The minimum value of `Quantity` is `-3`.
- The maximum value of `Discount_Percentage` is `110`.
- The maximum value of `Customer_Age` is `112`.
- The `Profit` column contains negative values.
- The `Order_Date` column is stored as a string.

The management team wants to understand:

**Are these values actual data quality problems, or are they part of normal business operations?**

Your responsibility is to perform a Data Quality Audit, identify potential issues, and provide data-based evidence for each finding.

---

## 📝 TASK 3.1 — Duplicate Records Analysis

First, check whether the dataset contains duplicate records.

### Your Tasks

1. Identify completely duplicated rows.
2. Calculate the total number of duplicate rows.
3. Calculate the percentage of duplicate rows.
4. Examine the duplicate records, if any.

### Manager's Questions

- How many duplicate rows are present in the dataset?
- What percentage of the dataset contains duplicate rows?
- Should duplicate records be deleted immediately? Why or why not?

**Important:** Do not delete any duplicate rows at this stage.

---

## 📝 TASK 3.2 — Date Validation

The `Order_Date` column is currently stored as a string.

To perform accurate sales trend analysis, the date values must be handled correctly.

### Your Tasks

1. Check the current data type of `Order_Date`.
2. Verify whether the dates follow a consistent format.
3. Identify dates that cannot be parsed.
4. Validate the date range.
5. Find the earliest and latest order dates in the dataset.

### Manager's Questions

- Is the `Order_Date` column suitable for DateTime analysis?
- How can invalid dates be identified?
- What problems can incorrect date formats cause in sales trend analysis?

**Important:** Do not modify the original dataset. Use a separate test Series or DataFrame if necessary.

---

## 📝 TASK 3.3 — Numerical Value Validation

Now, validate the following important numerical columns.

| Column | Validation Check |
|---|---|
| `Customer_Age` | Unusual age values |
| `Quantity` | Negative or zero quantity |
| `Unit_Price` | Zero or negative price |
| `Discount_Percentage` | Unusual discount values |
| `Sales_Amount` | Zero or negative sales |
| `Cost_Amount` | Zero or negative cost |
| `Profit` | Negative profit |
| `Delivery_Days` | Negative delivery days |
| `Customer_Rating` | Ratings outside the allowed range |

### Your Tasks

For each column:

1. Calculate the minimum value.
2. Calculate the maximum value.
3. Count negative values where applicable.
4. Count zero values where applicable.
5. Identify the number of potentially unusual values.

### Initial Business Validation Rules

You may use the following rules as a starting point:

| Column | Initial Validation Rule |
|---|---|
| `Customer_Age` | Negative age is unusual |
| `Quantity` | Negative quantity requires investigation |
| `Unit_Price` | Negative price requires investigation |
| `Discount_Percentage` | Values outside 0–100 require investigation |
| `Customer_Rating` | Values outside 1–5 require investigation |
| `Delivery_Days` | Negative values require investigation |

**Important:** These are initial validation rules, not final business rules.

For example:

- Negative quantity may represent a return or adjustment.
- Negative profit may represent a genuine business loss.
- Zero sales may be related to cancelled orders or promotional transactions.

Do not classify any value as incorrect without supporting evidence.

### Manager's Questions

- Which column contains the highest number of potentially unusual values?
- Which unusual values may be part of normal business operations?
- Which values require additional information or investigation?

---

## 📝 TASK 3.4 — Date Range & Order Year Consistency

The dataset contains two important columns:

- `Order_Date`
- `Order_Year`

Your goal is to check whether these two columns are consistent.

### Your Tasks

1. Extract the year from `Order_Date`.
2. Compare the extracted year with `Order_Year`.
3. Identify records where the years do not match.
4. Calculate the total number of year-mismatch records.

### Example

| Order_Date | Order_Year | Result |
|---|---:|---|
| 2022-05-10 | 2022 | Match |
| 2023-08-15 | 2024 | Mismatch |
| 2025-02-20 | 2025 | Match |

*This is only an example.*

### Manager's Question

If `Order_Date` and `Order_Year` are inconsistent, how reliable will the Year-wise Sales Analysis be?

---

## 📝 TASK 3.5 — Create a Data Quality Summary

Now, organize all your validation results into a single summary.

A Data Analyst should not only identify problems but also prepare a report that helps the manager make informed decisions.

### Your Report Must Include

| Validation Check | Result |
|---|---|
| Total Rows | Actual count |
| Duplicate Rows | Actual count |
| Invalid Date Count | Actual count |
| Negative Quantity Count | Actual count |
| Invalid Discount Count | Actual count |
| Invalid Rating Count | Actual count |
| Order Year Mismatch | Actual count |

All results must be calculated directly from the dataset using Python and Pandas.

**Do not enter or assume any result manually.**

## ⚠️ Manager's Strict Instructions

The following rules must be followed throughout this task:

- Use only Pandas for data analysis.
- Do not use NumPy, SQL, or visualization libraries.
- Do not delete any rows.
- Do not fill any missing values.
- Do not modify any original values.
- Do not classify every unusual value as incorrect data.
- Support every finding with data-based evidence.

Your current responsibility is **Data Quality Audit**, not Data Cleaning.

The goal is to identify potential data quality issues, understand their business context, and provide reliable findings for management.