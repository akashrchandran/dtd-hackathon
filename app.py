import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "superawsomepass"
app.config["SESSION_PERMANENT"] =  False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def register_user_to_db(username, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(username,password) values (?,?)', (username, password))
    con.commit()
    con.close()


def check_user(username, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('Select username,password FROM users WHERE username=? and password=?', (username, password))
    return bool(cur.fetchone())


@app.route("/")
def index():
    return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method != 'POST':
        return render_template('register.html')
    username = request.form['username']
    password = request.form['password']

    register_user_to_db(username, password)
    return redirect(url_for('index'))


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method != 'POST':
        return redirect(url_for('index'))
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    print(check_user(username, password))
    if check_user(username, password):
        print("saved")
        session['username'] = username
        session.modified = True
    return redirect(url_for('home'))


@app.route('/home', methods=['POST', "GET"])
def home():
    print(session)
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return "Username or Password is wrong!"


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)