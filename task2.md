ঠিক আছে! 👨‍💼 এখন থেকে আমি তোমার Data Analysis Manager, আর তুমি আমার Junior Data Analyst।

তোমার **Task 01 — Dataset Inspection** সম্পন্ন হয়েছে। এবার আমরা Task 02 শুরু করব। আগের মতোই VS Code-এ Python Script লিখবে, শুধু Pandas ব্যবহার করবে এবং প্রতিটি Task GitHub Portfolio-এর জন্য সুন্দরভাবে সাজাবে।

# 📊 TASK 02 — Missing Values Analysis

**Project:** Retail Sales & Profitability Analysis
**Department:** Data Analytics
**Your Position:** Junior Data Analyst
**Difficulty:** Beginner
**Tool:** Python + Pandas
**Dataset:** `Sales_transactions_2022_2025.csv`
**Estimated Time:** ৩০–৪৫ মিনিট

---

# ১. Business Scenario — তোমার কাজ কেন গুরুত্বপূর্ণ?

ধরো, তুমি একটি Retail কোম্পানিতে Junior Data Analyst হিসেবে কাজ করছ।

কোম্পানি তোমাকে ২০২২–২০২৫ সালের বিক্রয়সংক্রান্ত Dataset দিয়েছে।

ম্যানেজমেন্ট জানতে চায়:

* কোন Column-এ Missing Values আছে?
* কোন Column-এ সবচেয়ে বেশি Missing Values রয়েছে?
* মোট কতটি Missing Value আছে?
* কোন Column-এ Missing Values বেশি হওয়ায় ভবিষ্যৎ Analysis প্রভাবিত হতে পারে?
* Missing Values কি সত্যিই ভুল, নাকি ব্যবসার স্বাভাবিক প্রক্রিয়ার কারণে তৈরি হয়েছে?

তোমার দায়িত্ব হলো এই প্রশ্নগুলোর উত্তর বের করা।

**গুরুত্বপূর্ণ:** তুমি এখনো কোনো Missing Value পূরণ করবে না বা কোনো Row Delete করবে না। প্রথমে শুধু বিশ্লেষণ করবে।

---

# ২. Task 02-তে কী কী করতে হবে?

তোমাকে মোট ৬টি কাজ করতে হবে।

| Task | কাজ                         | কী জানতে পারবে                                                 |
| ---- | --------------------------- | -------------------------------------------------------------- |
| 2.1  | Missing Values Count        | প্রতিটি Column-এ কতটি Missing Value আছে                        |
| 2.2  | Missing Values Percentage   | প্রতিটি Column-এর কত শতাংশ Value Missing                       |
| 2.3  | Columns with Missing Values | কোন কোন Column-এ Missing Values রয়েছে                          |
| 2.4  | Total Missing Values        | পুরো Dataset-এ মোট Missing Cell কতটি                           |
| 2.5  |alu Highest Missing Ves      | কোন Column-এ সবচেয়ে বেশি Missing Values রয়েছে                  |
| 2.6  | Business Interpretation     | Missing Values ব্যবসায়িক Analysis-কে কীভাবে প্রভাবিত করতে পারে |

এবার প্রতিটি কাজ বুঝে নিই।

---

# 🟢 TASK 2.1 — Count Missing Values

### তোমার কাজ

প্রতিটি Column-এ কতটি Missing Value আছে, তা বের করবে।

তুমি আগেই শিখেছ:

```python
df.isnull().sum()
```

এটি প্রতিটি Column-এর Missing Value-এর সংখ্যা দেখাবে।

### কেন প্রয়োজন?

তোমার Dataset-এ আগের Inspection থেকে আমরা জানি:

| Column          | Missing Values |
| --------------- | -------------: |
| Customer_Name   |            108 |
| Customer_Age    |            218 |
| Customer_Gender |            162 |
| Product_Name    |            144 |
| Payment_Method  |            147 |
| Delivery_Days   |            162 |
| Return_Reason   |         16,168 |
| Promotion_Code  |          9,737 |
| Customer_Rating |          3,435 |
| Inventory_Level |            198 |

এগুলো তোমার আগের `df.info()` Output থেকে পাওয়া সংখ্যা।

এখন তোমার কাজ হলো Pandas দিয়ে আবার Missing Values Count বের করে ফলাফল যাচাই করা।

**Manager's Question:** কোন Column-এ সবচেয়ে বেশি Missing Values রয়েছে?

---

# 🟢 TASK 2.2 — Missing Values Percentage

শুধু Missing Values-এর সংখ্যা জানলেই হবে না। মোট ডেটার তুলনায় কত শতাংশ Value Missing, সেটাও জানতে হবে।


### একটি উদাহরণ

ধরো, একটি Dataset-এ ১০০টি Row আছে।

একটি Column-এ ২০টি Missing Value রয়েছে।

তাহলে:

$$
\text{Missing Percentage}=\frac{20}{100}\times100=20\%
$$

অর্থাৎ, Column-টির ২০% Value Missing।

