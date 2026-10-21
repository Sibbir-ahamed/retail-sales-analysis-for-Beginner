<!-- ======================================================= -->

<!-- RETAIL SALES & PROFITABILITY ANALYSIS                   -->

<!-- TASK 02: MISSING VALUES ANALYSIS                        -->

<!-- ======================================================= -->

<div align="center">

# 📊 RETAIL SALES ANALYTICS

### MISSING VALUES & DATA QUALITY REPORT

**Task 02 · Data Inspection & Quality Assessment**

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Analysis](https://img.shields.io/badge/Data_Analysis-0078D4?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-2E8B57?style=for-the-badge)

---

</div>

## 📌 01 — Executive Summary

This report analyzes missing values in the Retail Sales Transactions dataset using Python and Pandas. The objective is to evaluate data completeness, identify columns with missing values, and determine which fields require further investigation.

### 📈 Dataset Overview

| 📊 Metric                      |  📋 Result |
| :----------------------------- | ---------: |
| Total Records                  |   `19,850` |
| Total Columns                  |       `36` |
| Total Data Cells               |  `714,600` |
| Total Missing Values           |   `30,479` |
| Data Completeness              | **95.31%** |
| Missing Data Percentage        |  **4.69%** |
| Columns with Missing Values    |       `10` |
| Columns without Missing Values |       `26` |

### 🎯 Data Completeness

| Data Category | Percentage | Status    |
| :------------ | ---------: | :-------- |
| Complete Data |     95.31% | 🟢 Good   |
| Missing Data  |      4.69% | 🟠 Review |

> **Key Insight:** Most data cells contain values. However, missing values are concentrated in a few columns and require further investigation.

---

## 🔍 02 — Missing Values in Each Column

The `isnull().sum()` method was used to calculate the number of missing values in each column.

<details>
<summary><strong>📂 Click to view all 36 columns</strong></summary>

<br>

| No. | Column Name            | Missing Values |
| --: | :--------------------- | -------------: |
|   1 | `Transaction_ID`       |              0 |
|   2 | `Order_ID`             |              0 |
|   3 | `Customer_ID`          |              0 |
|   4 | `Customer_Name`        |            108 |
|   5 | `Customer_Age`         |            218 |
|   6 | `Customer_Gender`      |            162 |
|   7 | `Customer_Segment`     |              0 |
|   8 | `Order_Date`           |              0 |
|   9 | `Order_Time`           |              0 |
|  10 | `Sales_Channel`        |              0 |
|  11 | `Store_ID`             |              0 |
|  12 | `Store_Name`           |              0 |
|  13 | `Country`              |              0 |
|  14 | `Region`               |              0 |
|  15 | `City`                 |              0 |
|  16 | `Product_ID`           |              0 |
|  17 | `Product_Name`         |            144 |
|  18 | `Product_Category`     |              0 |
|  19 | `Product_Subcategory`  |              0 |
|  20 | `Quantity`             |              0 |
|  21 | `Unit_Price`           |              0 |
|  22 | `Discount_Percentage`  |              0 |
|  23 | `Sales_Amount`         |              0 |
|  24 | `Cost_Amount`          |              0 |
|  25 | `Profit`               |              0 |
|  26 | `Payment_Method`       |            147 |
|  27 | `Order_Status`         |              0 |
|  28 | `Shipping_Method`      |              0 |
|  29 | `Delivery_Days`        |            162 |
|  30 | `Return_Flag`          |              0 |
|  31 | `Return_Reason`        |         16,168 |
|  32 | `Sales_Representative` |              0 |
|  33 | `Promotion_Code`       |          9,737 |
|  34 | `Customer_Rating`      |          3,435 |
|  35 | `Inventory_Level`      |            198 |
|  36 | `Order_Year`           |              0 |

</details>

---

## 🚨 03 — Columns Requiring Attention

The following 10 columns contain missing values.

|  Priority | Column Name       | Missing Values |
| :-------: | :---------------- | -------------: |
|  🔴 High  | `Return_Reason`   |         16,168 |
|  🔴 High  | `Promotion_Code`  |          9,737 |
|  🟠 High  | `Customer_Rating` |          3,435 |
| 🟡 Review | `Customer_Age`    |            218 |
| 🟡 Review | `Inventory_Level` |            198 |
| 🟡 Review | `Customer_Gender` |            162 |
| 🟡 Review | `Delivery_Days`   |            162 |
| 🟡 Review | `Payment_Method`  |            147 |
| 🟡 Review | `Product_Name`    |            144 |
| 🟢 Review | `Customer_Name`   |            108 |

**Observation:** `Return_Reason`, `Promotion_Code`, and `Customer_Rating` account for most of the missing values.

*Priority is based on missing-value counts and does not necessarily represent business risk.*

---

## 🏆 04 — Missing Values Ranking

The columns containing missing values were ranked in descending order.

| Rank | Column Name       | Missing Values | Share of All Missing Values |
| ---: | :---------------- | -------------: | --------------------------: |
| 🥇 1 | `Return_Reason`   |         16,168 |                      53.05% |
| 🥈 2 | `Promotion_Code`  |          9,737 |                      31.94% |
| 🥉 3 | `Customer_Rating` |          3,435 |                      11.27% |
|    4 | `Customer_Age`    |            218 |                       0.72% |
|    5 | `Inventory_Level` |            198 |                       0.65% |
|    6 | `Customer_Gender` |            162 |                       0.53% |
|    7 | `Delivery_Days`   |            162 |                       0.53% |
|    8 | `Payment_Method`  |            147 |                       0.48% |
|    9 | `Product_Name`    |            144 |                       0.47% |
|   10 | `Customer_Name`   |            108 |                       0.35% |
|      | **Total**         |     **30,479** |                 **100.00%** |

### 💡 Ranking Insights

* 🔴 `Return_Reason` accounts for approximately **53.05%** of all missing values.
* 🟠 `Promotion_Code` accounts for approximately **31.94%**.
* 🟡 `Customer_Rating` accounts for approximately **11.27%**.

Together, these three columns account for approximately **96.26% of all missing values**.

---

## 🎯 05 — Highest Missing Values Analysis

### 🔴 Column: `Return_Reason`

| Metric                           |          Result |
| :------------------------------- | --------------: |
| Column Name                      | `Return_Reason` |
| Missing Values                   |      **16,168** |
| Total Dataset Rows               |          19,850 |
| Missing Percentage Within Column |      **81.45%** |

### Analysis

The `Return_Reason` column has the highest number of missing values in the dataset.

Approximately **81.45% of its rows have no recorded return reason**.

However, a missing return reason does not automatically indicate a data quality problem. Orders that were never returned may legitimately have no return reason.

### Recommended Investigation

1. Examine the `Return_Flag` column.
2. Identify orders marked as returned.
3. Check whether those returned orders have a corresponding `Return_Reason`.
4. Investigate missing reasons for returned orders.
5. Avoid filling missing values until their meaning is understood.

---

## 📊 06 — Key Findings

| No. | Finding                           | Result            |
| --: | :-------------------------------- | :---------------- |
|   1 | Total Missing Values              | 30,479            |
|   2 | Overall Missing Percentage        | 4.69%             |
|   3 | Overall Data Completeness         | 95.31%            |
|   4 | Columns Containing Missing Values | 10                |
|   5 | Columns Without Missing Values    | 26                |
|   6 | Highest Missing Value Column      | `Return_Reason`   |
|   7 | Second-Highest Column             | `Promotion_Code`  |
|   8 | Third-Highest Column              | `Customer_Rating` |

### Summary

* 🟢 The majority of data cells are populated.
* 🟠 Missing values are concentrated in a small number of columns.
* 🔴 `Return_Reason` requires further investigation.
* 🔴 `Promotion_Code` and `Customer_Rating` also contain substantial missing values.
* 🔎 Additional validation is necessary before data cleaning.

---

## 💡 07 — Recommendations

| Area                 | Recommended Action                                                    |
| :------------------- | :-------------------------------------------------------------------- |
| `Return_Reason`      | Compare missing values against `Return_Flag`.                         |
| `Promotion_Code`     | Check whether orders without promotions have blank codes.             |
| `Customer_Rating`    | Determine whether ratings are optional or unsubmitted.                |
| Customer Information | Investigate missing names, ages, and genders.                         |
| Product Information  | Validate missing product names against product identifiers.           |
| Payment Information  | Investigate missing payment methods.                                  |
| Delivery Information | Check missing delivery durations against order status.                |
| Data Cleaning        | Avoid deleting or filling values without understanding their meaning. |

---

## 📝 08 — Conclusion

The missing values analysis identified **30,479 missing data cells**, representing **4.69% of all data cells**.

Although the overall missing percentage is relatively low, the missing values are unevenly distributed across the dataset.

The `Return_Reason` column has the highest number of missing values, followed by `Promotion_Code` and `Customer_Rating`.

Further investigation is necessary to distinguish legitimate missing values from actual data quality problems before performing data cleaning.

This analysis provides a foundation for the next stage of the project:

**➡️ Task 03 — Data Cleaning & Preparation**

---

<div align="center">

### ✅ TASK 02 COMPLETED

**Retail Sales & Profitability Analysis**

![Python](https://img.shields.io/badge/Built_with-Python-3776AB?style=flat-square\&logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Powered_by-Pandas-150458?style=flat-square\&logo=pandas\&logoColor=white)

*Turning raw data into meaningful insights.*

</div>
