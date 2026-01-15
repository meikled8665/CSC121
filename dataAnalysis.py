import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("best_selling_albums.csv")

print(df.head())

year = df["Year"]
sales = df["Sales_Millions"]

oldest = df[df["Year"] == year.min()]
newest = df[df["Year"] == year.max()]["Album"]
highest_sales = df[df["Sales_Millions"] == sales.max()]
lowest_sales = df[df["Sales_Millions"] == sales.min()]

print("\n")
print(oldest)
print(newest)
print(lowest_sales)
print(highest_sales)