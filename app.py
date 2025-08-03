from flask import Flask, request, render_template
import pyodbc
import google.generativeai as genai
import re

app = Flask(__name__)

# SQL Server connection
conn = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=your_server_name;'
    r'DATABASE=StudentsDB;'
    r'Trusted_Connection=yes;'
)

# Gemini setup
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual API key
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Registration form
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        gender = request.form['gender']
        course = request.form['course']

        cursor = conn.cursor()
        cursor.execute("SELECT ID FROM Students ORDER BY ID")
        existing_ids = [row[0] for row in cursor.fetchall()]

        new_id = 1
        for id in existing_ids:
            if id == new_id:
                new_id += 1
            else:
                break

        cursor.execute(
            "INSERT INTO Students (ID, Name, Email, Age, Gender, Course) VALUES (?, ?, ?, ?, ?, ?)",
            (new_id, name, email, age, gender, course)
        )
        conn.commit()

        return render_template('success.html', student_name=name)
    return render_template('form.html')

# Admin view
@app.route('/nl2sql', methods=['POST'])
def nl_to_sql():
    try:
        user_input = request.form['query']
        user_input_cleaned = user_input.lower().replace(" and ", " & ")

        prompt = f"""
        You are an expert SQL developer. Convert the following natural language query into a single valid SQL Server SELECT statement ONLY. 
        The table is named Students with these columns: ID, Name, Email, Age, Gender, Course.

          Rules:
        - Do NOT explain the query.
        - Do NOT return any text outside the SQL code.
        - Do NOT use markdown syntax like ```sql.
        - Use COLLATE SQL_Latin1_General_CP1_CI_AS for case-insensitive comparison in WHERE clauses.
        - For questions like \"how many\", use COUNT(*).
        - For \"who are they\", return Name or relevant columns.
        - Only one valid SQL statement must be returned.

        Query: "{user_input_cleaned}"
        """

        response = model.generate_content(prompt)
        sql_query = re.sub(r"```sql|```", "", response.text).strip()

        if not sql_query.lower().startswith("select") or "you" in sql_query.lower():
            return "Gemini generated invalid SQL. Try rephrasing your query."

        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

        return render_template("results.html", query=sql_query, results=rows, columns=columns)

    except Exception as e:
        return f"Gemini API or SQL error: {str(e)}"

# Admin form interface
@app.route('/query', methods=['GET', 'POST'])
def query_page():
    if request.method == 'POST':
        return nl_to_sql()
    return render_template('nl_query.html')

if __name__ == '__main__':
    app.run(debug=True)
