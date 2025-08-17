import pandas as pd
import numpy as np

# ---------------------------
# HOMEWORK 1
# ---------------------------

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Rename column names using function
df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)
print("Renamed Columns:\n", df)

# 2. Print the first 3 rows
print("\nFirst 3 rows:\n", df.head(3))

# 3. Find the mean age
print("\nMean Age:", df['age'].mean())

# 4. Select and print only the 'first_name' and 'city' columns
print("\nSelected columns:\n", df[['first_name', 'city']])

# 5. Add a new column 'Salary' with random salary values
df['salary'] = np.random.randint(4000, 8000, size=len(df))
print("\nDataFrame with Salary:\n", df)

# 6. Display summary statistics of the DataFrame
print("\nSummary Statistics:\n", df.describe(include='all'))


# ---------------------------
# HOMEWORK 2
# ---------------------------

sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# 1. Maximum sales and expenses
print("\nMaximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max())

# 2. Minimum sales and expenses
print("\nMinimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min())

# 3. Average sales and expenses
print("\nAverage Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())


# ---------------------------
# HOMEWORK 3
# ---------------------------

expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Set 'Category' as index
expenses.set_index('Category', inplace=True)

# 1. Maximum expense for each category
print("\nMaximum expense for each category:\n", expenses.max(axis=1))

# 2. Minimum expense for each category
print("\nMinimum expense for each category:\n", expenses.min(axis=1))

# 3. Average expense for each category
print("\nAverage expense for each category:\n", expenses.mean(axis=1))
