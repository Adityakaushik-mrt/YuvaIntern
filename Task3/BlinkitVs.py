# ==============================================================================
# PROJECT: BLINKIT GROCERY SALES & OPERATIONAL ANALYTICS DASHBOARD
# OBJECTIVE: TASK 4 - DATA SCIENCE TOOL MASTERY PROJECT
# AUTHOR: DATA SCIENCE INTERN
# LIBRARIES USED: pandas, numpy, matplotlib, seaborn, plotly
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 1: IMPORT REQUIRED LIBRARIES & CONFIGURE STYLING
# ------------------------------------------------------------------------------
import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
warnings.filterwarnings('ignore')
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("=" * 80)
print("STEP 1: LIBRARIES IMPORTED SUCCESSFULLY")
print("=" * 80)

# ------------------------------------------------------------------------------
# STEP 2: DATA LOADING & INITIAL SHAPE AUDIT
# ------------------------------------------------------------------------------
file_path = 'BlinkIT Grocery Data.xlsx'
df = pd.read_excel(file_path)

rows, cols = df.shape
print(f"\n[INFO] Dataset Loaded Successfully!")
print(f"[INFO] Total Records (Rows): {rows:,}")
print(f"[INFO] Total Features (Columns): {cols}")
print("\n[PREVIEW] First 5 Rows of Dataset:")
print(df.head())
# ------------------------------------------------------------------------------
# STEP 3: DATA INTEGRITY & MISSING VALUE AUDIT
# ------------------------------------------------------------------------------
print("\n" + "=" * 80)
print("STEP 3: DATA EXPLORATION & AUDIT")
print("=" * 80)
missing_counts = df.isnull().sum()
print("\n[AUDIT] Missing Values Count Per Column:")
print(missing_counts[missing_counts > 0])

duplicate_rows = df.duplicated().sum()
print(f"\n[AUDIT] Duplicate Records: {duplicate_rows}")

print("\n[AUDIT] Inconsistent Categories in 'Item Fat Content':")
print(df['Item Fat Content'].value_counts())

# ------------------------------------------------------------------------------
# STEP 4: DATA PREPROCESSING & STANDARDIZATION
# ------------------------------------------------------------------------------
print("\n" + "=" * 80)
print("STEP 4: DATA CLEANING & STANDARDIZATION")
print("=" * 80)
df['Item Fat Content'] = df['Item Fat Content'].replace({
    'LF': 'Low Fat',
    'low fat': 'Low Fat',
    'reg': 'Regular'
})
print("[CLEAN] Standardized 'Item Fat Content' Categories:")
print(df['Item Fat Content'].value_counts())

df['Item Weight'] = df['Item Weight'].fillna(
    df.groupby('Item Type')['Item Weight'].transform('mean')
)
print(f"[CLEAN] Item Weight Missing Values Handled. Remaining Missing: {df['Item Weight'].isnull().sum()}")

CURRENT_YEAR = 2026
df['Outlet Age'] = CURRENT_YEAR - df['Outlet Establishment Year']
print(f"[CLEAN] Engineered Feature 'Outlet Age' (Range: {df['Outlet Age'].min()} - {df['Outlet Age'].max()} Years)")

# ------------------------------------------------------------------------------
# STEP 5: CALCULATE HIGH-LEVEL EXECUTIVE BUSINESS KPIS
# ------------------------------------------------------------------------------
print("\n" + "=" * 80)
print("STEP 5: EXECUTIVE KPI SUMMARY RESULTS")
print("=" * 80)

total_sales_revenue = df['Sales'].sum()
average_item_sales = df['Sales'].mean()
total_items_sold = len(df)
average_customer_rating = df['Rating'].mean()

print(f" • TOTAL REVENUE GENERATED    : ${total_sales_revenue:,.2f}")
print(f" • AVERAGE SALES PER ITEM     : ${average_item_sales:,.2f}")
print(f" • TOTAL PRODUCT ITEMS SOLD   : {total_items_sold:,}")
print(f" • AVERAGE CUSTOMER RATING    : {average_customer_rating:.2f} / 5.0")
print("=" * 80)

