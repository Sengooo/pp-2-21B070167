import psycopg2
import csv
import json

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="myuser",
    password="qwerty"
)

# Create a cursor
cur = conn.cursor()

# Create a table
cur.execute("""
    CREATE TABLE Doctor (
        Doctor_Id SERIAL PRIMARY KEY,
        Doctor_Name VARCHAR(255) NOT NULL,
        Hospital_Id SERIAL NOT NULL,
        Joining_Date DATE NOT NULL,
        Speciality VARCHAR(255) NOT NULL,
        Salary INTEGER NOT NULL,
        Experience SMALLINT
    )
""")

# Insert data into the table
cur.execute("""
    INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience)
    VALUES
        (101, 'David', 1, '2005-2-10', 'Pediatric', 40000, NULL),
        (102, 'Michael', 1, '2018-07-23', 'Oncologist', 20000, NULL),
        (103, 'Susan', 2, '2016-05-19', 'Garnacologist', 25000, NULL),
        (104, 'Robert', 2, '2017-12-28', 'Pediatric ', 28000, NULL),
        (105, 'Linda', 3, '2004-06-04', 'Garnacologist', 42000, NULL),
        (106, 'William', 3, '2012-09-11', 'Dermatologist', 30000, NULL),
        (107, 'Richard', 4, '2014-08-21', 'Garnacologist', 32000, NULL),
        (108, 'Karen', 4, '2011-10-17', 'Radiologist', 30000, NULL)
""")

# Commit the changes
conn.commit()

# Task 2 - Function 1: Return all doctor names with their respective salaries that are greater than average salary, sorted from lowest to highest
cur.execute("""
    SELECT Doctor_Name, Salary
    FROM Doctor
    WHERE Salary > (SELECT AVG(Salary) FROM Doctor)
    ORDER BY Salary ASC
""")
rows = cur.fetchall()
print("Task 2 - Function 1:")
for row in rows:
    print(row)

# Task 2 - Function 2: Return all information about doctors who have joined since the beginning of 2012, sorted from oldest employee to newest
cur.execute("""
    SELECT *
    FROM Doctor
    WHERE Joining_Date >= '2012-01-01'
    ORDER BY Joining_Date ASC
""")
rows = cur.fetchall()
print("Task 2 - Function 2:")
for row in rows:
    print(row)

# Task 2 - Function 3: Return how many doctors belong to specialties from a table
cur.execute("""
    SELECT Speciality, COUNT(*) AS Count
    FROM Doctor
    GROUP BY Speciality
""")
rows = cur.fetchall()
print("Task 2 - Function 3:")
for row in rows:
    print(row)

# Task 2 - Procedure 1: Update rows based on the doctor's name
def update_doctor(name, salary):
    cur.execute("""
        UPDATE Doctor
        SET Salary = %s
        WHERE Doctor_Name = %s
    """, (salary, name))
    conn.commit()

# Update the salary of doctor 'David'
