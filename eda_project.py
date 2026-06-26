import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Display first few rows
print("=== Student Dataset ===")
print(df)

# Dataset information
print("\n=== Dataset Info ===")
print(df.info())

# Summary statistics
print("\n=== Summary Statistics ===")
print(df.describe())

# Check for missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Highest and lowest scorer
top_student = df.loc[df["Marks"].idxmax()]
low_student = df.loc[df["Marks"].idxmin()]

print("\nTop Scorer:")
print(top_student)

print("\nLowest Scorer:")
print(low_student)

print("\nAverage Marks:", df["Marks"].mean())

# --------- Bar Chart ---------
plt.figure(figsize=(6, 4))
plt.bar(df["Name"], df["Marks"])
plt.title("Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()

# --------- Pie Chart ---------
plt.figure(figsize=(6, 6))
plt.pie(df["Marks"], labels=df["Name"], autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()

# --------- Line Chart ---------
plt.figure(figsize=(6, 4))
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student Marks Trend")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()