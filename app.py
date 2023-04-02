import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "superawsomepass"
app.config["SESSION_PERMANENT"] =  False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def register_user_to_db(email, password, name, patient):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(email,password, name, patient) values (?,?,?,?)', (email, password, name, patient))
    con.commit()
    con.close()


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
    print(session)
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return "Username or Password is wrong!"


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)