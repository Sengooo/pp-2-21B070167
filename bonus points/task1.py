import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="Sengo",
    password="qwerty"
)

# Create a cursor
cur = conn.cursor()

# Create a table
cur.execute("""
    CREATE TABLE Hospital (
        Hospital_Id SERIAL PRIMARY KEY,
        Hospital_Name VARCHAR(255) NOT NULL,
        Bed_Count SERIAL
    )
""")

# Insert data into the table
cur.execute("""
    INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count)
    VALUES
        (1, 'Mayo Clinic', 200),
        (2, 'Cleveland Clinic', 400),
        (3, 'Johns Hopkins', 1000),
        (4, 'UCLA Medical Center', 1500)
""")

# Commit the changes
conn.commit()

# Query the table and print the results
cur.execute("""
    SELECT Hospital_Name, Bed_Count
    FROM Hospital
    WHERE Bed_Count > 600
    ORDER BY Bed_Count DESC
""")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
