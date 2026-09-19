import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("data/students.csv")


# ==========================================
# 2. Dataset Overview
# ==========================================

print("===== DATASET OVERVIEW =====")

print("\nFirst 5 Students:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


# ==========================================
# 3. Check Missing Values
# ==========================================

print("\n===== MISSING VALUES =====")

print(df.isnull().sum())


# ==========================================
# 4. Average Scores
# ==========================================

print("\n===== AVERAGE SCORES =====")

averages = df[["Python", "SQL", "ML", "Final_Mark"]].mean()

print(averages.round(2))


# ==========================================
# 5. Highest and Lowest Performers
# ==========================================

highest = df.loc[df["Final_Mark"].idxmax()]
lowest = df.loc[df["Final_Mark"].idxmin()]

print("\n===== PERFORMANCE ANALYSIS =====")

print("\nHighest Performer:")
print("Name:", highest["Name"])
print("Final Mark:", highest["Final_Mark"])

print("\nLowest Performer:")
print("Name:", lowest["Name"])
print("Final Mark:", lowest["Final_Mark"])


# ==========================================
# 6. Attendance Analysis
# ==========================================

average_attendance = df["Attendance"].mean()

print("\n===== ATTENDANCE ANALYSIS =====")

print("Average Attendance:", round(average_attendance, 2), "%")


# ==========================================
# 7. Attendance vs Final Mark Correlation
# ==========================================

correlation = df["Attendance"].corr(df["Final_Mark"])

print("\nAttendance vs Final Mark Correlation:")
print(round(correlation, 2))


# ==========================================
# 8. Subject Performance Ranking
# ==========================================

subject_averages = df[["Python", "SQL", "ML"]].mean()
subject_averages = subject_averages.sort_values(ascending=False)

print("\n===== SUBJECT PERFORMANCE =====")

print(subject_averages.round(2))


# ==========================================
# 9. Bar Chart - Average Subject Scores
# ==========================================

plt.figure(figsize=(7, 5))

plt.bar(
    subject_averages.index,
    subject_averages.values
)

plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")

plt.tight_layout()
plt.show()


# ==========================================
# 10. Scatter Plot - Attendance vs Final Mark
# ==========================================

plt.figure(figsize=(7, 5))

plt.scatter(
    df["Attendance"],
    df["Final_Mark"]
)

plt.title("Attendance vs Final Mark")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Mark")

plt.tight_layout()
plt.show()

print("\n===== ANALYSIS COMPLETED =====")
print("Student academic and attendance analysis completed successfully.")