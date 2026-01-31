from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import time

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# Create table on startup with retry logic
def init_db():
    max_retries = 5
    for attempt in range(max_retries):
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                dob DATE,
                degree VARCHAR(50),
                year_of_passing INT,
                branch VARCHAR(100),
                email VARCHAR(100),
                phone VARCHAR(15)
            )
            """)
            db.commit()
            db.close()
            print("Database initialized successfully")
            return
        except Exception as e:
            print(f"Database connection attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                print("Failed to initialize database after retries")

init_db()

# Home → Add Student ONLY
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            data = (
                request.form["name"],
                request.form["dob"],
                request.form["degree"],
                int(request.form["year"]),
                request.form["branch"],
                request.form["email"],
                request.form["phone"]
            )

            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO students
                (name, dob, degree, year_of_passing, branch, email, phone)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, data)
            db.commit()

            return redirect("/")   # stays on form page

        except Exception as e:
            print("DB ERROR:", e)
            return "Error saving student data"

    return render_template("index.html")

# View Students page
@app.route("/students")
def students():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
