import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Exercise 1: Importance of Data Visualization
"""
Data visualization is crucial in data analysis because it helps in identifying trends, patterns, and outliers in datasets.
It simplifies complex data and enhances understanding by presenting information in a graphical format.

A line graph is used to visualize trends over time. It is particularly useful for displaying continuous data and identifying changes or fluctuations over a period.
"""

# Exercise 2: Line Plot for Temperature Variation
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [72, 74, 76, 80, 82, 78, 75]

plt.figure(figsize=(8,5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b')
plt.xlabel("Day")
plt.ylabel("Temperature (°F)")
plt.title("Temperature Variation Over a Week")
plt.grid()
plt.show()

# Exercise 3: Bar Chart for Monthly Sales
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [5000, 5500, 6200, 7000, 7500]

plt.figure(figsize=(8,5))
plt.bar(months, sales, color='green')
plt.xlabel("Month")
plt.ylabel("Sales Amount ($)")
plt.title("Monthly Sales Data")
plt.show()

# Exercise 4: Histogram of CGPA
# cgpa_data = [2.5, 3.0, 3.2, 3.5, 3.8, 3.9, 2.8, 3.4, 3.1, 3.6, 3.7, 3.0, 3.3, 3.9, 2.9]
# df = pd.DataFrame({"CGPA": cgpa_data})

data = {'CGPA': [3.5, 3.7, 3.8, 3.9, 4.0, 3.6, 3.4, 3.8, 3.5, 3.9]}
df = pd.DataFrame(data)

plt.figure(figsize=(8,5))
# sns.histplot(df["CGPA"], bins=5, color='purple', kde=True)
sns.distplot(df["CGPA"], bins=5, color='purple', kde=True)
plt.title("Distribution of CGPA")
plt.xlabel("CGPA")
plt.ylabel("Frequency")
plt.show()

# Exercise 5: Comparing Anxiety Levels Across Genders
data = {"Choose your gender": ["Male", "Female", "Non-binary", "Male", "Female"],
        "Do you have Anxiety?": ["Yes", "No", "Yes", "Yes", "No"]}
df = pd.DataFrame(data)

plt.figure(figsize=(8,5))
sns.countplot(x="Choose your gender", hue="Do you have Anxiety?", data=df, palette="coolwarm")
plt.title("Anxiety Levels Across Genders")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Exercise 6: Scatter Plot for Age vs Panic Attacks
data = {"Age": [18, 19, 20, 21, 22, 23, 24, 25],
        "Do you have Panic Attacks?": ["Yes", "No", "Yes", "Yes", "No", "Yes", "No", "No"]}
df = pd.DataFrame(data)
df["Panic_Attack"] = df["Do you have Panic Attacks?"].map({"Yes": 1, "No": 0})

plt.figure(figsize=(8,5))
sns.scatterplot(x=df["Age"], y=df["Panic_Attack"], color='red', alpha=0.7)
plt.xlabel("Age")
plt.ylabel("Panic Attack (1=Yes, 0=No)")
plt.title("Relationship Between Age and Panic Attacks")
plt.show()