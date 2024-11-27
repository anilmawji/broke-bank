from flask import Flask, render_template
import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__, template_folder='templates')


def try_connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database="banking_platform"
        )
    except mysql.connector.Error:
        return None


@app.route('/')

def index():
    database = try_connect_db()

    if database is None:
        return "<h1>Loading...</h1>"
    
    cursor = database.cursor()

    user_input = "janesmith2@email.com' OR 1=1 -- "
    query = f"SELECT * FROM users WHERE email_address = '{user_input}'"

    cursor.execute(query)
    result = cursor.fetchall()

    for x in result:
        print(x)

    return render_template('index.html', logged_in=True)


@app.route('/transactions')

def transactions():
    return render_template('transactions.html', logged_in=True)


@app.errorhandler(404)

def page_not_found(e):
    return render_template('404.html'), 404


