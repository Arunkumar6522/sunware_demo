from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__, template_folder="templates", static_folder="static")

app.secret_key = "karthick_studen_career_guidane"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "arundata"

mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit-form", methods=["POST"])
def submit_form():
    if request.method == "POST":
        try:
            # Retrieve data from the form
            name = request.form.get("name", "")
            total_experience = ", ".join(request.form.getlist("Total_Experience"))
            branch_name = ", ".join(request.form.getlist("Branch_Name"))
            gender = request.form.get("gender", "")
            communication = request.form.get("communication", "")
            project_name = ", ".join(request.form.getlist("project_name"))
            primary_skills = ", ".join(request.form.getlist("primary_skills"))
            secondary_skills = ", ".join(request.form.getlist("secondary_skills"))
            interested_technology = ", ".join(
                request.form.getlist("Intrested_Techonology")
            )
            language_interested = ", ".join(request.form.getlist("language_intrested"))
            email = request.form.get("email", "")

            # Ensure all required fields are present
            if not (name):
                return "Missing required fields"

            # Insert data into MySQL
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                "INSERT INTO users (name, total_experience, branch_name, gender, communication, project_name, primary_skills, secondary_skills, interested_technology, language_interested,email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    name,
                    total_experience,
                    branch_name,
                    gender,
                    communication,
                    project_name,
                    primary_skills,
                    secondary_skills,
                    interested_technology,
                    language_interested,
                    email,
                ),
            )
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            return f"An error occurred: {e}"

    return redirect("/?submitted=true")


if __name__ == "__main__":
    app.run(debug=True)
