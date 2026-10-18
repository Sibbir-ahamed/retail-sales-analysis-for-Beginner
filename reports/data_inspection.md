# Data Inspection Report

## 1. Dataset Overview

* Total Rows: 18045
* Total Columns: 36

## 2. Column Information

All the columns name
['Transaction_ID', 'Order_ID', 'Customer_ID', 'Customer_Name', 'Customer_Age', 'Customer_Gender', 'Customer_Segment', 'Order_Date', 'Order_Time', 'Sales_Channel', 'Store_ID', 'Store_Name', 'Country', 'Region', 'City', 'Product_ID', 'Product_Name', 'Product_Category', 'Product_Subcategory', 'Quantity', 'Unit_Price', 'Discount_Percentage', 'Sales_Amount', 'Cost_Amount', 'Profit', 'Payment_Method', 'Order_Status', 'Shipping_Method', 'Delivery_Days', 'Return_Flag', 'Return_Reason', 'Sales_Representative', 'Promotion_Code', 'Customer_Rating', 'Inventory_Level', 'Order_Year']

## 3. Data Types

 #   Column                Non-Null Count  Dtype
---  ------                --------------  -----
 0   Transaction_ID        18045 non-null  str
 1   Order_ID              18045 non-null  str
 2   Customer_ID           18045 non-null  str
 3   Customer_Name         17937 non-null  str
 4   Customer_Age          17827 non-null  float64
 5   Customer_Gender       17883 non-null  str    
 6   Customer_Segment      18045 non-null  str    
 7   Order_Date            18045 non-null  str    
 8   Order_Time            18045 non-null  str    
 9   Sales_Channel         18045 non-null  str
 10  Store_ID              18045 non-null  str    
 11  Store_Name            18045 non-null  str    
 12  Country               18045 non-null  str    
 13  Region                18045 non-null  str    
 14  City                  18045 non-null  str    
 15  Product_ID            18045 non-null  str    
 16  Product_Name          17901 non-null  str
 17  Product_Category      18045 non-null  str    
 18  Product_Subcategory   18045 non-null  str    
 19  Quantity              18045 non-null  int64  
 20  Unit_Price            18045 non-null  float64
 21  Discount_Percentage   18045 non-null  float64
 22  Sales_Amount          18045 non-null  float64
 23  Cost_Amount           18045 non-null  float64
 24  Profit                18045 non-null  float64
 25  Payment_Method        17898 non-null  str    
 26  Order_Status          18045 non-null  str    
 27  Shipping_Method       18045 non-null  str    
 28  Delivery_Days         17883 non-null  float64
 29  Return_Flag           18045 non-null  str    
 30  Return_Reason         1877 non-null   str    
 31  Sales_Representative  18045 non-null  str
 32  Promotion_Code        8308 non-null   str    
 33  Customer_Rating       14610 non-null  float64
 34  Inventory_Level       17847 non-null  float64
 35  Order_Year            18045 non-null  int64
dtypes: float64(9), int64(2), str(25)

## Missing Values
Missing values:
Customer_Name        108
Customer_Age         218
Customer_Gender      162
Product_Name         144
Payment_Method       147
Delivery_Days        162
Return_Reason      16168
Promotion_Code      9737
Customer_Rating     3435
Inventory_Level      198

## 4. Summary statistics:
```text
Summary statistics:
       Customer_Age      Quantity    Unit_Price  Discount_Percentage  Sales_Amount   Cost_Amount        Profit  Delivery_Days  Customer_Rating  Inventory_Level    Order_Year
count  17827.000000  18045.000000  18045.000000         18045.000000  18045.000000  18045.000000  18045.000000   17883.000000     14610.000000     17847.000000  18045.000000
mean      38.916924      2.127127    232.685633             6.256858    457.309027    366.001156     91.404131       2.262204         3.985969        70.257914   2023.566417
std       10.727357      1.786212    294.208022             6.881178    856.597181    705.866738    167.827883       2.321656         1.008422        22.042609      1.118744
min        4.000000     -3.000000     21.390000             0.000000     16.680000     12.170000   -299.310000       0.000000         1.000000         0.000000   2022.000000
25%       32.000000      1.000000     53.380000             0.000000     78.530000     56.120000     19.480000       0.000000         4.000000        55.000000   2023.000000
50%       39.000000      2.000000     99.870000             5.000000    168.810000    122.300000     40.190000       1.000000         4.000000        70.000000   2024.000000
75%       46.000000      3.000000    285.580000            10.000000    472.450000    376.020000     93.270000       4.000000         5.000000        85.000000   2025.000000
max      112.000000     11.000000   1425.090000           110.000000  14303.070000  10791.000000   3512.080000      10.000000         5.000000       157.000000   2025.000000
```

## 5. Initial Observations

## 5. Initial Observations

1. **Dataset Size:** The dataset contains 18,045 rows and 36 columns, covering customer, transaction, product, sales, profit, payment, delivery, and return information.

2. **Data Types:** The dataset contains 25 string columns, 9 float64 columns, and 2 int64 columns.

3. **Customer Information:** The average customer age is approximately 38.92 years. However, the minimum age is 4 and the maximum age is 112, so the age values should be validated.

4. **Sales and Profit:** The average Sales_Amount is approximately 457.31, while the average Profit is approximately 91.40. Profit also contains negative values, with a minimum of -299.31.

5. **Quantity:** The average quantity is approximately 2.13 units per record. The minimum quantity is -3, which requires investigation to determine whether it represents a return, adjustment, or data quality issue.

6. **Discount:** The average discount percentage is approximately 6.26%. However, the maximum value is 110%, which appears unusual and should be validated.

7. **Customer Ratings:** The average customer rating is approximately 3.99 out of 5. However, ratings are missing from some records.

8. **Delivery:** The average delivery time is approximately 2.26 days. Some records have a delivery time of zero days, which may be valid but requires context.

9. **Business Analysis Opportunities:** The dataset can support further analysis of sales trends, product performance, profitability, customer segments, regional performance, promotions, delivery, and product returns.


## 6. Data Quality Notes

[Record any missing-value concerns or unusual data types observed. Duplicate records have not yet been investigated.]

## 6. Next Steps

* Investigate missing values.
* Check for duplicate records.
* Validate data types.
* Begin exploratory data analysis.
