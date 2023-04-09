from flask import current_app as app
from flask_login import login_required, current_user
from flask import render_template,request 


@app.route("/")
def index():
    
    """create a homepage that allow users to login and view what they can do"""

    return render_template('index.html')

@app.route("/test371371")
def test():
    
    """create a testing page for own use"""
    list = db.session.execute(db.select(data).scalars())
    return render_template('test.html',list=list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return render_template('login.html')



@app.route("/store")
def store():
    return "placeholder"


@app.route("/data-entry",methods=['GET','POST'])
def data_entry():
    return render_template('data-entry.html')


@app.route("/predict")
def predict():
    return render_template('predict.html')