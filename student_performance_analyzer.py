# -*- coding: utf-8 -*-
"""Student Performance Analyzer

Analyzes, calculates, and visualizes student academic performance
using Pandas, NumPy, Matplotlib, and Seaborn.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("       STUDENT PERFORMANCE ANALYZER")
print("=" * 50)

# Optional Google Colab upload handler
dataset_path = "students.csv"
if not os.path.exists(dataset_path):
    try:
        from google.colab import files
        print("Please upload students.csv:")
        uploaded = files.upload()
    except ImportError:
        pass

# Load Dataset
print("\n[+] Loading Dataset...")
data = pd.read_csv(dataset_path)

print("\n--- First 5 Rows ---")
print(data.head())

print(f"\nDataset Shape: {data.shape} (Rows: {data.shape[0]}, Columns: {data.shape[1]})")

print("\n--- Dataset Info ---")
data.info()

# Calculations
data["Total"] = data["Math"] + data["English"] + data["Science"] + data["Computer"]
data["Percentage"] = (data["Total"] / 400) * 100

print("\n--- Processed Data with Total & Percentage ---")
print(data)

# High & Low Achievers
highest_student = data.loc[data["Percentage"].idxmax()]
print("\n[+] Highest Performing Student:")
print(highest_student)

lowest_student = data.loc[data["Percentage"].idxmin()]
print("\n[-] Lowest Performing Student:")
print(lowest_student)

# Class Statistics
class_average = data["Percentage"].mean()
print(f"\nClass Average Percentage: {class_average:.2f}%")

above_80 = data[data["Percentage"] > 80]
print(f"\nStudents with Percentage > 80% ({len(above_80)} students):")
print(above_80[["Student", "Total", "Percentage"]])

# NumPy Statistical Analysis
percentages = np.array(data["Percentage"])
print("\n--- NumPy Percentage Summary ---")
print(f"Maximum Percentage: {np.max(percentages):.2f}%")
print(f"Minimum Percentage: {np.min(percentages):.2f}%")
print(f"Average Percentage: {np.mean(percentages):.2f}%")
print(f"Standard Deviation: {np.std(percentages):.2f}%")

# Subject Averages
subject_cols = ["Math", "English", "Science", "Computer"]
subject_average = data[subject_cols].mean()
print("\n--- Subject Averages ---")
print(subject_average)

# Ensure assets directory exists for saving plots
os.makedirs("assets", exist_ok=True)

# 1. Subject Average Marks Bar Plot
plt.figure(figsize=(8, 5))
sns.barplot(
    x=subject_average.index,
    y=subject_average.values,
    hue=subject_average.index,
    palette="crest",
    legend=False
)
plt.title("Average Marks by Subject", fontsize=14, fontweight="bold")
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Average Marks", fontsize=12)
plt.ylim(0, 100)
for i, v in enumerate(subject_average.values):
    plt.text(i, v + 1.5, f"{v:.1f}", ha="center", fontweight="bold")
plt.tight_layout()
plt.savefig("assets/average_marks_by_subject.png", dpi=300)
plt.close()

# 2. Correlation Heatmap
plt.figure(figsize=(8, 6))
correlation = data[subject_cols + ["Percentage"]].corr()
sns.heatmap(correlation, annot=True, cmap="Blues", fmt=".2f", linewidths=0.5)
plt.title("Subject & Percentage Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("assets/correlation_heatmap.png", dpi=300)
plt.close()

# 3. Student Scores Comparison (English vs Computer)
plt.figure(figsize=(10, 5))
plt.bar(data["English"], data["Computer"], color="#4A90E2", edgecolor="black", alpha=0.7)
plt.title("Student English vs Computer Marks Comparison", fontsize=14, fontweight="bold")
plt.xlabel("English Marks", fontsize=12)
plt.ylabel("Computer Marks", fontsize=12)
plt.tight_layout()
plt.savefig("assets/student_scores_bar.png", dpi=300)
plt.close()

# 4. Math vs Science Bar Plot
plt.figure(figsize=(10, 5))
sns.barplot(
    data=data,
    x="Math",
    y="Science",
    hue="Math",
    palette="viridis",
    legend=False
)
plt.title("Student Math vs Science Comparison", fontsize=14, fontweight="bold")
plt.xlabel("Math Marks", fontsize=12)
plt.ylabel("Science Marks", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("assets/math_vs_science.png", dpi=300)
plt.close()

print("\n[OK] Analysis and Visualizations completed successfully!")