# ------------------------------------------------------------------------------
# STEP 6: DATA VISUALIZATIONS WITH BUSINESS INSIGHTS & OUTPUTS
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# VISUALIZATION 1: SALES BY ITEM FAT CONTENT (DONUT CHART)
# ------------------------------------------------------------------------------
print("\n[CHART 1] Calculating Sales by Fat Content...")
fat_sales = df.groupby('Item Fat Content')['Sales'].sum().reset_index()
for idx, row in fat_sales.iterrows():
    percentage = (row['Sales'] / total_sales_revenue) * 100
    print(f"   -> {row['Item Fat Content']}: ${row['Sales']:,.2f} ({percentage:.1f}%)")

fig1 = px.pie(
    fat_sales,
    values='Sales',
    names='Item Fat Content',
    hole=0.6,
    color='Item Fat Content',
    color_discrete_map={'Low Fat': '#2b6cb0', 'Regular': '#dd6b20'},
    title='<b>Sales Distribution by Item Fat Content (Blinkit)</b>'
)
fig1.update_layout(font=dict(weight="bold", size=13))
fig1.show()

# ------------------------------------------------------------------------------
# VISUALIZATION 2: TOP 10 ITEM CATEGORIES BY REVENUE (HORIZONTAL BAR CHART)
# ------------------------------------------------------------------------------
print("\n[CHART 2] Top 5 Category Revenue Leaders:")
top_items = df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()
for idx, row in top_items.head(5).iterrows():
    print(f"   -> {row['Item Type']}: ${row['Sales']:,.2f}")

fig2 = px.bar(
    top_items,
    x='Sales',
    y='Item Type',
    orientation='h',
    text_auto='$,.2s',
    color='Sales',
    color_continuous_scale='Blues',
    title='<b>Top 10 Item Categories by Revenue</b>'
)
fig2.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    xaxis_title='<b>Total Sales ($)</b>',
    yaxis_title='<b>Item Category</b>',
    font=dict(weight="bold")
)
fig2.show()

# ------------------------------------------------------------------------------
# VISUALIZATION 3: REVENUE BREAKDOWN BY OUTLET FORMAT (BAR CHART)
# ------------------------------------------------------------------------------
print("\n[CHART 3] Outlet Format Performance Summary:")
outlet_perf = df.groupby('Outlet Type').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Orders=('Sales', 'count'),
    Avg_Sales=('Sales', 'mean')
).reset_index()
for idx, row in outlet_perf.iterrows():
    share = (row['Total_Sales'] / total_sales_revenue) * 100
    print(f"   -> {row['Outlet Type']}: ${row['Total_Sales']:,.2f} ({share:.1f}% share, {row['Total_Orders']} items)")

fig3 = px.bar(
    outlet_perf,
    x='Outlet Type',
    y='Total_Sales',
    text_auto='$,.2s',
    color='Outlet Type',
    title='<b>Sales Revenue by Outlet Format</b>'
)
fig3.update_layout(
    xaxis_title='<b>Outlet Format</b>',
    yaxis_title='<b>Total Revenue ($)</b>',
    font=dict(weight="bold")
)
fig3.show()

# ------------------------------------------------------------------------------
# VISUALIZATION 4: HIERARCHICAL REVENUE BREAKDOWN (SUNBURST CHART)
# ------------------------------------------------------------------------------
print("\n[CHART 4] City Tier Revenue Contribution:")
tier_sales = df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
for idx, row in tier_sales.iterrows():
    share = (row['Sales'] / total_sales_revenue) * 100
    print(f"   -> {row['Outlet Location Type']}: ${row['Sales']:,.2f} ({share:.1f}%)")

fig4 = px.sunburst(
    df,
    path=['Outlet Location Type', 'Outlet Size', 'Outlet Type'],
    values='Sales',
    color='Outlet Location Type',
    title='<b>Sales Hierarchy: City Tier → Outlet Size → Outlet Type</b>'
)
fig4.update_layout(font=dict(weight="bold", size=13))
fig4.show()

# ------------------------------------------------------------------------------
# VISUALIZATION 5: CORRELATION MATRIX (SEABORN HEATMAP)
# ------------------------------------------------------------------------------
print("\n[CHART 5] Numerical Attribute Correlation Matrix:")
numerical_cols = ['Item Visibility', 'Item Weight', 'Sales', 'Rating', 'Outlet Age']
corr_matrix = df[numerical_cols].corr()
print(corr_matrix.round(3))

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='Blues', linewidths=0.8, linecolor='white')
plt.title('Correlation Matrix of Grocery Metrics', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.show()

print("\n" + "=" * 80)
print("ALL DASHBOARD VISUALIZATIONS GENERATED SUCCESSFULLY!")
print("=" * 80)