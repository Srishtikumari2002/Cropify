from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

# creating flask object
app = Flask(__name__)


model = joblib.load("./random_forest.joblib")

def Predict(state,district,year,month,price,soil):
    y_pred = model.predict(state,district,year,month,price,soil)
    print(y_pred)
    return y_pred


@app.route('/', methods=['GET', 'POST'])
def get_val():
    if (request.method == 'POST'):
        state = request.form.get('state')
        district = request.form.get('district')
        year = request.form.get('year')
        month = request.form.get('month')
        price = request.form.get('price')
        soil = request.form.get('soil')  
        return render_template('crop.html', prediction=Predict(state, district, year, month, price, soil) )

    return render_template('crop.html')

if __name__=='__main__':
    app.run()