from sqlalchemy import *
from flask import Flask, request, render_template, g, redirect, Response, session

app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/userpass'
DATABASE_URI = "postgresql://localhost/users"
engine = create_engine(DATABASE_URI)



@app.route('/')
def hello_world():
    g.conn = engine.connect()
    cursor = g.conn.execute('SELECT * FROM userpass')
    retpage = ""
    for userpass in cursor:
        user = userpass[0]
        pswd = userpass[1]
        retpage += "{0}: {1}<br>".format(user, pswd)
    return retpage

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if request.form['username'] == '' or\
                        'username' not in request.form:
            context = dict(error_message = "No username given")
            return render_template("create.html", **context)
        if request.form['password'] == '' or\
                        'password' not in request.form:
            context = dict(error_message = "No password given")
            return render_template("create.html", **context)
        if request.form['password_conf'] != request.form['password'] or\
                        'password' not in request.form:
            context = dict(error_message = "Passwords must match")
            return render_template("create.html", **context)

        username = request.form['username'].strip()
        passhash = hashlib.md5(request.form['password']).hexdigest()

        g.conn = engine.connect()

        cursor = g.conn.execute("SELECT * FROM userpass WHERE username=%s", username)

        if cursor.first() != None:
            context = dict(error_message = "User already exists")
            return render_template("create.html", **context)

        g.conn.execute("INSERT INTO userpass VALUES (%s, %s)", username, passhash)

    return render_template("create.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        g.conn = engine.connect()
        cursor = g.conn.execute("SELECT pass FROM userpass WHERE user=%s",request.form['username'])
        print(cursor.fetchone())
        try:
            pass
        except:
            print("Invalid username or password")
            return redirect('/')
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
