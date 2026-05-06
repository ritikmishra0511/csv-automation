import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Before cleaning:")
print(df)
print("\nShape:", df.shape)

# Remove rows where Name is missing
df = df.dropna(subset=["Name"])

# Remove rows where Sales is missing
df = df.dropna(subset=["Sales"])

# Remove rows where Sales is not a number
df = df[pd.to_numeric(df["Sales"], errors="coerce").notna()]

# Convert Sales to number
df["Sales"] = pd.to_numeric(df["Sales"])

# Remove rows where Month is missing
df = df.dropna(subset=["Month"])

print("\nAfter cleaning:")
print(df)
print("\nShape:", df.shape)

# Generate summary
print("\n--- SALES SUMMARY REPORT ---")
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Highest Sale:", df["Sales"].max())
print("Lowest Sale:", df["Sales"].min())
print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())
print("\nSales by Month:")
print(df.groupby("Month")["Sales"].sum())

# Save cleaned data to new CSV
df.to_csv("cleaned_sales.csv", index=False)
print("\nSaved cleaned data to cleaned_sales.csv")