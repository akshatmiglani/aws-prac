from flask import Flask, render_template, request
import pymysql
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

HOST=os.getenv("HOST")
USER=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")
DATABASE=os.getenv("DATABASE")
# Configure MySQL
db_config = {
    'host': HOST,
    'user': USER,
    'port':3306,
    'password': PASSWORD,
    'database': DATABASE ,
    'cursorclass': pymysql.cursors.DictCursor
}
print(db_config)
connection = pymysql.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

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

    try:
        with connection.cursor() as cursor:
            
            sql = "INSERT INTO feedback (roll_number, name, email, course_name, rating, question1, question2) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (roll_number, name, email, course_name, rating, question1, question2))

        connection.commit()

        return render_template('success.html')

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
