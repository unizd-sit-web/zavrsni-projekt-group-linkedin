from flask import Flask, render_template

app = Flask(__name__)

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