from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from dotenv import load_dotenv
import os


app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key_here'


def try_connect_db():
    try:
        return mysql.connector.connect(
            host='localhost',
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database='banking_platform'
        )
    except mysql.connector.Error:
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        database = try_connect_db()
        if database is None:
            return '<h1>Loading...</h1>'

        cursor = database.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND user_password = '{password}'")
        user = cursor.fetchone()

        if user:
            session['user'] = user
            # If the user exists in the database, redirect to transactions page
            return redirect(url_for('transactions'))
        else:
            # If the login fails, show an error message
            flash('Invalid username or password', 'error')

    return render_template('index.html')


@app.route('/transactions')
def transactions():
    if 'user' not in session:
        # User is not logged in, redirect to login page
        return redirect(url_for('index'))
    
    user = session['user']

    database = try_connect_db()
    if database is None:
        return '<h1>Loading...</h1>'
    
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM transactions WHERE user_id = '{user['user_id']}'")
    transactions = cursor.fetchall()

    return render_template('transactions.html', transactions=transactions, full_name=user['full_name'])


@app.route('/logout')
def logout():
    # Remove the user information from the session
    session.pop('user', None)
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)