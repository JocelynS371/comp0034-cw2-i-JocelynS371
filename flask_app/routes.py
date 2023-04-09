from flask import current_app as app
from flask_login import login_required, current_user
from flask import render_template,request 
from . import db
from .models import data,user
from .forms import UserForm, LoginForm, PredictionForm

@app.route("/")
def index():
    
    """create a homepage that allow users to login and view what they can do"""

    return render_template('index.html')

@app.route("/test371371")
def test():
    
    """create a testing page for own use"""
    data_list = db.session.execute(db.select(data))
    return render_template('test.html',data_list=data_list)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        new_user = user(username=username, password = password)
        db.session.add(new_user)
        db.session.commit()
        text = f'Register Success, please remember your password {username}'
        return text
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user.check_credentials(username,password):
            return 'Logged in successfully!'
        else:
            error = 'Invalid username or password.'
            return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)






@app.route("/store")
def store():
    return "placeholder"


@app.route("/data-entry",methods=['GET','POST'])
def data_entry():
    return render_template('data-entry.html')


@app.route("/predict")
def predict():
    return render_template('predict.html')