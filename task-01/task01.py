import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("Titanic-Dataset.csv")

# ===============================
# BAR CHART – Gender Distribution
# ===============================
gender_counts = df['Sex'].value_counts()

plt.figure()
plt.bar(gender_counts.index, gender_counts.values)
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.title("Gender Distribution in Titanic Dataset")
plt.show()

# ===============================
# HISTOGRAM – Age Distribution
# ===============================
plt.figure()
plt.hist(df['Age'].dropna(), bins=8)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution in Titanic Dataset")
plt.show()
