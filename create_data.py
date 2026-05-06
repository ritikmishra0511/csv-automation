import csv

data = [
    ["Name", "Sales", "Region", "Month"],
    ["Alice", "1500", "North", "January"],
    ["Bob", "", "South", "January"],
    ["Charlie", "2300", "North", "February"],
    ["", "1800", "East", "February"],
    ["Diana", "abc", "West", "March"],
    ["Eve", "3200", "South", "March"],
    ["Frank", "1100", "North", ""],
    ["Grace", "2750", "East", "January"],
    ["Henry", "", "", "February"],
]

with open("sales_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Created sales_data.csv")