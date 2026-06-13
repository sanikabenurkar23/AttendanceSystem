import sqlite3
from datetime import date

# ==========================
# DATABASE SETUP
# ==========================
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_no INTEGER,
    date TEXT,
    status TEXT,
    FOREIGN KEY (roll_no) REFERENCES students(roll_no)
)
''')

conn.commit()
conn.close()


# ==========================
# ADD STUDENT
# ==========================
def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students (roll_no, name) VALUES (?, ?)",
            (roll, name)
        )

        conn.commit()
        conn.close()

        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("Roll Number already exists!")

    except ValueError:
        print("Please enter a valid roll number.")


# ==========================
# MARK ATTENDANCE
# ==========================
def mark_attendance():
    try:
        roll = int(input("Enter Roll Number: "))

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll,)
        )

        student = cursor.fetchone()

        if student is None:
            print("Student not found!")
            conn.close()
            return

        status = input("Enter Attendance (Present/Absent): ").capitalize()

        if status not in ["Present", "Absent"]:
            print("Please enter Present or Absent.")
            conn.close()
            return

        today = str(date.today())

        cursor.execute(
            "INSERT INTO attendance (roll_no, date, status) VALUES (?, ?, ?)",
            (roll, today, status)
        )

        conn.commit()
        conn.close()

        print("Attendance marked successfully!")

    except ValueError:
        print("Please enter a valid roll number.")


# ==========================
# VIEW ATTENDANCE
# ==========================
def view_attendance():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT students.roll_no,
               students.name,
               attendance.date,
               attendance.status
        FROM students
        JOIN attendance
        ON students.roll_no = attendance.roll_no
        ORDER BY attendance.date
    ''')

    records = cursor.fetchall()

    if len(records) == 0:
        print("No attendance records found.")
    else:
        print("\nAttendance Records")
        print("-" * 60)
        print("{:<10} {:<20} {:<15} {:<10}".format(
            "Roll No", "Name", "Date", "Status"
        ))
        print("-" * 60)

        for record in records:
            print("{:<10} {:<20} {:<15} {:<10}".format(
                record[0],
                record[1],
                record[2],
                record[3]
            ))

    conn.close()


# ==========================
# VIEW STUDENTS
# ==========================
def view_students():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found.")
    else:
        print("\nStudent List")
        print("-" * 35)
        print("{:<10} {:<20}".format("Roll No", "Name"))
        print("-" * 35)

        for student in students:
            print("{:<10} {:<20}".format(
                student[0],
                student[1]
            ))

    conn.close()


# ==========================
# SEARCH STUDENT
# ==========================
def search_student():
    try:
        roll = int(input("Enter Roll Number to Search: "))

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll,)
        )

        student = cursor.fetchone()

        if student:
            print("\nStudent Found")
            print(f"Roll No: {student[0]}")
            print(f"Name: {student[1]}")
        else:
            print("Student not found!")

        conn.close()

    except ValueError:
        print("Please enter a valid roll number.")


# ==========================
# UPDATE STUDENT NAME
# ==========================
def update_student():
    try:
        roll = int(input("Enter Roll Number: "))
        new_name = input("Enter New Name: ")

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE students SET name = ? WHERE roll_no = ?",
            (new_name, roll)
        )

        if cursor.rowcount == 0:
            print("Student not found!")
        else:
            conn.commit()
            print("Student updated successfully!")

        conn.close()

    except ValueError:
        print("Please enter a valid roll number.")


# ==========================
# DELETE STUDENT
# ==========================
def delete_student():
    try:
        roll = int(input("Enter Roll Number to Delete: "))

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM attendance WHERE roll_no = ?",
            (roll,)
        )

        cursor.execute(
            "DELETE FROM students WHERE roll_no = ?",
            (roll,)
        )

        if cursor.rowcount == 0:
            print("Student not found!")
        else:
            conn.commit()
            print("Student deleted successfully!")

        conn.close()

    except ValueError:
        print("Please enter a valid roll number.")


# ==========================
# ATTENDANCE PERCENTAGE
# ==========================
def attendance_percentage():
    try:
        roll = int(input("Enter Roll Number: "))

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM attendance WHERE roll_no = ?",
            (roll,)
        )
        total = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(*) FROM attendance
            WHERE roll_no = ? AND status = 'Present'
            """,
            (roll,)
        )
        present = cursor.fetchone()[0]

        if total == 0:
            print("No attendance records found!")
        else:
            percentage = (present / total) * 100
            print(f"Attendance Percentage: {percentage:.2f}%")

        conn.close()

    except ValueError:
        print("Please enter a valid roll number.")


# ==========================
# MAIN MENU
# ==========================
while True:
    print("\n===== STUDENT ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. View Students")
    print("5. Search Student")
    print("6. Update Student Name")
    print("7. Delete Student")
    print("8. Attendance Percentage")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        mark_attendance()

    elif choice == '3':
        view_attendance()

    elif choice == '4':
        view_students()

    elif choice == '5':
        search_student()

    elif choice == '6':
        update_student()

    elif choice == '7':
        delete_student()

    elif choice == '8':
        attendance_percentage()

    elif choice == '9':
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")