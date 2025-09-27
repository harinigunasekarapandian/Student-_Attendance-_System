# Student-_Attendance-_System
Flask + SQLite based Student Attendance Manager. Easily record daily attendance, manage subjects and students, and generate detailed reports with percentages.
# 🎓 Student Attendance Management System (Flask + SQLite)

A simple **Student Attendance System** built using **Flask (Python Web Framework)**, **SQLite database**, and **HTML/CSS frontend**.  
It allows teachers/admins to mark attendance, view detailed attendance reports, calculate attendance percentages, and manage records.

---

## 🚀 Features
- ✅ Mark student attendance (Present/Absent) for each subject  
- ✅ Auto-stores records with current date  
- ✅ View all attendance history  
- ✅ Calculate **attendance percentage** per student & subject  
- ✅ Delete attendance records by date  
- ✅ Clean and responsive UI  

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, Jinja2 Templates  

---

## 📂 Project Structure
📁 student-attendance-system
│── app.py # Main Flask app
│── setup_db.py # Database setup (creates tables & inserts sample data)
│── attendance.db # SQLite Database (auto-created after running database1.py)
│── static/
│ └── style.css # CSS styling
│── templates/
│ ├── index.html # Attendance form
│ ├── report.html # Attendance report & summary
│ └── percentages.html # Extra percentage view (optional)
│── README.md
Setup database:
python database1.py

Run Flask app:
python app1.py
Open in browser:
👉 http://127.0.0.1:5000/

📊 Example Workflows

Mark Attendance → Select student, subject, status → Submit

View Report → Shows all records + attendance percentage

Delete Records → Choose a date → Delete attendance for that day
<img width="1361" height="636" alt="image" src="https://github.com/user-attachments/assets/19a0a267-5299-4832-9efc-9f88663bd5dd" />
<img width="1351" height="625" alt="image" src="https://github.com/user-attachments/assets/1fb536ac-294d-4adf-9a83-963ccd16d81d" />
<img width="1363" height="629" alt="image" src="https://github.com/user-attachments/assets/fe038e98-98d0-4021-91ed-0658ec264b73" />





