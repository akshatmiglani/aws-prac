from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'proj-db.cr2mgycg0xoo.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'akshat'
app.config['MYSQL_PASSWORD'] = '1234akshat'
app.config['MYSQL_DB'] = 'practice'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('feedback_form.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    # Get form data
    roll_number = request.form['roll_number']
    name = request.form['name']
    email = request.form['email']
    course_name = request.form['course_name']
    rating = int(request.form['rating'])
    question1 = request.form['question1']
    question2 = request.form['question2']

    # Store data in the MySQL database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO feedback (roll_number, name, email, course_name, rating, question1, question2) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (roll_number, name, email, course_name, rating, question1, question2))

    mysql.connection.commit()
    cur.close()

    return "Feedback submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
