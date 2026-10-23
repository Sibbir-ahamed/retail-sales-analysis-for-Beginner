ঠিক আছে! 👨‍💼 তোমার Manager হিসেবে এবার তোমাকে একটু কঠিন Task দিচ্ছি। এবার শুধু Pandas-এর Method ব্যবহার করতে পারলেই হবে না, **ডেটা যাচাই করে সমস্যা শনাক্ত করতে হবে এবং Business Context অনুযায়ী সিদ্ধান্ত নিতে হবে।**

তুমি Task 01-এ Dataset Inspection এবং Task 02-এ Missing Values Analysis সম্পন্ন করেছ। তাই Task 03-এ আমরা পরবর্তী ধাপে যাব।

# 📊 TASK 03 — Data Quality Audit & Validation

**Project:** Retail Sales & Profitability Analysis
**Position:** Junior Data Analyst
**Difficulty:** Intermediate 🟠
**Tools:** Python, Pandas, VS Code
**Dataset:** `Sales_transactions_2022_2025.csv`
**Submission:** Python Script + Excel Report + GitHub Documentation

## 🎯 Business Scenario

তোমার কোম্পানির ম্যানেজার লক্ষ্য করেছেন, Dataset-এ কিছু অস্বাভাবিক তথ্য রয়েছে।

উদাহরণস্বরূপ, প্রাথমিক Inspection-এ দেখা গেছে:

* `Quantity`-এর Minimum Value হলো `-3`।
* `Discount_Percentage`-এর Maximum Value হলো `110`।
* `Customer_Age`-এর Maximum Value হলো `112`।
* `Profit`-এ Negative Value রয়েছে।
* `Order_Date` String হিসেবে সংরক্ষিত।

ম্যানেজমেন্ট জানতে চায়:

**এই তথ্যগুলো কি সত্যিকারের Data Quality Problem, নাকি ব্যবসার স্বাভাবিক কার্যক্রমের অংশ?**

তোমার কাজ হলো Data Quality Audit করে সম্ভাব্য সমস্যা শনাক্ত করা এবং প্রতিটি সমস্যার পক্ষে প্রমাণ উপস্থাপন করা।

---

# 📝 TASK 3.1 — Duplicate Records Analysis

প্রথমে পরীক্ষা করবে Dataset-এ Duplicate Record আছে কি না।

### তোমার কাজ

১. সম্পূর্ণ Row Duplicate হয়েছে কি না, তা বের করবে।

২. মোট কতটি Duplicate Row রয়েছে, তা গণনা করবে।

৩. Duplicate Row-এর Percentage বের করবে।

৪. Duplicate Row থাকলে সেগুলো পরীক্ষা করবে।

### Manager-এর প্রশ্ন

* Dataset-এ কতটি Duplicate Row আছে?
* Duplicate Row-এর Percentage কত?
* Duplicate Record পাওয়া গেলে কি সঙ্গে সঙ্গে Delete করা উচিত? কেন?

**শর্ত:** এখনই কোনো Duplicate Row Delete করবে না।

---

# 📝 TASK 3.2 — Date Validation

তোমার Dataset-এ `Order_Date` Column বর্তমানে String হিসেবে রয়েছে।

Date অনুযায়ী Sales Trend বিশ্লেষণ করতে হলে Date-কে সঠিকভাবে Handle করা প্রয়োজন।

### তোমার কাজ

১. `Order_Date`-এর বর্তমান Data Type পরীক্ষা করবে।

২. Date-গুলো সঠিক Format-এ আছে কি না যাচাই করবে।

৩. কোন কোন Date Parse করা যাচ্ছে না, তা শনাক্ত করবে।

৪. Date Range পরীক্ষা করবে।

৫. Dataset-এর সর্বপ্রথম এবং সর্বশেষ Order Date বের করবে।

### Manager-এর প্রশ্ন

* `Order_Date` কি DateTime হিসেবে ব্যবহার করার উপযোগী?
* কোনো Invalid Date থাকলে কীভাবে শনাক্ত করবে?
* Date Format সঠিক না হলে Sales Trend Analysis-এ কী সমস্যা হতে পারে?

**শর্ত:** মূল Dataset পরিবর্তন করবে না। প্রয়োজনে আলাদা পরীক্ষামূলক Series বা DataFrame ব্যবহার করবে।

---

# 📝 TASK 3.3 — Numerical Value Validation

