from flask import current_app as app


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/predict")
def predict():
    return "placeholder"


@app.route("/place")
def place():
    return "placeholder2"