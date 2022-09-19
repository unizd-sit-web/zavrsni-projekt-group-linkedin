import sqlite3 as sql
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    language = db.Column(db.String(30), nullable=False)


@app.route('/')
@app.route('/home/')
def home():
    return render_template("home.html")

@app.route('/search/')
def search():
    return render_template("search.html")

@app.route('/signUp/')
def signUp():
    return render_template("signUp.html")

@app.route('/confirm/', methods=['POST'])
def confirm(name, email, language):

    cur = sql.connect('users.db')
    c = cur.cursor()
    c.execute("INSERT INTO User (name, email, language) VALUES (%s, %s, %s)" %(name, email, language))
    cur.commit()

    return render_template("confirm.html")