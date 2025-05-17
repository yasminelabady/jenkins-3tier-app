import pandas as pd
import mysql.connector
from mysql.connector import Error, IntegrityError
import time

# Retry until MySQL is ready
while True:
    try:
        conn = mysql.connector.connect(
            host="mysql-db",
            user="root",
            password="root",
            database="myapp"
        )
        if conn.is_connected():
            print("Connected to MySQL")
            break
    except Error:
        print("Waiting for MySQL to be ready...")
        time.sleep(5)

cursor = conn.cursor()

# Read the CSV file
df = pd.read_csv("data.csv")

# Insert data while ignoring duplicates
for index, row in df.iterrows():
    try:
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (row['name'], row['age']))
    except IntegrityError:
        print(f"Duplicate entry skipped: {row['name']}")

# Finalize
conn.commit()
cursor.close()
conn.close()
print("Done inserting data.")

