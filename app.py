from email import message
import email
import sqlite3 as sql
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    language = db.Column(db.String(30), nullable=False)

    def __init__(self, name, email, language):
        self.name = name
        self.email = email
        self.language = language


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
def confirm():
    name = request.form.get("name")
    email = request.form.get("email")
    lang = request.form.get("language")

    usr = User(name, email, lang)
    db.session.add(usr)
    db.session.commit()

    '''msg=Message("Thanks for signing up!", sender=email)
    msg.add_recipient("petesic.donat@gmail.com")
    msg.body=('Thank you for signing up for our website!')

    Mail.send(msg)
    '''
    
    return render_template("confirm.html")