from flask import current_app as app
from flask_login import login_required, current_user
from flask import render_template


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return render_template('login.html')



@app.route("/store")
def store():
    return "placeholder"


@app.route("/data-entry")
def data_entry():
    return render_template('data-entry.html')


@app.route("/predict")
def predict():
    return "placeholder3"