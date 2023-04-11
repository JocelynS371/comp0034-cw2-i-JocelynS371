from flask import current_app as app
from flask_login import login_required, current_user, logout_user, login_user
from flask import render_template,request, flash, redirect, url_for
from . import db
from .models import Data,User
from .forms import UserForm, LoginForm, PredictionForm
from pathlib import Path
import pickle
from datetime import datetime

model_file = Path('flask_app/data/model_temp.sav')
with open(model_file, 'rb') as f:
    model = pickle.load(f)

@app.route("/")
def index():
    
    """create a homepage that allow users to login and view what they can do"""

    return render_template('index.html')

@app.route("/test371371")
def test():
    #data_entries = data.query.all()
    #return render_template('test.html', data_entries=data_entries)
    #return print(f'the attribute is {dir(User())}')
    return dir(current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        new_user = User(username=username, password = password)
        db.session.add(new_user)
        db.session.commit()
        text = f'Register Success, please remember your password {username}'
        return text
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are logged in already')
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user=User.check_credentials(username,password)
        if user is not None:
            flash('Logged in successfully!')
            login_user(user)
            return redirect(url_for('index'))
        elif user is None:
            error = 'Invalid username or password.'
            return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/store")
@login_required
def store():
    return "placeholder"


@app.route('/data-entry', methods=['GET', 'POST'])
@login_required
def data_entry():
    if request.method == 'POST':
        index = int(request.form['entry_id'])
        data_entry = data.query.get(index)
        return render_template('data-entry.html', data_entry=data_entry)
    return render_template('data-entry.html')


@app.route("/predict", methods=['GET','POST'])
@login_required
def predict():
    if request.method == 'POST':
            date_str = datetime.strptime(request.form['date'],'%Y-%m-%d')
            date = datetime.toordinal(date_str)
            longitude = request.form['longitude']
            latitude = request.form['latitude']

            # perform prediction
            prediction = model.predict([[date, longitude, latitude]])[0]

            # render the prediction result in the same page
            return render_template('predict.html', prediction=prediction)

    return render_template('predict.html')