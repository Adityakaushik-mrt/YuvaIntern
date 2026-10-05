# Sales Exploratory Data Analysis Using Python

## 📌 Project Overview

This project performs an **Exploratory Data Analysis (EDA)** on a pizza sales transaction dataset using Python. The objective is to understand customer purchasing patterns, transaction amounts, pizza categories, pizza sizes, and relationships between numerical business metrics.

The analysis is performed using **Pandas, NumPy, Matplotlib, and Seaborn**. The project follows a structured data-analysis workflow including data loading, data inspection, data-quality checking, statistical analysis, visualization, outlier detection, and correlation analysis.

The dataset contains **50,000 transaction records and 20 columns**, including order information, customer information, pizza details, pricing, discounts, GST, total transaction amount, order type, payment method, month, day of week, hour, and discount category.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Understand the structure and characteristics of the pizza transaction dataset.
* Inspect the dataset for missing values and data-quality issues.
* Perform descriptive statistical analysis.
* Analyze the distribution of total transaction amounts.
* Compare average transaction amounts across different pizza sizes.
* Identify variability and potential outliers using box plots.
* Analyze relationships between numerical variables using a correlation matrix.
* Generate meaningful business insights from the data.
* Present analytical findings through clear and professional visualizations.

---

## 🗂️ Dataset Information

The dataset contains **50,000 rows and 20 columns**.

### Important Columns

| Column              | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `order_id`          | Unique order identifier                               |
| `order_date`        | Date of the order                                     |
| `order_time`        | Time of the order                                     |
| `store_id`          | Store identifier                                      |
| `city`              | City where the order was placed                       |
| `customer_id`       | Customer identifier                                   |
| `pizza_name`        | Name of the pizza                                     |
| `category`          | Pizza category                                        |
| `size`              | Pizza size                                            |
| `quantity`          | Number of pizzas ordered                              |
| `unit_price`        | Price per pizza                                       |
| `discount`          | Discount applied to the transaction                   |
| `gst`               | GST amount                                            |
| `total_amount`      | Final transaction amount                              |
| `order_type`        | Type of order, such as Delivery, Dine-in, or Takeaway |
| `payment_method`    | Payment method used                                   |
| `Month`             | Month of the transaction                              |
| `day Of Week`       | Day on which the order was placed                     |
| `Hour`              | Hour of the transaction                               |
| `Discount Category` | Classification of discount level                      |

---

## 🛠️ Technologies & Libraries Used

* **Python**
* **Pandas** – Data loading, inspection, grouping, and analysis
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization

### Installation

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn
```

---

## 🔍 Project Workflow

### 1. Import Libraries

The project imports the required Python libraries:

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
```

A Seaborn visualization theme is also configured for improved chart presentation.

---

### 2. Load the Dataset

The dataset is loaded using Pandas:

```python
df = pd.read_csv('SQL.csv')
```

The first few records are inspected using:

```python
df.head()
```

---

### 3. Data Inspection

The project examines the structure of the dataset using:

```python
df.info()
```

and generates descriptive statistics using:

```python
df.describe()
```

The dataset contains:

* **50,000 records**
* **20 columns**
* Numerical and categorical variables
* Pricing, discount, GST, and transaction-value information

---

### 4. Missing Value Analysis

Missing values are checked using:

```python
df.isnull().sum()
```

This step helps verify the completeness and quality of the dataset before performing exploratory analysis.

---

# 📊 Exploratory Data Analysis

## 5. Distribution of Total Transaction Amount

A histogram with KDE is used to analyze the distribution of `total_amount`.

The analysis calculates both:

* Mean transaction amount
* Median transaction amount

The visualization helps understand customer spending behavior and identify whether transaction values are normally distributed or skewed.

### Key Insight

The transaction-value distribution is **right-skewed**. Most transactions fall approximately between **₹300 and ₹800**, while higher-value transactions extend beyond ₹1,500 and in some cases above ₹3,000.

Because these high-value transactions pull the average upward, the **median provides a more representative measure of typical customer spending**.

---

## 6. Average Transaction Amount by Pizza Size

The project groups transactions by `size` and calculates the average `total_amount`.

```python
avg_data = (
    df.groupby("size")["total_amount"]
      .mean()
      .sort_values()
)
```

A horizontal bar chart is used to compare the average transaction amount across pizza sizes.

### Business Value

This analysis helps identify:

* Higher-performing pizza sizes
* Lower-performing sizes
* Differences in average customer spending
* Potential opportunities for pricing and promotional strategies

---

## 7. Spread and Outlier Detection

A Seaborn box plot is used to analyze transaction-value variation across different pizza names.

```python
sns.boxplot(
    x="pizza_name",
    y="total_amount",
    data=df,
    hue="category",
    legend=False
)
```

The box plot helps identify:

* Median transaction values
* Interquartile ranges
* Distribution spread
* Potential high-value outliers

### Business Value

Outlier analysis can help identify unusual transactions that may require further investigation. These transactions could represent large orders, special purchases, unusual discounts, or other exceptional business cases.

---

## 8. Correlation Analysis

A correlation matrix is generated using the numerical columns:

```python
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True
)
```

The correlation matrix helps determine whether numerical metrics move together positively or negatively or operate relatively independently.

This provides a useful overview of relationships between variables such as:

* Quantity
* Unit price
* Discount
* GST
* Total amount
* Hour

---

# 📈 Key Findings

Based on the analysis performed in the notebook:

1. The dataset contains **50,000 pizza transaction records**.
2. The transaction-value distribution is **right-skewed**.
3. Most transaction amounts are concentrated in the lower-to-middle range.
4. High-value transactions increase the mean transaction amount.
5. The median is therefore a useful indicator of typical customer spending.
6. Average transaction values differ across pizza sizes.
7. Box plots reveal variation and potential outliers across pizza names.
8. Correlation analysis provides insight into relationships among numerical transaction variables.
9. The dataset provides useful information for understanding pizza sales and customer purchasing behavior.

---

# 📂 Project Structure

```text
Pizza-Sales-EDA/
│
├── Task2.ipynb
├── SQL.csv
└── README.md
```

> Keep `SQL.csv` in the same directory as `Task2.ipynb` because the notebook loads the dataset using `pd.read_csv('SQL.csv')`.

---

# ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Open the Project

Open the project folder in:

* Jupyter Notebook
* JupyterLab
* VS Code
* Google Colab

### Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 4: Place the Dataset

Make sure `SQL.csv` is available in the same directory as the notebook.

### Step 5: Run the Notebook

Open:

```text
Task2.ipynb
```

and execute the notebook cells sequentially.

---

# 💡 Business Applications

The analysis can support several business decisions, including:

* Understanding customer spending behavior
* Comparing performance by pizza size
* Identifying unusual or high-value transactions
* Understanding relationships between pricing, discounts, and revenue
* Supporting pricing and promotional decisions
* Identifying areas for deeper sales analysis

---

# 👨‍💻 Skills Demonstrated

* Python Programming
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Data Cleaning
* Data Inspection
* Exploratory Data Analysis
* Statistical Analysis
* Data Visualization
* Outlier Detection
* Correlation Analysis
* Business Insight Generation

---

## ⭐ Conclusion

This project demonstrates a complete introductory-to-intermediate **Exploratory Data Analysis workflow in Python**. It converts raw pizza transaction data into meaningful statistical observations and visual insights.

The project demonstrates how Python-based analytics can be used to understand transaction behavior, compare categories, identify unusual observations, and explore relationships between business metrics.
