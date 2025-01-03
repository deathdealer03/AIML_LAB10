import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Load sample dataset
tips = sns.load_dataset("tips")

# Convert non-numeric columns to numeric
tips['sex_numeric'] = tips['sex'].map({'Female': 0, 'Male': 1})
tips['smoker_numeric'] = tips['smoker'].map({'No': 0, 'Yes': 1})

# Line plot
plt.figure(figsize=(8, 6))
sns.lineplot(x="total_bill", y="tip", data=tips)
plt.title("Line Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.savefig("line_plot.png")
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Scatter Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.savefig("scatter_plot.png")
plt.show()

# Bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Bar Plot: Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.savefig("bar_plot.png")
plt.show()

# Histogram
plt.figure(figsize=(8, 6))
sns.histplot(tips["total_bill"], bins=20)
plt.title("Histogram: Total Bill Distribution")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# Heatmap
plt.figure(figsize=(8, 6))
corr = tips[['total_bill', 'tip', 'sex_numeric', 'smoker_numeric']].corr()
sns.heatmap(corr, annot=True, cmap="YlOrRd")
plt.title("Heatmap: Correlation Matrix")
plt.savefig("heatmap.png")
plt.show()
