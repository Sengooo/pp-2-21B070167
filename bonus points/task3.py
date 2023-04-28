import psycopg2
import csv
import json

# Connect to the database
conn = psycopg2.connect(database="hospital", user="postgres", password="password", host="localhost", port="5432")
cur = conn.cursor()

# Define the function to join the Hospital and Doctor tables
def join_tables():
    cur.execute("""SELECT d.Doctor_Name, h.Hospital_Name, d.Joining_Date, d.Salary
                   FROM Doctor d
                   JOIN Hospital h
                   ON d.Hospital_Id = h.Hospital_Id
                   WHERE h.Bed_Count > 800 AND d.Salary >= 32000
                   ORDER BY h.Hospital_Name ASC""")
    rows = cur.fetchall()
    return rows

# Define the function to delete a hospital and its related doctors
def delete_hospital(hospital_name):
    cur.execute("""DELETE FROM Doctor WHERE Hospital_Id IN (SELECT Hospital_Id FROM Hospital WHERE Hospital_Name = %s)""", (hospital_name,))
    cur.execute("""DELETE FROM Hospital WHERE Hospital_Name = %s""", (hospital_name,))
    conn.commit()

# Define the procedure to export joined data to a csv or json file
def export_to_file(file_type):
    if file_type == "csv":
        with open('joined_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Doctor_Name', 'Hospital_Name', 'Joining_Date', 'Speciality', 'Salary', 'Experience'])
            cur.execute("""SELECT d.Doctor_Name, h.Hospital_Name, d.Joining_Date, d.Speciality, d.Salary, d.Experience
                           FROM Doctor d
                           JOIN Hospital h
                           ON d.Hospital_Id = h.Hospital_Id""")
            rows = cur.fetchall()
            for row in rows:
                writer.writerow(row)
    elif file_type == "json":
        data = {}
        data['joined_data'] = []
        cur.execute("""SELECT d.Doctor_Name, h.Hospital_Name, d.Joining_Date, d.Speciality, d.Salary, d.Experience
                       FROM Doctor d
                       JOIN Hospital h
                       ON d.Hospital_Id = h.Hospital_Id""")
        rows = cur.fetchall()
        for row in rows:
            data['joined_data'].append({
                'Doctor_Name': row[0],
                'Hospital_Name': row[1],
                'Joining_Date': row[2].strftime('%Y-%m-%d'),
                'Speciality': row[3],
                'Salary': row[4],
                'Experience': row[5]
            })
        with open('joined_data.json', 'w') as file:
            json.dump(data, file)

# Close the database connection
cur.close()
conn.close()
