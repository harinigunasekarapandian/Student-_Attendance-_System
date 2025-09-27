from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('attendance.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home page: show form for marking attendance
@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM Students').fetchall()
    subjects = conn.execute('SELECT * FROM Subjects').fetchall()
    conn.close()
    return render_template('index.html', students=students, subjects=subjects)

# Form submit: mark attendance
@app.route('/mark', methods=['POST'])
def mark_attendance():
    try:
        # Get the data from the form
        student_id = request.form['student']
        subject_id = request.form['subject']
        status = request.form['status']
        today = date.today().isoformat()

        # Connect to the database and insert the attendance record
        conn = get_db_connection()
        conn.execute(''' 
            INSERT INTO Attendance (student_id, subject_id, date, status)
            VALUES (?, ?, ?, ?)
        ''', (student_id, subject_id, today, status))
        conn.commit()
        conn.close()

        # Redirect back to the home page after successfully marking attendance
        return redirect('/')

    except Exception as e:
        print(f"Error: {e}")
        return "There was an issue marking the attendance. Please try again."

# Delete attendance for a specific date
@app.route('/delete', methods=['POST'])
def delete_attendance():
    try:
        date_to_delete = request.form['date']  # Get the date from the form
        if not date_to_delete:
            return "Please select a date."

        # Connect to the database and delete attendance records for that date
        conn = get_db_connection()
        conn.execute('''
            DELETE FROM Attendance WHERE date = ?
        ''', (date_to_delete,))
        conn.commit()
        conn.close()

        # Redirect back to the report page or home page after deletion
        return redirect('/report')  # or redirect('/')

    except Exception as e:
        print(f"Error: {e}")
        return "There was an issue deleting the attendance. Please try again."

# Report page with attendance details and percentage
@app.route('/report')
def report():
    conn = get_db_connection()

    # Attendance report
    report_data = conn.execute('''
        SELECT s.name AS student, sub.subject_name, a.date, a.status
        FROM Attendance a
        JOIN Students s ON a.student_id = s.student_id
        JOIN Subjects sub ON a.subject_id = sub.subject_id
        ORDER BY a.date DESC
    ''').fetchall()

    # Attendance percentage per student
    percentages = conn.execute('''
        SELECT s.name AS student, sub.subject_name,
               COUNT(*) AS total_classes,
               SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) AS present_count,
               ROUND(100.0 * SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) / COUNT(*), 2) AS attendance_percent
        FROM Attendance a
        JOIN Students s ON a.student_id = s.student_id
        JOIN Subjects sub ON a.subject_id = sub.subject_id
        GROUP BY a.student_id, a.subject_id
    ''').fetchall()

    # Get distinct dates for the delete form
    dates = conn.execute('SELECT DISTINCT date FROM Attendance ORDER BY date DESC').fetchall()
    conn.close()

    return render_template('report.html', report=report_data, percentages=percentages, dates=dates)

if __name__ == '__main__':
    app.run(debug=True)
