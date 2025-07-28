from flask import Flask, request, render_template
import pyodbc

app = Flask(__name__)

# Database connection
conn = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=Venkat\SQLEXPRESS01;'
    r'DATABASE=StudentsDB;'
    r'Trusted_Connection=yes;'
)



@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        gender = request.form['gender']
        course = request.form['course']

        cursor = conn.cursor()

        # Step 1: Get all existing IDs
        cursor.execute("SELECT ID FROM Students ORDER BY ID")
        existing_ids = [row[0] for row in cursor.fetchall()]

        # Step 2: Find smallest missing ID
        new_id = 1
        for id in existing_ids:
            if id == new_id:
                new_id += 1
            else:
                break

        # Step 3: Insert new student with that ID
        cursor.execute(
            "INSERT INTO Students (ID, Name, Email, Age, Gender, Course) VALUES (?, ?, ?, ?, ?, ?)",
            (new_id, name, email, age, gender, course)
        )
        conn.commit()

        return render_template('success.html', student_name=name)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