### তোমার কাজ

প্রতিটি Column-এর Missing Value Percentage বের করবে।

নিচের সূত্রটি মনে রাখবে:

Percentage= যে অংশ বের করতে চাই​ / মোট সংখ্যা × 100

**Manager's Question:** `Customer_Rating` Column-এর কত শতাংশ Value Missing?

এই প্রশ্নের উত্তর তোমাকে প্রকৃত Output থেকে বের করতে হবে।

---

# 🟢 TASK 2.3 — Identify Columns with Missing Values

তোমার Dataset-এ ৩৬টি Column রয়েছে।

সব Column-এর ফলাফল দেখার পাশাপাশি শুধু যেসব Column-এ Missing Values রয়েছে, সেগুলো আলাদা করে শনাক্ত করবে।

উদাহরণস্বরূপ, নিচের মতো একটি Report তৈরি হতে পারে:

| Column         | Missing Values |
| -------------- | -------------: |
| Customer_Name  |            108 |
| Customer_Age   |            218 |
| Return_Reason  |         16,168 |
| Promotion_Code |          9,737 |

এটি একটি উদাহরণমূলক অংশ, সম্পূর্ণ তালিকা নয়।

### তোমার কাজ

* Missing Values থাকা Column-গুলোর নাম বের করবে।
* প্রতিটি Column-এর Missing Value Count দেখাবে।
* Missing Values নেই এমন Column-গুলোকে এই তালিকায় রাখবে না।

### কেন প্রয়োজন?

এতে দ্রুত বোঝা যাবে কোন Column-গুলোতে আরও Investigation প্রয়োজন।

---

# 🟢 TASK 2.4 — Calculate Total Missing Values

এবার পুরো Dataset-এ মোট কতটি Missing Cell আছে, তা বের করবে।

মনে রাখবে, এখানে **মোট Missing Cell** গণনা করতে হবে, Missing Values থাকা Column-এর সংখ্যা নয়।

উদাহরণ:

| Column        | Missing Values |
| ------------- | -------------: |
| Customer_Name |              5 |
| Customer_Age  |              3 |
| Product_Name  |              2 |

মোট Missing Values:

$$
5+3+2=10
$$

এখানে মোট Missing Cell হলো ১০টি।

### তোমার কাজ

তোমার ১৮,০৪৫ Row ও ৩৬ Column-এর Dataset-এ মোট Missing Values কতটি, তা বের করবে।

---

# 🟢 TASK 2.5 — Find the Column with the Highest Missing Values

এখন খুঁজে বের করবে কোন Column-এ সবচেয়ে বেশি Missing Values রয়েছে।

তোমার আগের Output অনুযায়ী:

* `Return_Reason`: 16,168
* `Promotion_Code`: 9,737
* `Customer_Rating`: 3,435

এই তিনটি Column-এর মধ্যে `Return_Reason`-এ সবচেয়ে বেশি Missing Values রয়েছে।

তবে মনে রাখবে, **সব Missing Values-কে Data Quality Error বলা যাবে না।**

উদাহরণস্বরূপ:

* কোনো Order Return না হলে `Return_Reason` ফাঁকা থাকা স্বাভাবিক হতে পারে।
* কোনো Promotion ব্যবহার না করলে `Promotion_Code` ফাঁকা থাকা স্বাভাবিক হতে পারে।
* কোনো Customer Rating না দিলে `Customer_Rating` ফাঁকা থাকতে পারে।

এগুলো নিশ্চিত করার জন্য পরবর্তী সময়ে সংশ্লিষ্ট Column-এর ব্যবসায়িক অর্থ ও অন্যান্য তথ্য পরীক্ষা করতে হবে।

### তোমার কাজ

নিচের প্রশ্নগুলোর উত্তর দেবে:

১. কোন Column-এ সবচেয়ে বেশি Missing Values রয়েছে?

২. দ্বিতীয় সর্বোচ্চ Missing Values কোন Column-এ রয়েছে?

৩. কোন Column-গুলোতে Missing Values তুলনামূলক কম?

৪. Missing Values-এর সংখ্যা বেশি হলেই কি সেটিকে ভুল Data বলতে পারি? কেন?

missing = df.isnull().sum()

missing_sorted = missing.sort_values(ascending=False)

second_highest = missing_sorted.iloc[1]

print("Second Highest Column:", second_highest.name)
print("Missing Values:", second_highest)



---

# 🟢 TASK 2.6 — Business Interpretation

এটাই তোমার সবচেয়ে গুরুত্বপূর্ণ কাজ।

এখানে শুধু সংখ্যা লিখবে না; বরং সংখ্যাগুলো ব্যবসার জন্য কী অর্থ বহন করতে পারে, তা ব্যাখ্যা করবে।

### উদাহরণ ১: Customer Rating

ধরো, অনেক Customer-এর Rating অনুপস্থিত।

এতে Customer Satisfaction বিশ্লেষণ করতে গেলে সমস্যা হতে পারে, কারণ সব Customer-এর Feedback পাওয়া যাচ্ছে না।

