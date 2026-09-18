import pandas as pd
import sqlite3

# Load the CSV dataset
df = pd.read_csv("data/students.csv")

# Create/connect to SQLite database
conn = sqlite3.connect("students.db")

# Store the dataset as a SQL table
df.to_sql("students", conn, if_exists="replace", index=False)

print("Database created successfully.")

# Check the first 5 records
print("\nFirst 5 records from database:")
result = pd.read_sql_query("SELECT * FROM students LIMIT 5", conn)
print(result)

# Close database connection
conn.close()