এবার কয়েকটি গুরুত্বপূর্ণ Numerical Column পরীক্ষা করবে।

নিচের Column-গুলো নিয়ে কাজ করবে:

| Column                | কী যাচাই করবে                |
| --------------------- | ---------------------------- |
| `Customer_Age`        | অস্বাভাবিক বয়স               |
| `Quantity`            | Negative বা Zero Quantity    |
| `Unit_Price`          | Zero বা Negative Price       |
| `Discount_Percentage` | অস্বাভাবিক Discount          |
| `Sales_Amount`        | Zero বা Negative Sales       |
| `Cost_Amount`         | Zero বা Negative Cost        |
| `Profit`              | Negative Profit              |
| `Delivery_Days`       | Negative Delivery Days       |
| `Customer_Rating`     | অনুমোদিত সীমার বাইরের Rating |

### তোমার কাজ

প্রতিটি Column-এর জন্য:

১. Minimum Value বের করবে।

২. Maximum Value বের করবে।

৩. Negative Value-এর সংখ্যা বের করবে, যেখানে এটি প্রাসঙ্গিক।

৪. Zero Value-এর সংখ্যা বের করবে, যেখানে এটি প্রাসঙ্গিক।

৫. সম্ভাব্য অস্বাভাবিক Value-এর সংখ্যা বের করবে।

### গুরুত্বপূর্ণ Business Rules

কিছু Rule প্রাথমিকভাবে ব্যবহার করতে পারো:

| Column                | প্রাথমিক Validation Rule          |
| --------------------- | --------------------------------- |
| `Customer_Age`        | Negative Age অস্বাভাবিক           |
| `Quantity`            | Negative Quantity তদন্ত করতে হবে  |
| `Unit_Price`          | Negative Price তদন্ত করতে হবে     |
| `Discount_Percentage` | 0–100-এর বাইরে হলে তদন্ত করতে হবে |
| `Customer_Rating`     | 1–5-এর বাইরে হলে তদন্ত করতে হবে   |
| `Delivery_Days`       | Negative হলে তদন্ত করতে হবে       |

**মনে রাখবে:** এগুলো প্রাথমিক Validation Rule, চূড়ান্ত Business Rule নয়। যেমন, Negative Quantity Return বা Adjustment বোঝাতে পারে। Negative Profit বাস্তব ক্ষতি বোঝাতে পারে। তাই কোনো Value-কে প্রমাণ ছাড়া ভুল বলবে না।

### Manager-এর প্রশ্ন

* কোন Column-এ সবচেয়ে বেশি সম্ভাব্য অস্বাভাবিক Value রয়েছে?
* কোন অস্বাভাবিক Value ব্যবসার স্বাভাবিক কার্যক্রমের অংশ হতে পারে?
* কোন Value-গুলো যাচাই করার জন্য অতিরিক্ত তথ্য প্রয়োজন?

---

# 📝 TASK 3.4 — Date Range ও Order Year Consistency

তোমার Dataset-এ দুটি গুরুত্বপূর্ণ Column রয়েছে:

* `Order_Date`
* `Order_Year`

এবার পরীক্ষা করবে, এই দুটি Column-এর মধ্যে কোনো অসংগতি রয়েছে কি না।

### তোমার কাজ

১. `Order_Date` থেকে Year নির্ধারণ করবে।

২. সেটিকে `Order_Year`-এর সঙ্গে তুলনা করবে।

৩. দুই Column-এর Year না মিললে সেই Record-গুলো শনাক্ত করবে।

৪. মোট কতটি Record-এ Year Mismatch রয়েছে, তা বের করবে।

### উদাহরণ

| Order_Date | Order_Year | Result   |
| ---------- | ---------: | -------- |
| 2022-05-10 |       2022 | Match    |
| 2023-08-15 |       2024 | Mismatch |
| 2025-02-20 |       2025 | Match    |

এটি কেবল উদাহরণ।

**Manager-এর প্রশ্ন:** `Order_Date` এবং `Order_Year`-এর মধ্যে অসংগতি থাকলে Year-wise Sales Analysis কতটা নির্ভরযোগ্য হবে?

---

# 📝 TASK 3.5 — Create a Data Quality Summary

এবার তোমার সমস্ত ফলাফল এক জায়গায় সাজাবে।