### উদাহরণ ২: Customer Age

Customer Age অনুপস্থিত থাকলে বয়সভিত্তিক Customer Segmentation অসম্পূর্ণ হতে পারে।

### উদাহরণ ৩: Promotion Code

Promotion Code অনুপস্থিত থাকলে বোঝা কঠিন হতে পারে কোনো Order-এ Promotion ব্যবহার করা হয়নি, নাকি তথ্যটি সংরক্ষিত হয়নি।

এটি বোঝার জন্য আরও Investigation প্রয়োজন।

### তোমার কাজ

তোমার প্রকৃত ফলাফল ব্যবহার করে অন্তত ৫টি Business Observation লিখবে।

প্রতিটি Observation-এ দুটি বিষয় থাকবে:

1. কী পেয়েছ?
2. সেটি ব্যবসায়িক Analysis-এর জন্য কেন গুরুত্বপূর্ণ?

---

# ৩. VS Code-এ কীভাবে কাজ করবে?

তোমার বর্তমান Project Structure পরিবর্তন করতে হবে না।

```text
retail-sales-analysis/
│
├── data/
│   └── Sales_transactions_2022_2025.csv
│
├── src/
│   └── data_inspection.py
│
├── reports/
│   ├── data_inspection_report.md
│   └── missing_values_report.md
│
├── requirements.txt
└── README.md
```

Task 01-এর কোড মুছে ফেলবে না।

বরং `src` ফোল্ডারে নতুন একটি Python ফাইল তৈরি করো:

`missing_values_analysis.py`

এভাবে Task 01 ও Task 02-এর কোড আলাদা থাকবে।

---

# ৪. তোমার Coding Assignment

নিচের কাজগুলোর জন্য নিজে Pandas Code লিখবে।

```python
import pandas as pd

# Load Dataset
df = pd.read_csv(
    r"E:\Data_Analysis sheet\retail\data\Sales_transactions_2022_2025.csv"
)

# Task 2.1: Count missing values in each column


# Task 2.2: Calculate missing value percentage


# Task 2.3: Display only columns containing missing values


# Task 2.4: Calculate total missing values


# Task 2.5: Identify the column with the highest missing values


# Task 2.6: Write business observations
```

**এটি তোমার Assignment Template।** প্রতিটি অংশের Code নিজে লিখবে।

আমি ইচ্ছা করেই সম্পূর্ণ Solution দিচ্ছি না, কারণ তুমি বাস্তব Data Analyst-এর মতো চিন্তা করতে শিখছ।

একটি বিষয় মনে রাখবে: আমরা এখানে শুধু Pandas ব্যবহার করছি। NumPy, SQL বা অন্য কোনো লাইব্রেরি প্রয়োজন নেই।

---

# ৫. Task 02-এর Success Checklist

কাজ শেষ হলে নিচের Checklist মিলিয়ে দেখবে।

* [ ] প্রতিটি Column-এর Missing Values Count বের করেছি।
* [ ] প্রতিটি Column-এর Missing Values Percentage বের করেছি।
* [ ] Missing Values থাকা Column-গুলো আলাদা করেছি।
* [ ] Dataset-এর Total Missing Values বের করেছি।
* [ ] সর্বোচ্চ Missing Values থাকা Column শনাক্ত করেছি।
* [ ] Missing Values-এর সংখ্যা অনুযায়ী Column-গুলো তুলনা করেছি।
* [ ] Missing Values-এর Business Impact ব্যাখ্যা করেছি।
* [ ] `missing_values_report.md` তৈরি করেছি।
* [ ] Python Script সফলভাবে চালিয়েছি।
* [ ] কোনো Missing Value পূরণ বা Delete করিনি।
* [ ] কোনো Data পরিবর্তন করিনি।

---

# ৬. Manager-এর কাছে কী জমা দেবে?

Task শেষ হলে আমাকে তিনটি জিনিস পাঠাবে:

**১. Python Code:** `missing_values_analysis.py`

**২. Terminal Output:** Missing Values Count, Percentage, Total এবং Highest Missing Values-এর ফলাফল।

**৩. Business Observation:** অন্তত ৫টি পর্যবেক্ষণ।

আমি তোমার Code ও Output Review করব। কোনো ভুল থাকলে তোমাকে সংশোধন করতে বলব।

সবকিছু সঠিক হলে Task 02 সম্পন্ন হবে।

## 👨‍💼 শেষ নির্দেশনা

**এখন শুধু Task 2.1 দিয়ে শুরু করো।**

প্রথমে প্রতিটি Column-এর Missing Values Count বের করার Code লেখো এবং Terminal Output দেখো। একসঙ্গে ছয়টি Task করার দরকার নেই।

তুমি Code ও Output পাঠালে আমি Review করব। তারপর আমরা Task 2.2-তে যাব।

এভাবেই ধাপে ধাপে তুমি Pandas শিখবে এবং GitHub-এর জন্য একটি বাস্তব Data Analysis Portfolio তৈরি করবে।













