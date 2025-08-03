# Student Registration + Natural Language SQL Querying
A full-stack web app that combines:

- Student registration form with SQL Server backend

- AI-powered natural language queries via Google Gemini

- Admin interface to convert Natural Language to SQL and view results

- Selenium WebDriver automation to auto-fill forms

- Dynamic ID assignment, case-insensitive searches, and smart query detection

## Features
- Register student info via a user-friendly web form

- Store entries in Microsoft SQL Server

- Ask questions in plain English like:

  - “How many students are in Signals and Systems?”

  - “Who are the females enrolled in Data Structures?”

- Automatically fixes common case mismatches

- Automate form submissions with Selenium

## Tech Stack
| Layer     | Tools/Tech                          |
| --------- | ----------------------------------- |
| Frontend  | HTML, GitHub Pages                  |
| Backend   | Python (Flask)                      |
| AI Engine | Google Gemini 1.5 Flash via API     |
| Database  | Microsoft SQL Server (via `pyodbc`) |
| Testing   | Selenium WebDriver (Chrome)         |


## How to Run the Project
1. Clone the repository
```bash

git clone https://github.com/Venky-dll/student-registration-form.git
cd student-registration-form
```

2. Install dependencies
```bash
pip install flask selenium pyodbc google-generativeai

```
3. Set your SQL Server configuration in app.py
Edit these lines in the script:<br>
<br>
                    conn = pyodbc.connect(<br>
                        r'DRIVER={SQL Server};'<br>
                        r'SERVER=YourServerName;'<br>
                        r'DATABASE=YourDatabaseName;'<br>
                        r'Trusted_Connection=yes;'<br>
                    )<br>

4. Replace Gemini API Key
In app.py, set your API key from Google AI Studio:
```bash
genai.configure(api_key="your-api-key-here")

```

5. Run the Flask app
```bash
python app.py
```
Then open:
```bash 
http://127.0.0.1:5000 — for student registration
http://127.0.0.1:5000/query — for admin natural language querying
```
## File Structure
student-registration-form/<br>
│<br>
├── templates/<br>
│   ├── form.html              # Student form UI<br>
│   ├── success.html           # Registration confirmation<br>
│   ├── nl_query.html          # Admin Natural Language to SQL interface<br>
│   └── results.html           # SQL results display<br>
│<br>
├── app.py                     # Flask backend + Gemini integration<br>
├── multiple_entries.py        # Selenium script for automation (optional)<br>
└── README.md                  # Project documentation (this file)<br>
## Example Queries (Admin Panel)
--“Show all students”

--“List names of males in Data Structures”

--“How many are in Signals & Systems?”

--“Who are the students aged over 21?”

## Works even with:

Miscapitalized queries

Slightly mistyped input (autocorrect support in progress)
