# 📊 Task 03 — Data Quality Audit & Validation

### Retail Sales & Profitability Analysis

![Python](https://img.shields.io/badge/Python-Data_Analysis-blue?logo=python)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?logo=pandas)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)
![Level](https://img.shields.io/badge/Level-Intermediate-yellow)

---

## 📌 Overview

In this task, I will check the quality of my retail sales dataset using Python and Pandas.

During my initial data inspection, I found some unusual values that may affect the accuracy of my analysis.

My goal is to identify these values, investigate possible problems, and understand their meaning from a business point of view.

> **This task focuses on Data Quality Audit, not Data Cleaning.**

---

## 🎯 Business Scenario

During the initial inspection, I found some unusual values in the dataset:

| Column | Finding |
|---|---|
| `Quantity` | Minimum value: -3 |
| `Discount_Percentage` | Maximum value: 110 |
| `Customer_Age` | Maximum value: 112 |
| `Profit` | Contains negative values |
| `Order_Date` | Stored as a string |

These findings raised an important question:

**Are these values actual data errors, or are they part of normal business activities?**

I will investigate these values before making any decision.

---

## 📝 Task 3.1 — Duplicate Records Analysis

Duplicate records can affect transaction counts and sales calculations.

### What I Will Do

- Check for completely duplicated rows.
- Count the total duplicate records.
- Calculate the duplicate percentage.
- Display and inspect duplicate records.

### Validation Summary

| Validation Check | Result |
|---|---:|
| Total Rows | To be calculated |
| Duplicate Rows | To be calculated |
| Duplicate Percentage | To be calculated |

### Business Questions

- How many duplicate records exist?
- What percentage of the dataset contains duplicates?
- Can duplicate records affect sales analysis?
- Should duplicate records be deleted immediately?

**My Approach:** I will investigate duplicate records before deciding whether they should be removed.

---

## 📅 Task 3.2 — Date Validation

The `Order_Date` column is currently stored as a string.

To perform date-based analysis, I need to check whether the dates are valid and usable.

### What I Will Do

- Check the current data type.
- Validate date conversion.
- Identify invalid dates.
- Find the earliest and latest order dates.
- Calculate the date range.

### Validation Summary

| Validation Check | Result |
|---|---|
| Current Data Type | To be checked |
| Invalid Date Count | To be calculated |
| First Order Date | To be calculated |
| Last Order Date | To be calculated |
| Date Range | To be calculated |

### Business Questions

- Is `Order_Date` suitable for date analysis?
- Are there any invalid dates?
- How can incorrect dates affect sales trend analysis?

---

## 🔢 Task 3.3 — Numerical Value Validation

In this task, I will check important numerical columns to identify unusual values.

### Columns Under Review

| Column | Validation Focus |
|---|---|
| `Customer_Age` | Unusual age values |
| `Quantity` | Negative or zero quantity |
| `Unit_Price` | Negative or zero price |
| `Discount_Percentage` | Invalid discount values |
| `Sales_Amount` | Negative or zero sales |
| `Cost_Amount` | Negative or zero cost |
| `Profit` | Negative profit |
| `Delivery_Days` | Negative delivery days |
| `Customer_Rating` | Rating outside the allowed range |

### What I Will Check

For each numerical column, I will calculate:

- Minimum Value
- Maximum Value
- Negative Value Count
- Zero Value Count
- Potentially Unusual Value Count

### Basic Validation Rules

| Column | Validation Rule |
|---|---|
| `Customer_Age` | Negative age is invalid |
| `Quantity` | Negative quantity needs investigation |
| `Unit_Price` | Negative price needs investigation |
| `Discount_Percentage` | Values outside 0–100 need checking |
| `Customer_Rating` | Values outside 1–5 need checking |
| `Delivery_Days` | Negative delivery days need investigation |

### Business Observation

Not every unusual value is necessarily wrong.

For example:

- Negative quantity may represent a product return.
- Negative profit may represent a business loss.
- Zero sales may be related to cancelled orders.
- Negative cost may represent a refund or adjustment.

I will use business context before classifying any value as an error.

---

## 📆 Task 3.4 — Date Range & Order Year Consistency

The dataset contains two important columns:

- `Order_Date`
- `Order_Year`

I will check whether both columns contain consistent year information.

### What I Will Do

1. Extract the year from `Order_Date`.
2. Compare it with `Order_Year`.
3. Identify mismatched records.
4. Count the total year mismatches.
5. Inspect the mismatched records.

### Example

| Order_Date | Order_Year | Result |
|---|---:|---|
| 2022-05-10 | 2022 | Match |
| 2023-08-15 | 2024 | Mismatch |
| 2025-02-20 | 2025 | Match |

*Example data only.*

### Business Question

How can year mismatches affect yearly sales reports and business performance analysis?

---

## 📋 Task 3.5 — Data Quality Summary

After completing the validation tasks, I will prepare a summary of the results.

| Validation Check | Result |
|---|---:|
| Total Rows | Actual Count |
| Duplicate Rows | Actual Count |
| Invalid Date Count | Actual Count |
| Negative Quantity Count | Actual Count |
| Invalid Discount Count | Actual Count |
| Invalid Rating Count | Actual Count |
| Order Year Mismatch | Actual Count |

All results will be calculated using Python and Pandas.

---

## ⚠️ Audit Guidelines

During this task, I will follow these rules:

- Use Pandas for data analysis.
- Do not use NumPy, SQL, or visualization libraries.
- Do not delete any rows.
- Do not fill missing values.
- Do not modify original values.
- Do not treat every unusual value as an error.
- Support findings with actual data.
- Consider business context before making decisions.

---

## ✅ Progress Checklist

- [ ] Duplicate Records Analysis
- [ ] Duplicate Percentage Calculation
- [ ] Date Validation
- [ ] Invalid Date Identification
- [ ] Date Range Analysis
- [ ] Numerical Value Validation
- [ ] Negative Quantity Investigation
- [ ] Negative Profit Investigation
- [ ] Discount & Rating Validation
- [ ] Order Year Consistency Check
- [ ] Data Quality Summary
- [ ] Business Observations
- [ ] Excel Report Preparation

---

## 📦 Deliverables

| Deliverable | Description |
|---|---|
| Python Script | Data Quality Audit using Pandas |
| Excel Report | Validation results and summary |
| Documentation | Findings and business observations |

---

## 👨‍💼 Manager's Review

I will complete this task step by step.

### First Assignment: Task 3.1 — Duplicate Records Analysis

I will start by checking duplicate records only.

**Submission: