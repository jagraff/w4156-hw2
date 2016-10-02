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
DATABASE_URI = 'postgresql://dyn-160-39-252-160.dyn.columbia.edu:5432/userpass'
engine = create_engine(DATABASE_URI)

g.conn = engine.connect()

cursor = g.conn.execute('Select * from userpass')

print(cursor.fetchone())


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
