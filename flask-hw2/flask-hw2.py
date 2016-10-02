from flask import Flask
import os
import hashlib
import re
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response, session

app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/userpass'
DATABASE_URI = "postgresql://dyn-160-39-252-160.dyn.columbia.edu/users"
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


if __name__ == '__main__':
    app.run()
