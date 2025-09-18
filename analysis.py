import pandas as pd

# Load the dataset
# Make sure 'Stores.csv' is in the same folder as this script
try:
    df = pd.read_csv('Stores.csv')
    print("File 'Stores.csv' successfully loaded.")

    print("\nFirst 5 rows of the data:")
    print(df.head())

    print("\nBasic information about the dataset:")
    df.info()

except FileNotFoundError:
    print("Error: 'Stores.csv' not found. Please make sure the file is in the correct directory.")
    # --- Start of New Code ---

# Step 2: Add Financial Metrics

# Clean up column names (remove spaces)
df.columns = df.columns.str.replace(' ', '_')

# Assume a 15% profit margin
PROFIT_MARGIN = 0.15
df['Profit'] = df['Store_Sales'] * PROFIT_MARGIN

# Calculate Sales per Customer
# Avoid division by zero if a store had 0 customers
df['Sales_per_Customer'] = df.apply(
    lambda row: row['Store_Sales'] / row['Daily_Customer_Count'] if row['Daily_Customer_Count'] > 0 else 0,
    axis=1
)


print("\nData with New Financial Columns:")
# Display the first 5 rows with the new columns, rounded to 2 decimal places
print(df.head().round(2))

# --- End of New Code ---
# --- Start of New Code ---

import matplotlib.pyplot as plt
import seaborn as sns

print("\nStep 3: Creating Visualizations...")

# Clean up column names better (remove trailing underscore)
df.rename(columns={'Store_ID_': 'Store_ID'}, inplace=True)


# 1. Visualization: Top 10 Most Profitable Stores
plt.figure(figsize=(12, 6))
top_10_profit = df.sort_values(by='Profit', ascending=False).head(10)
sns.barplot(x='Store_ID', y='Profit', data=top_10_profit, order=top_10_profit['Store_ID'])
plt.title('Top 10 Most Profitable Stores')
plt.xlabel('Store ID')
plt.ylabel('Estimated Profit')
plt.savefig('top_10_profitable_stores.png') # Saves the chart as an image
print("Chart 1: 'top_10_profitable_stores.png' saved.")


# 2. Visualization: Store Area vs. Sales
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Store_Area', y='Store_Sales', data=df)
plt.title('Store Area vs. Store Sales')
plt.xlabel('Store Area (in sq. ft)')
plt.ylabel('Store Sales')
plt.savefig('area_vs_sales.png')
print("Chart 2: 'area_vs_sales.png' saved.")


# 3. Visualization: Items Available vs. Sales
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Items_Available', y='Store_Sales', data=df)
plt.title('Items Available vs. Store Sales')
plt.xlabel('Number of Items Available')
plt.ylabel('Store Sales')
plt.savefig('items_vs_sales.png')
print("Chart 3: 'items_vs_sales.png' saved.")

# --- End of New Code ---