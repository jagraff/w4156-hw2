import os
import hashlib
import re
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, session

app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/userpass'
DATABASE_URI = "postgresql://localhost/users"
engine = create_engine(DATABASE_URI)

app.secret_key = '\n\x1f\xe9(\xf0DdG~\xd4\x863\xa0\x10\x1e\xbaF\x10\x16\x7f(\x06\xb7/'

@app.route('/')
def hello_world():
    if 'username' not in session:
        return redirect('/login')
    g.conn = engine.connect()
    cursor = g.conn.execute('SELECT * FROM userpass WHERE username = %s', session['username'])
    return cursor.fetchone()[1]

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
        return redirect('/')

    return render_template("create.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        g.conn = engine.connect()
        cursor = g.conn.execute("SELECT pass FROM userpass WHERE username=%s",request.form['username'])
        passhash = cursor.first()[0]
        if passhash == None:
            return render_template('login.html', error="Incorrect username or password")
        password = request.form['password']
        print hashlib.md5(password).hexdigest()
        if passhash != hashlib.md5(password).hexdigest():
            return render_template('login.html', error="Incorrect password")

        session['username'] = request.form['username']
        return redirect('/')

    return render_template('login.html')


if __name__ == '__main__':
    app.run()
