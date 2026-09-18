import sqlite3

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()


# ==========================================
# 1. Top 5 Students
# ==========================================
cursor.execute("""
    SELECT Name, Final_Mark
    FROM students
    ORDER BY Final_Mark DESC
    LIMIT 5
""")

results = cursor.fetchall()

print("===== TOP 5 STUDENTS =====")
for row in results:
    print("Name:", row[0], "| Final Mark:", row[1])


# ==========================================
# 2. Students with Final Mark 80+
# ==========================================
cursor.execute("""
    SELECT Name, Final_Mark
    FROM students
    WHERE Final_Mark >= 80
    ORDER BY Final_Mark DESC
""")

results = cursor.fetchall()

print("\n===== STUDENTS WITH FINAL MARK 80 OR ABOVE =====")
for row in results:
    print("Name:", row[0], "| Final Mark:", row[1])


# ==========================================
# 3. Average Subject Scores
# ==========================================
cursor.execute("""
    SELECT
        AVG(Python),
        AVG(SQL),
        AVG(ML),
        AVG(Final_Mark)
    FROM students
""")

result = cursor.fetchone()

print("\n===== AVERAGE SCORES =====")
print("Python:", round(result[0], 2))
print("SQL:", round(result[1], 2))
print("ML:", round(result[2], 2))
print("Final Mark:", round(result[3], 2))


# ==========================================
# 4. Average Attendance
# ==========================================
cursor.execute("""
    SELECT AVG(Attendance)
    FROM students
""")

result = cursor.fetchone()

print("\n===== AVERAGE ATTENDANCE =====")
print("Average Attendance:", round(result[0], 2), "%")


# ==========================================
# 5. Highest and Lowest Final Mark
# ==========================================
cursor.execute("""
    SELECT MAX(Final_Mark), MIN(Final_Mark)
    FROM students
""")

result = cursor.fetchone()

print("\n===== FINAL MARK RANGE =====")
print("Highest Final Mark:", result[0])
print("Lowest Final Mark:", result[1])


# ==========================================
# 6. Top 5 by Attendance
# ==========================================
cursor.execute("""
    SELECT Name, Attendance, Final_Mark
    FROM students
    ORDER BY Attendance DESC
    LIMIT 5
""")

results = cursor.fetchall()

print("\n===== TOP 5 BY ATTENDANCE =====")
for row in results:
    print(
        "Name:", row[0],
        "| Attendance:", row[1], "%",
        "| Final Mark:", row[2]
    )


# Close database connection
conn.close()