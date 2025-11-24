import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned sales data
file = './cleanSales.csv'
df = pd.read_csv(file)

print("Sales Information")
df.info()

print("\nSales Numerical Summary")
print(df.describe())

print("\nFirst 5 rows")
print(df.head())

print("\nSales Data shape")
print(df.shape)

print("\nCheck if missing values")
print(df.isnull().sum())

print("\nDrop any missing values")
df_cleaned = df.dropna().copy()

print("\nCheck again")
print(df_cleaned.isnull().sum())

print("\nCheck duplicates")
print(df_cleaned.duplicated().sum())

print("\nStandardizing categories")
print(df_cleaned['Region'].unique())
print(df_cleaned['Category'].value_counts())
print(df_cleaned['Country'].unique())

# Apply safe standardization
df_cleaned.loc[:, 'Region'] = df_cleaned['Region'].str.lower().str.strip()

# Convert dates safely (fixed)
df_cleaned.loc[:, 'Order Date'] = pd.to_datetime(df_cleaned['Order Date'])
df_cleaned.loc[:, 'Ship Date'] = pd.to_datetime(df_cleaned['Ship Date'])

print("\nAfter Cleaning:")
df_cleaned.info()

# Save cleaned dataset
df_cleaned.to_csv('cleanSales_final.csv', index=False)
print("\nCleaned data saved successfully as cleanSales_final.csv")

# --- Optional: Top 10 Products by Sales ---
top_products = (
    df_cleaned.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(14, 7))
sns.set_style("whitegrid")

sns.barplot(
    x=top_products.values,
    y=top_products.index,
    palette="viridis"    # better colors
)

plt.title("Top 10 Products by Total Sales", fontsize=18, weight='bold')
plt.xlabel("Total Sales", fontsize=14)
plt.ylabel("Product Name", fontsize=14)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()
