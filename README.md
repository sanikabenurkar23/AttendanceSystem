# Student Attendance Management System

A console-based Student Attendance Management System developed using **Python** and **SQLite**. This application helps manage student records, track daily attendance, calculate attendance percentages, and generate attendance reports.

## Features
- Add Student
- View Students
- Search Student
- Update Student Details
- Delete Student
- Mark Attendance
- View Attendance Records
- Calculate Attendance Percentage
- Dashboard Summary
- Export Attendance Report to CSV

## Technologies Used
- Python 3
- SQLite
- CSV Module
- Datetime Module

## Project Structure

```
AttendanceSystem/
│── attendance.py
│── attendance.db
│── attendance_report.csv
│── README.md
```

## Database
The project uses SQLite with two tables:

### Students Table
- Roll Number
- Student Name

### Attendance Table
- Attendance ID
- Roll Number
- Date
- Attendance Status (Present/Absent)

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
python attendance.py
```

## Sample Menu
===== STUDENT ATTENDANCE MANAGEMENT SYSTEM =====

1. Add Student
2. Mark Attendance
3. View Attendance
4. View Students
5. Search Student
6. Update Student Name
7. Delete Student
8. Attendance Percentage
9. Dashboard Summary
10. Export Attendance to CSV
11. Exit
```

## Output

- Stores student information in SQLite database.
- Maintains attendance records.
- Calculates attendance percentage.
- Generates attendance reports.
- Exports attendance data to a CSV file.

## Future Enhancements

- Graphical User Interface (Tkinter)
- Login Authentication
- Attendance Reports by Date
- Student-wise Attendance History
- Monthly Attendance Reports
- Email Notifications
