import sqlite3

# Create the SQLite database and tables
conn = sqlite3.connect('attendance.db')
c = conn.cursor()

# Create Students table
c.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Create Subjects table
c.execute('''
    CREATE TABLE IF NOT EXISTS Subjects (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL
    )
''')

# Create Attendance table
c.execute('''
    CREATE TABLE IF NOT EXISTS Attendance (
        attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        date TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERENCES Students(student_id),
        FOREIGN KEY(subject_id) REFERENCES Subjects(subject_id)
    )
''')

# Insert 10 students
students = [
    ('Harini',), ('Jeya',), ('Jeno',), ('Kishori',),
    ('Janani',), ('Jeyavarshini',), ('Kala',), ('Mala',),
    ('Raja',), ('Karthi',)
]
c.executemany('INSERT INTO Students (name) VALUES (?)', students)

# Insert 5 subjects
subjects = [
    ('DBMS',), ('DAA',), ('TOC',), ('OS',), ('App Development',)
]
c.executemany('INSERT INTO Subjects (subject_name) VALUES (?)', subjects)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database setup complete with students and subjects.")
