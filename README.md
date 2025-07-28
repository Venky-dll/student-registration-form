# 📝 Student Registration Form Automation

This project is a simple **web-based student registration form** that automates data entry using **Selenium WebDriver** and stores the submitted entries into a **SQL Server** database using **Flask** and **pyodbc**.

---

## 📌 Features

- HTML form for student registration.
- Python Flask backend to process submissions.
- Submissions stored in Microsoft SQL Server.
- Selenium-based automation to auto-fill and submit the form multiple times.
- Dynamic ID assignment that reuses deleted IDs.
- Thank you page after successful submission.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, GitHub Pages
- **Backend:** Python (Flask)
- **Database:** Microsoft SQL Server (via SSMS + pyodbc)
- **Automation:** Selenium WebDriver (Chrome)

---

## 🚀 How to Run the Project

### 1. Clone this repository

```bash

git clone https://github.com/Venky-dll/student-registration-form.git
cd student-registration-form 
```
### 2. Install dependencies
```bash

pip install flask selenium pyodbc
```
### 3. Set your SQL Server connection in app.py
Replace the SERVER, DATABASE, and TABLE values in the script: <br>
                  <sub> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;conn = pyodbc.connect( <br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;r'DRIVER={SQL Server};' <br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;r'SERVER=YourServerName;' <br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;r'DATABASE=YourDatabaseName;'<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;r'Trusted_Connection=yes;') <br></sub>
### 4. Run the Flask app
```bash
python app.py
```
App will run locally at:
```bash
http://127.0.0.1:5000
```

## 📂 File Structure

student-registration-form/<br>
│<br>
├── templates/<br>
│   ├── form.html<br>
│   └── success.html<br>
│<br>
├── app.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Flask backend<br>
└── README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# This file<br>


