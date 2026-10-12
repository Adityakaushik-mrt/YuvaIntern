# 🛒 Blinkit Grocery Sales & Operational Analytics Dashboard

An end-to-end Data Science & Business Intelligence project analyzing 8,500+ grocery transaction records from Blinkit (formerly Grofers). Built using Python, Pandas, Seaborn, and Plotly Express to evaluate retail demand, inventory fat-content preferences, outlet-format productivity, and geographic market trends.

---

## 📌 Project Overview
* **Domain:** E-Commerce / Quick-Commerce (Q-Commerce) Retail Analytics
* **Dataset:** `BlinkIT Grocery Data.xlsx` (8,523 rows × 12 columns)
* **Internship Track:** Task 4 — Data Science Tool Mastery Project
* **Core Objectives:**
  * Clean, standardize, and impute missing data across grocery items.
  * Evaluate consumer preferences across dietary categories (Low Fat vs. Regular).
  * Determine category-wise top grossing items (Fruits/Vegetables, Snacks, Household).
  * Benchmark store formats (Supermarket Type 1/2/3 vs. Grocery Stores).
  * Map multi-tier geographic revenue drivers (Tier 1, Tier 2, Tier 3).

---

## 🛠️ Tools & Libraries Mastered
* **Language:** Python 3.10+
* **Data Processing & Feature Engineering:** `pandas`, `numpy`
* **Statistical Modeling & Heatmaps:** `seaborn`, `matplotlib`
* **Interactive Business Visualizations:** `plotly.express`, `plotly.graph_objects`

---

## 📈 Executive KPI Summary Results
* **Total Sales Revenue:** `$1,201,681.49` (~$1.20M)
* **Average Sales Per Item:** `$140.99`
* **Total Product Lines Sold:** `8,523`
* **Average Customer Rating:** `3.97 / 5.0`

---

## 🔍 Key Dashboard Insights & Recommendations

### 1. Item Fat Content (Low Fat vs. Regular)
* **Key Finding:** Low-fat grocery products generated **$776,319.69 (64.6%)**, compared to **$425,361.80 (35.4%)** for regular-fat products.
* **Recommendation:** Create a dedicated "Healthy & Clean Living" banner on the Blinkit app to cross-sell organic and health-oriented items.

### 2. Top Revenue Drivers by Category
* **Key Finding:** **Fruits and Vegetables** ($178.1K) and **Snack Foods** ($175.4K) are the largest revenue contributors, followed by **Household Items** ($136.0K) and **Frozen Foods** ($118.6K).
* **Recommendation:** Prioritize hyper-local cold-chain dark stores for perishable goods to maintain sub-15 minute delivery times and minimize spoilage.

### 3. Store Format Productivity
* **Key Finding:** **Supermarket Type 1** accounts for **$787,549.89 (65.5%)** of total revenue across 5,577 transaction items, whereas standalone **Grocery Stores** underperform at $151.9K.
* **Recommendation:** Convert small standalone grocery locations into micro-fulfillment dark stores optimized for fast-moving items.

### 4. Geographic Market Hierarchy
* **Key Finding:** **Tier 3 cities** generated the highest sales volume (**$472.1K / 39.3%**), outperforming **Tier 2** ($393.2K / 32.7%) and **Tier 1** ($336.4K / 28.0%). **Medium-sized stores** generated maximum profits across all city tiers.
* **Recommendation:** Expand dark-store density in emerging Tier 2 and Tier 3 cities where quick-commerce adoption is growing rapidly with lower operational costs.

### 5. Metric Correlation Analysis
* **Key Finding:** `Item Visibility` shows a near-zero/slightly negative correlation (-0.13) with sales, indicating that high product exposure alone does not drive purchases without price competitiveness and strong product ratings.

---

## 📂 Repository File Structure
```text
├── data/
│   └── BlinkIT Grocery Data.xlsx      # Raw Excel dataset
├── notebooks/
│   └── blinkit_eda_dashboard.ipynb     # Fully executed Jupyter Notebook
├── scripts/
│   └── blinkit_analysis.py            # Clean Python analytical script
├── requirements.txt                   # Environment dependencies
└── README.md                          # Comprehensive project documentation
---

### 👤 Author
- **Intern:** [Aditya Sharma]
- **Role:** Data Analytics Intern