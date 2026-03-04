import csv

with open("sales.csv", "r", newline = "") as file:
    reader = csv.reader(file)