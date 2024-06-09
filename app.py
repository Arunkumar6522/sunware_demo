from flask import Flask,render_template,request, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__, template_folder='templates', static_folder="static")

app.secret_key='karthick_studen_career_guidane'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='arundata'

mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Retrieving data from the form
    # name = request.form.get('name')
    # total_experience = request.form.getlist('Total_Experience')
    # branch_name = request.form.getlist('Branch_Name')
    # gender = request.form.get('gender')
    # communication = request.form.get('communication')
    # project_name = request.form.getlist('project_name')
    # primary_skills = request.form.getlist('primary_skills')
    # secondary_skills = request.form.getlist('secondary_skills')
    # interested_technology = request.form.getlist('Intrested Techonology')
    # language_interested = request.form.getlist('language_intrested')
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.form['name']
        total_experience = ', '.join(request.form.getlist('Total_Experience'))
        branch_name = ', '.join(request.form.getlist('Branch_Name'))
        gender = request.form['gender']
        communication = request.form['communication']
        project_name = ', '.join(request.form.getlist('project_name'))
        primary_skills = ', '.join(request.form.getlist('primary_skills'))
        secondary_skills = ', '.join(request.form.getlist('secondary_skills'))
        interested_technology = ', '.join(request.form.getlist('Intrested_Techonology'))
        language_interested = ', '.join(request.form.getlist('language_intrested'))

        # Insert data into MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO users (name, total_experience, branch_name, gender, communication, project_name, primary_skills, secondary_skills, interested_technology, language_interested) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (name, total_experience, branch_name, gender, communication, project_name, primary_skills, secondary_skills, interested_technology, language_interested)
        )
        mysql.connection.commit()
        cursor.close()

    return redirect('/#submitted')
# f"Form submitted successfully! Received: Name - {name} , Gender - {gender} ,{total_experience} ,{branch_name}, {communication},{project_name},{primary_skills},{secondary_skills},{interested_technology},{language_interested},  etc."

if __name__=='__main__':
    app.run(debug=True)