একজন Data Analyst শুধু সমস্যা শনাক্ত করে না; সে এমন Report তৈরি করে, যাতে Manager সহজে সিদ্ধান্ত নিতে পারেন।

### তোমার রিপোর্টে থাকবে

| Validation Check        | Result        |
| ----------------------- | ------------- |
| Total Rows              | প্রকৃত সংখ্যা |
| Duplicate Rows          | প্রকৃত সংখ্যা |
| Invalid Date Count      | প্রকৃত সংখ্যা |
| Negative Quantity Count | প্রকৃত সংখ্যা |
| Invalid Discount Count  | প্রকৃত সংখ্যা |
| Invalid Rating Count    | প্রকৃত সংখ্যা |
| Order Year Mismatch     | প্রকৃত সংখ্যা |

এখানে সব Result কোড থেকে গণনা করবে। অনুমান করে সংখ্যা লিখবে না।

---

# 📁 Project Structure

তোমার প্রজেক্ট এবার এভাবে সাজাতে পারো:

```text
retail-sales-analysis/
│
├── data/
│   └── Sales_transactions_2022_2025.csv
│
├── src/
│   ├── data_inspection.py
│   ├── missing_values_analysis.py
│   └── data_quality_audit.py
│
├── reports/
│   ├── data_inspection_report.md
│   ├── Task_02_Missing_Values_Report.xlsx
│   ├── Task_03_Data_Quality_Report.xlsx
│   └── Task_03_Data_Quality_Observations.md
│
├── requirements.txt
└── README.md
```

Task 01 ও Task 02-এর ফাইলগুলো পরিবর্তন না করে রাখবে। নতুন Task-এর জন্য নতুন Script তৈরি করবে।

---

# ⚠️ Manager-এর কঠোর নির্দেশনা

এই Task-এ কিছু বিষয় অবশ্যই মেনে চলবে:

* শুধু Pandas ব্যবহার করবে।
* NumPy, SQL বা Visualization Library ব্যবহার করবে না।
* কোনো Row Delete করবে না।
* কোনো Missing Value পূরণ করবে না।
* কোনো Original Value পরিবর্তন করবে না।
* সব অস্বাভাবিক Value-কে ভুল Data হিসেবে চিহ্নিত করবে না।
* প্রতিটি সিদ্ধান্তের পক্ষে Data-ভিত্তিক প্রমাণ দেখাবে।

তোমার বর্তমান কাজ হলো **Data Quality Audit**, Data Cleaning নয়।

---

# ✅ TASK 03 — Success Checklist

* [ ] Duplicate Rows পরীক্ষা করেছি।
* [ ] Duplicate Row-এর Percentage গণনা করেছি।
* [ ] `Order_Date` Validation করেছি।
* [ ] Date Range শনাক্ত করেছি।
* [ ] Numerical Columns-এর Minimum ও Maximum পরীক্ষা করেছি।
* [ ] সম্ভাব্য অস্বাভাবিক Value শনাক্ত করেছি।
* [ ] Negative Quantity ও Negative Profit পরীক্ষা করেছি।
* [ ] Discount ও Rating-এর সীমা যাচাই করেছি।
* [ ] `Order_Date` এবং `Order_Year` তুলনা করেছি।
* [ ] Data Quality Summary তৈরি করেছি।
* [ ] Business Observations লিখেছি।
* [ ] Python Script সফলভাবে চালিয়েছি।
* [ ] কোনো Original Data পরিবর্তন করিনি।

---

## 👨‍💼 Manager-এর নির্দেশনা: এখনই সব Task শুরু করবে না

তুমি নতুন, তাই ধাপে ধাপে কাজ করবে।

### তোমার প্রথম Assignment: TASK 3.1 — Duplicate Records Analysis

প্রথমে শুধু Duplicate Records নিয়ে কাজ করো।

আমাকে পাঠাবে:

1. তোমার Python Code।
2. Total Duplicate Rows।
3. Duplicate Percentage।
4. তোমার Business Observation।

আমি তোমার কোড Review করব। সঠিক হলে পরবর্তী Task, অর্থাৎ **3.2 — Date Validation**, শুরু করতে বলব।

**এবার তোমার লক্ষ্য শুধু কোড লেখা নয়; একজন Data Analyst-এর মতো সমস্যা শনাক্ত করা, প্রমাণ দেখানো এবং যুক্তিসংগত সিদ্ধান্ত নেওয়া।**
