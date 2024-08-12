# -*- coding: utf-8 -*-
"""Sales Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oYXAA7HbUD4Qhx8wOPyAmTNiTz5BB0xJ
"""

import numpy as np
import pandas as pd

df = pd.read_excel('ECOMM DATA.xlsx')

df.head()

# Check for missing values
print(df.isnull().sum())

# Handle missing values if necessary (example: filling missing values with 0)
df.fillna(0, inplace=True)

# Convert date columns to datetime format if necessary
df['Order Date'] = pd.to_datetime(df['Order Date'])

"""#### **Total Sales**"""

total_sales = df['Sales'].sum()
print(f"Total Sales: ${total_sales}")

"""#### **Analyze Sales Trends Over Time**"""

# Group by date and sum the sales
sales_trends = df.groupby('Order Date')['Sales'].sum().reset_index()

# Plot sales trends
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(sales_trends['Order Date'], sales_trends['Sales'], marker='o')
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

"""#### **Determined best selling products**"""

# Assuming 'Product Name' is the column with product names
best_selling_products = df.groupby('Product Name')['Sales'].sum().reset_index()
best_selling_products = best_selling_products.sort_values(by='Sales', ascending=False).head(10)

# Display best-selling products
print("Best-Selling Products:")
print(best_selling_products)

"""#### **Visualizations**"""

# Total Sales Bar Chart
plt.figure(figsize=(12, 6))
plt.bar(best_selling_products['Product Name'], best_selling_products['Sales'])
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Sales')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.show()

"""Monthly Sales Trends"""

# Extract month and year from the 'Order Date' column
df['Month'] = df['Order Date'].dt.to_period('M')

# Group by 'Month' and sum the sales
monthly_sales_trends = df.groupby('Month')['Sales'].sum().reset_index()

# Plot monthly sales trends
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales_trends['Month'].astype(str), monthly_sales_trends['Sales'], marker='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

"""Sales by Category"""

# Assuming 'Category' is a column in your dataset
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()

# Plot sales by category
plt.figure(figsize=(10, 6))
plt.bar(sales_by_category['Category'], sales_by_category['Sales'], color='skyblue')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

"""Sales by Region"""

# Assuming 'Region' is a column in your dataset
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()

# Plot sales by region
plt.figure(figsize=(11, 5))
plt.bar(sales_by_region['Region'], sales_by_region['Sales'], color='lightgreen')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.xticks(rotation=40)
plt.grid(True)
plt.show()

"""Sales Distribution"""

# Plot sales distribution as a histogram
plt.figure(figsize=(8, 4))
plt.hist(df['Sales'], bins=50, color='purple')
plt.title('Sales Distribution')
plt.xlabel('Sales')

plt.ylabel('Frequency')
plt.grid(True)
plt.show()

"""Pie Chart of Sales by Category"""

# Pie chart of sales by category
plt.figure(figsize=(4, 4))
plt.pie(sales_by_category['Sales'], labels=sales_by_category['Category'], autopct='%1.1f%%', startangle=140)
plt.title('Sales by Category')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()