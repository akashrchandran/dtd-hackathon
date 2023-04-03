import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "superawsomepass"
app.config["SESSION_PERMANENT"] =  False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def init_db():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, email Text not null , password TEXT not null, name TEXT not null, patient BOOL not null)')
    con.commit()
    con.close()

def register_user_to_db(email, password, name, patient):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(email,password, name, patient) values (?,?,?,?)', (email, password, name, patient))
    con.commit()
    con.close()

def get_user(user_id):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    res = cur.execute('Select * FROM users WHERE user_id=?', str(user_id))
    res = res.fetchone()
    con.commit()
    con.close()
    return res

def check_user(email, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('Select user_id,email,password FROM users WHERE email=? and password=?', (email, password))
    res = cur.fetchone()
    con.close()
    return res

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method != 'POST':
        return render_template('register.html')
    print("POST")
    email = request.form['email']
    password = request.form['password']
    name = request.form['f_name'] + " " + request.form['l_name']
    patient = bool(request.form['patient'])
    register_user_to_db(email, password, name, patient)
    return redirect(url_for('login'))


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method != 'POST':
        return render_template('login.html')
    email = request.form['email']
    password = request.form['password']
    if res := check_user(email, password):
        session['user_id'] = res[0]
        session.modified = True
    return redirect(url_for('home'))


@app.route('/home', methods=['POST', "GET"])
def home():
    if 'user_id' not in session:
        return "Username or Password is wrong!"
    details = get_user(session['user_id'])
    return (
        render_template('patient.html', details=details)
        if details[4]
        else render_template('doctor.html', details=details)
    )


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0',debug=False)