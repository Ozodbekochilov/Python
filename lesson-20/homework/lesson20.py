import pandas as pd
import sqlite3

# Chinook.db ga ulanish
conn = sqlite3.connect("task\\chinook.db")

# =================== HOMEWORK 1 ===================

# --task-1
# Customer Purchases Analysis
print("--task-1: Total amount spent by each customer")

query = """
SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName,
       i.InvoiceId, i.Total
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
"""
df = pd.read_sql_query(query, conn)

# Har bir customer bo‘yicha total amount
customer_totals = df.groupby(["CustomerId", "CustomerName"])["Total"].sum().reset_index(name="TotalSpent")
print(customer_totals)

# --task-2
# Top 5 customers with highest purchase amounts
print("--task-2: Top 5 customers by purchase amount")
top5 = customer_totals.sort_values("TotalSpent", ascending=False).head(5)
print(top5)

# --task-3
# Album vs Individual Track Purchases
print("--task-3: Percentage of customers preferring tracks vs albums")

query2 = """
SELECT i.CustomerId, ii.InvoiceLineId, ii.TrackId, t.AlbumId
FROM Invoice i
JOIN InvoiceLine ii ON i.InvoiceId = ii.InvoiceId
JOIN Track t ON ii.TrackId = t.TrackId
"""
purchases = pd.read_sql_query(query2, conn)

# Har bir customer-album uchun sotib olingan tracklar soni
album_track_counts = purchases.groupby("AlbumId")["TrackId"].nunique().reset_index(name="TotalTracks")
cust_album = purchases.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index(name="TracksBought")

# Full album sotib olganini aniqlash
cust_album = cust_album.merge(album_track_counts, on="AlbumId", how="left")
cust_album["FullAlbum"] = cust_album["TracksBought"] == cust_album["TotalTracks"]

# Har bir customerning xarid odatini aniqlash
customer_pref = cust_album.groupby("CustomerId")["FullAlbum"].any().reset_index()
customer_pref["Preference"] = customer_pref["FullAlbum"].apply(lambda x: "Full Album" if x else "Individual Tracks")

# Foiz hisoblash
summary = customer_pref["Preference"].value_counts(normalize=True) * 100
print(summary)

conn.close()
