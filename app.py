from flask import Flask, render_template, request
import pandas as pd
import numpy as np

# creating flask object
app = Flask(__name__)


model = joblib.load("./random_forest.joblib")
@app.route('/', methods=['GET', 'POST'])
def Predict(state,district,year,month,price,soil):
    y_pred = model.predict(state,district,year,month,price,soil)
    return y_pred


@app.route('/', methods=['GET', 'POST'])
def get_val():
    if (request.method == 'POST'):

        if request.form["Submit_B"]=="newsContent":
            text = request.form.get('content')
            return render_template('Index.html', prediction=Predict(text) , scroll="detection")

    return render_template('Index.html')
