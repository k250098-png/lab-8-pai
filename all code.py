import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data.csv", keep_default_na=False)

#  Task 1
t1 = df[df["scenario"] == "01_StudyVsScore"].copy()
t1["study_hours"] = pd.to_numeric(t1["study_hours"])
t1["exam_score"] = pd.to_numeric(t1["exam_score"])

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=t1, x="study_hours", y="exam_score",
    hue="prep_course", style="prep_course", s=100
)
plt.title("Study Hours vs. Exam Score by Prep Course Status")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# Task 2
t2 = df[df["scenario"] == "02_MonthlySales"].copy()
t2["exam_score"] = pd.to_numeric(t2["exam_score"])

plt.figure(figsize=(8, 5))
for company, group in t2.groupby("school_type", sort=False):
    plt.plot(group["study_hours"], group["exam_score"], marker="o", linewidth=2, label=company)

plt.title("Monthly Revenue Trends (Jan - Jun 2023)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend(title="Company")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# Task 3
t3 = df[df["scenario"] == "03_SalaryDiff"].copy()
t3["exam_score"] = pd.to_numeric(t3["exam_score"])

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=t3, x="prep_course", y="exam_score",
    order=["Entry", "Mid", "Senior"], palette="Set2"
)
plt.title("Salary Spread Across Experience Levels")
plt.xlabel("Experience Level")
plt.ylabel("Salary ($)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

#  Task 4
t4 = df[df["scenario"] == "04_CustAgeDist"].copy()
t4["age"] = pd.to_numeric(t4["prep_course"])

plt.figure(figsize=(8, 5))
ax = sns.histplot(data=t4, x="age", hue="study_hours", bins=5, kde=True)
ax.legend_.set_title("Gender")
plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")
plt.tight_layout()
plt.show()

# Task 5
t5 = df[df["scenario"] == "05_AdVsRevenue"].copy()
t5["ad_spend"] = pd.to_numeric(t5["study_hours"])
t5["revenue"] = pd.to_numeric(t5["prep_course"])

plt.figure(figsize=(8, 5))
sns.regplot(data=t5, x="ad_spend", y="revenue", color="darkgreen", marker="+")
plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
