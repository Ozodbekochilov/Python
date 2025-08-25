import pandas as pd
import sqlite3

# =================== HOMEWORK ASSIGNMENT 1: SALES DATA ===================

# CSV faylni o'qish
sales_df = pd.read_csv("task\\sales_data.csv")

# --task-1
# Group the data by Category: Total quantity, Avg price, Max quantity
print("--Assignment1-Task1")
agg_stats = sales_df.groupby("Category").agg(
    Total_Quantity=("Quantity", "sum"),
    Avg_Price=("Price", "mean"),
    Max_Quantity=("Quantity", "max")
).reset_index()
print(agg_stats)

# --task-2
# Identify the top-selling product in each category
print("--Assignment1-Task2")
top_products = sales_df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_products = top_products.sort_values(["Category", "Quantity"], ascending=[True, False])
print(top_products.groupby("Category").head(1))

# --task-3
# Find the date with highest total sales
print("--Assignment1-Task3")
sales_df["Total_Sales"] = sales_df["Quantity"] * sales_df["Price"]
date_sales = sales_df.groupby("Date")["Total_Sales"].sum().reset_index()
print(date_sales.loc[date_sales["Total_Sales"].idxmax()])


# =================== HOMEWORK ASSIGNMENT 2: CUSTOMER ORDERS ===================

orders_df = pd.read_csv("task\\customer_orders.csv")

# --task-4
# Group by CustomerID and filter out customers with less than 20 orders
print("--Assignment2-Task1")
customer_order_counts = orders_df.groupby("CustomerID")["OrderID"].count().reset_index(name="OrderCount")
print(customer_order_counts[customer_order_counts["OrderCount"] >= 20])

# --task-5
# Identify customers who ordered products with avg price > $120
print("--Assignment2-Task2")
customer_avg_price = orders_df.groupby("CustomerID")["Price"].mean().reset_index(name="AvgPrice")
print(customer_avg_price[customer_avg_price["AvgPrice"] > 120])

# --task-6
# Find total quantity and total price for each product, filter total qty < 5
print("--Assignment2-Task3")
product_totals = orders_df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Price=("Price", "sum")
).reset_index()
print(product_totals[product_totals["Total_Quantity"] >= 5])


# =================== HOMEWORK ASSIGNMENT 3: POPULATION SALARY ANALYSIS ===================

# SQLite DB dan o'qish
conn = sqlite3.connect("task\\population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# Salary bandsni Excel fayldan o‘qish
salary_bands = pd.read_excel("task\\population salary analysis.xlsx")

# Salary categoryga qo‘shish uchun bandlardan foydalanamiz
def categorize_salary(salary):
    for _, row in salary_bands.iterrows():
        if row["Min"] <= salary <= row["Max"]:
            return row["Band"]
    return "Other"

population_df["Salary_Band"] = population_df["Salary"].apply(categorize_salary)

# --task-7
# Measures by salary category
print("--Assignment3-Task1")
band_stats = population_df.groupby("Salary_Band").agg(
    Population_Count=("Salary", "count"),
    Avg_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median")
).reset_index()
band_stats["Percentage"] = (band_stats["Population_Count"] / len(population_df)) * 100
print(band_stats)

# --task-8
# Measures by salary category within each State
print("--Assignment3-Task2")
state_band_stats = population_df.groupby(["State", "Salary_Band"]).agg(
    Population_Count=("Salary", "count"),
    Avg_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median")
).reset_index()
state_band_stats["Percentage"] = state_band_stats.groupby("State")["Population_Count"].apply(lambda x: (x / x.sum()) * 100)
print(state_band_stats)
