<div align="center">

# 📊 DATA INSPECTION REPORT

## Retail Sales & Profitability Analysis

**Task 01 | Initial Dataset Assessment**

<br>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Task](https://img.shields.io/badge/Task-01-blue?style=for-the-badge)
![Report](https://img.shields.io/badge/Type-Data_Inspection-2EA44F?style=for-the-badge)

**Inspect the Data. Identify Potential Issues. Establish an Analytical Foundation.**

</div>

---

## 📑 Table of Contents

- [1. Executive Summary](#-1-executive-summary)
- [2. Dataset Overview](#-2-dataset-overview)
- [3. Dataset Structure](#-3-dataset-structure)
- [4. Column Information](#-4-column-information)
- [5. Missing Values Overview](#-5-missing-values-overview)
- [6. Statistical Summary](#-6-statistical-summary)
- [7. Key Findings & Initial Observations](#-7-key-findings--initial-observations)
- [8. Data Quality Assessment](#-8-data-quality-assessment)
- [9. Business Analysis Opportunities](#-9-business-analysis-opportunities)
- [10. Next Steps](#-10-next-steps)
- [11. Conclusion](#-11-conclusion)

---

## 🎯 1. Executive Summary

The purpose of this report is to inspect the retail sales dataset and establish an initial understanding of its structure, completeness, data types, and numerical characteristics.

The dataset contains **18,045 records and 36 columns**, covering customer information, transactions, products, sales, costs, profits, payments, deliveries, and returns.

The initial inspection identified missing values in several columns, including `Return_Reason`, `Promotion_Code`, and `Customer_Rating`.

The statistical summary also revealed values that require further investigation, including negative quantities, negative profits, customer ages outside common business expectations, and discount percentages exceeding 100%.

These observations are not automatically confirmed data errors. Their validity must be assessed using the dataset's business rules and context.

> **Key takeaway:** The dataset provides a foundation for retail sales analysis, but further data quality checks are necessary before drawing reliable business conclusions.

---

## 📊 2. Dataset Overview

### Dataset Profile

| Metric | Result |
|---|---:|
| Total Records | 18,045 |
| Total Columns | 36 |
| String Columns | 25 |
| Float64 Columns | 9 |
| Int64 Columns | 2 |
| Reporting Period | 2022–2025 |
| Total Missing Cells | 35,341 |
| Columns with Missing Values | 10 |

**Dataset File:** `Sales_transactions_2022_2025.csv`

**Tools Used:** Python, Pandas, NumPy

**Analysis Type:** Initial Dataset Inspection

> **Note:** The total missing cell count is calculated by summing the missing values reported for all 10 affected columns. It represents missing cells, not the number of records containing at least one missing value.

---

## 🗂️ 3. Dataset Structure

The dataset contains information across several business areas.

| Category | Example Columns | Business Purpose |
|---|---|---|
| Transaction Information | `Transaction_ID`, `Order_ID` | Identify transactions and orders |
| Customer Information | `Customer_ID`, `Customer_Age`, `Customer_Gender` | Understand customer characteristics |
| Order Information | `Order_Date`, `Order_Time`, `Order_Status` | Analyze order activity and status |
| Sales Channels | `Sales_Channel`, `Store_ID`, `Store_Name` | Compare sales channels and stores |
| Geographic Information | `Country`, `Region`, `City` | Analyze regional performance |
| Product Information | `Product_ID`, `Product_Name`, `Product_Category` | Evaluate product performance |
| Sales & Profitability | `Quantity`, `Sales_Amount`, `Cost_Amount`, `Profit` | Assess sales and profitability |
| Payment Information | `Payment_Method` | Examine payment methods |
| Delivery Information | `Shipping_Method`, `Delivery_Days` | Investigate delivery performance |
| Returns & Promotions | `Return_Flag`, `Return_Reason`, `Promotion_Code` | Examine returns and promotions |
| Customer Feedback | `Customer_Rating` | Explore customer ratings |
| Inventory | `Inventory_Level` | Investigate inventory information |

These categories are based on the column names and intended analytical use. Their exact business definitions should be confirmed where necessary.

---

## 📋 4. Column Information

The dataset contains 36 columns with the following names and non-null counts.

| # | Column Name | Non-Null Count | Data Type |
|---:|---|---:|---|
| 1 | `Transaction_ID` | 18,045 | string |
| 2 | `Order_ID` | 18,045 | string |
| 3 | `Customer_ID` | 18,045 | string |
| 4 | `Customer_Name` | 17,937 | string |
| 5 | `Customer_Age` | 17,827 | float64 |
| 6 | `Customer_Gender` | 17,883 | string |
| 7 | `Customer_Segment` | 18,045 | string |
| 8 | `Order_Date` | 18,045 | string |
| 9 | `Order_Time` | 18,045 | string |
| 10 | `Sales_Channel` | 18,045 | string |
| 11 | `Store_ID` | 18,045 | string |
| 12 | `Store_Name` | 18,045 | string |
| 13 | `Country` | 18,045 | string |
| 14 | `Region` | 18,045 | string |
| 15 | `City` | 18,045 | string |
| 16 | `Product_ID` | 18,045 | string |
| 17 | `Product_Name` | 17,901 | string |
| 18 | `Product_Category` | 18,045 | string |
| 19 | `Product_Subcategory` | 18,045 | string |
| 20 | `Quantity` | 18,045 | int64 |
| 21 | `Unit_Price` | 18,045 | float64 |
| 22 | `Discount_Percentage` | 18,045 | float64 |
| 23 | `Sales_Amount` | 18,045 | float64 |
| 24 | `Cost_Amount` | 18,045 | float64 |
| 25 | `Profit` | 18,045 | float64 |
| 26 | `Payment_Method` | 17,898 | string |
| 27 | `Order_Status` | 18,045 | string |
| 28 | `Shipping_Method` | 18,045 | string |
| 29 | `Delivery_Days` | 17,883 | float64 |
| 30 | `Return_Flag` | 18,045 | string |
| 31 | `Return_Reason` | 1,877 | string |
| 32 | `Sales_Representative` | 18,045 | string |
| 33 | `Promotion_Code` | 8,308 | string |
| 34 | `Customer_Rating` | 14,610 | float64 |
| 35 | `Inventory_Level` | 17,847 | float64 |
| 36 | `Order_Year` | 18,045 | int64 |

### Data Type Distribution

| Data Type | Number of Columns |
|---|---:|
| String | 25 |
| Float64 | 9 |
| Int64 | 2 |
| **Total** | **36** |

### Initial Data Type Observations

- `Order_Date` and `Order_Time` are stored as strings. Their formats should be checked before converting them to appropriate date or time representations.
- `Customer_Age`, `Delivery_Days`, and `Inventory_Level` are stored as `float64`, partly because these columns contain missing values. Their expected business types should be reviewed before any conversion.
- Identifier columns such as `Transaction_ID`, `Order_ID`, and `Customer_ID` are stored as strings, which is appropriate when they function as identifiers rather than numerical measurements.

---

## 🕳️ 5. Missing Values Overview

The initial inspection identified missing values in 10 columns.

### Missing Value Summary

| Column Name | Missing Values | Missing Percentage |
|---|---:|---:|
| `Customer_Name` | 108 | 0.60% |
| `Customer_Age` | 218 | 1.21% |
| `Customer_Gender` | 162 | 0.90% |
| `Product_Name` | 144 | 0.80% |
| `Payment_Method` | 147 | 0.81% |
| `Delivery_Days` | 162 | 0.90% |
| `Return_Reason` | 16,168 | 89.60% |
| `Promotion_Code` | 9,737 | 53.96% |
| `Customer_Rating` | 3,435 | 19.04% |
| `Inventory_Level` | 198 | 1.10% |
| **Total Missing Cells** | **35,341** | — |

*Missing percentages are calculated using 18,045 total records and rounded to two decimal places.*

### Key Observations

- `Return_Reason` has the highest number of missing values.
- `Promotion_Code` is missing in more than half of all records.
- `Customer_Rating` also has a substantial number of missing values.
- The other affected columns have comparatively smaller missing percentages.

### Important Business Consideration

A missing `Return_Reason` may be expected when an order has not been returned. Similarly, a missing `Promotion_Code` may indicate that no promotion was applied.

These explanations are possibilities, not confirmed causes.

The next stage should compare missingness against relevant business fields, such as `Return_Flag` and order status, to determine whether the missing values are expected or require investigation.

---

## 📈 6. Statistical Summary

The following table presents the descriptive statistics obtained during the initial inspection.

| Statistic | Customer_Age | Quantity | Unit_Price | Discount_% | Sales_Amount | Cost_Amount | Profit | Delivery_Days | Customer_Rating | Inventory_Level | Order_Year |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 17,827 | 18,045 | 18,045 | 18,045 | 18,045 | 18,045 | 18,045 | 17,883 | 14,610 | 17,847 | 18,045 |
| Mean | 38.92 | 2.13 | 232.69 | 6.26 | 457.31 | 366.00 | 91.40 | 2.26 | 3.99 | 70.26 | 2023.57 |
| Std. Dev. | 10.73 | 1.79 | 294.21 | 6.88 | 856.60 | 705.87 | 167.83 | 2.32 | 1.01 | 22.04 | 1.12 |
| Minimum | 4 | -3 | 21.39 | 0 | 16.68 | 12.17 | -299.31 | 0 | 1 | 0 | 2022 |
| 25% | 32 | 1 | 53.38 | 0 | 78.53 | 56.12 | 19.48 | 0 | 4 | 55 | 2023 |
| Median | 39 | 2 | 99.87 | 5 | 168.81 | 122.30 | 40.19 | 1 | 4 | 70 | 2024 |
| 75% | 46 | 3 | 285.58 | 10 | 472.45 | 376.02 | 93.27 | 4 | 5 | 85 | 2025 |
| Maximum | 112 | 11 | 1,425.09 | 110 | 14,303.07 | 10,791.00 | 3,512.08 | 10 | 5 | 157 | 2025 |

*Values are rounded for readability. The original descriptive statistics should be retained in the analysis notebook when exact precision is required.*

### Interpretation Notes

- The average customer age is approximately 38.92 years.
- The average quantity is approximately 2.13 units per record.
- The mean sales amount is approximately 457.31.
- The mean profit is approximately 91.40.
- The mean customer rating is approximately 3.99 on the observed 1–5 scale.
- The maximum discount percentage is 110, which requires validation against the dataset's discount rules.

**Important:** Descriptive statistics summarize the observed data. They do not establish whether unusual values are incorrect.

---

## 🔎 7. Key Findings & Initial Observations

### 7.1 Dataset Size

The dataset contains 18,045 records and 36 columns, providing a broad range of information for further retail sales analysis.

### 7.2 Data Types

The dataset contains 25 string columns, 9 float64 columns, and 2 int64 columns.

The date and time columns are currently stored as strings and may require further inspection before time-based analysis.

### 7.3 Customer Age

The average customer age is approximately 38.92 years.

The minimum age is 4, while the maximum age is 112. These values should be reviewed against the intended customer population and business rules.

The observed values alone do not establish that either record is invalid.

### 7.4 Sales and Profitability

The average `Sales_Amount` is approximately 457.31, while the average `Profit` is approximately 91.40.

The minimum profit is -299.31, indicating that some records have negative profit values.

These records should be investigated to understand whether they represent valid business outcomes, returns, adjustments, or calculation issues.

### 7.5 Quantity

The average quantity is approximately 2.13 units per record.

The minimum quantity is -3. Negative quantities may represent returns or adjustments, but the dataset's business rules must be checked before classifying them.

### 7.6 Discount Percentage

The average discount percentage is approximately 6.26%.

The maximum value is 110%, which is unusual under conventional discount definitions.

The calculation method, business rules, and underlying records should be checked before determining whether this is a data quality issue.

### 7.7 Customer Ratings

The average customer rating is approximately 3.99.

The observed minimum and maximum ratings are 1 and 5, respectively. However, 3,435 ratings are missing.

The missingness may affect customer satisfaction analysis if the available ratings are not representative of all transactions.

### 7.8 Delivery Time

The average recorded delivery time is approximately 2.26 days.

Some records have a delivery time of zero days. This may reflect same-day delivery or another business rule, but the interpretation requires additional context.

### 7.9 Potential Analysis Opportunities

The available fields could support future analysis of:

- Sales trends over time.
- Product and category performance.
- Profitability by product, region, and channel.
- Customer segments and purchasing patterns.
- Promotion effectiveness.
- Delivery performance.
- Return patterns.
- Customer ratings.
- Inventory-related trends.

These are potential analytical directions, not completed findings.

---

## 🛡️ 8. Data Quality Assessment

The initial inspection identifies several areas that require further investigation.

| Area | Observation | Recommended Investigation |
|---|---|---|
| Missing Data | Missing values exist in 10 columns. | Quantify missingness and investigate its context. |
| Return Reasons | 89.60% of values are missing. | Compare against `Return_Flag` and relevant order statuses. |
| Promotion Codes | 53.96% of values are missing. | Check whether missing codes correspond to transactions without promotions. |
| Customer Ratings | 19.04% of values are missing. | Investigate rating availability and possible response patterns. |
| Customer Age | Values range from 4 to 112. | Validate against the intended customer population and business rules. |
| Quantity | Minimum value is -3. | Investigate returns, adjustments, and transaction definitions. |
| Discount | Maximum value is 110%. | Verify the discount formula, scale, and allowed business rules. |
| Profit | Negative values are present. | Check the profit calculation and transaction context. |
| Date & Time | Stored as strings. | Validate formats before converting to date/time types. |
| Duplicate Records | Not yet investigated. | Check exact duplicate rows and possible repeated transactions. |

### Data Handling Principles

At this stage:

- No missing values have been filled.
- No rows or columns have been deleted.
- No unusual values have been automatically classified as errors.
- No duplicate-record conclusions have been made.

All potential issues should be investigated before any data cleaning decisions are implemented.

---

## 💼 9. Business Analysis Opportunities

The dataset may support several business questions once its quality and structure have been investigated.

| Business Area | Potential Question |
|---|---|
| Sales Performance | How do sales change over time? |
| Product Analysis | Which products and categories generate the most sales? |
| Profitability | Which products or regions generate higher or lower profit? |
| Customer Analysis | How do purchasing patterns differ across customer segments? |
| Promotions | How are promotional transactions associated with sales and profitability? |
| Delivery | How does delivery time vary across orders or shipping methods? |
| Returns | Which products or categories have more returns? |
| Customer Experience | How do customer ratings vary across products or channels? |
| Inventory | How does recorded inventory relate to product sales? |

These questions should be investigated only after confirming that the relevant fields are sufficiently reliable for the intended analysis.

---

## 🚀 10. Next Steps

Based on the initial inspection, the recommended next steps are:

### Task 02 — Missing Values Analysis

- Calculate missing values for every column.
- Calculate missing percentages.
- Identify the columns with the highest missingness.
- Investigate possible business explanations.

### Task 03 — Duplicate Records Analysis

- Identify exact duplicate rows.
- Investigate repeated transaction identifiers.
- Distinguish duplicate records from legitimate repeated transactions.

### Task 04 — Data Type Validation

- Inspect date and time formats.
- Review numerical columns and their expected business types.
- Validate data conversion requirements.

### Task 05 — Data Quality Assessment

- Investigate unusual quantities, discounts, ages, and profit values.
- Compare observations against documented business rules.
- Record confirmed issues separately from potential concerns.

### Task 06 — Exploratory Data Analysis

- Explore sales trends.
- Compare product and regional performance.
- Investigate customer segments.
- Examine profitability and return patterns.

> **Note:** These are recommended next steps. Each task should be completed and documented before its findings are presented as established results.

---

## 📝 11. Conclusion

The initial inspection established the dataset's size, structure, column types, missing value distribution, and numerical characteristics.

The results indicate that the dataset offers opportunities for retail sales and profitability analysis. However, missing information and several unusual numerical values require further investigation.

The next stage is to assess missing values and other potential data quality issues before conducting deeper exploratory analysis.

**A reliable analysis begins with understanding the data, questioning unusual observations, and supporting decisions with evidence.**

---

<div align="center">

### 📊 TASK 01 — COMPLETED: INITIAL INSPECTION DOCUMENTED

**Next:** Missing Values Analysis

*Inspect Carefully · Investigate Objectively · Analyze Responsibly*

</div>