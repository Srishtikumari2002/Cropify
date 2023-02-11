from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import pickle

# creating flask object
app = Flask(__name__)



model1 = pickle.load(open('./models/rainfall_pred_RandomForest.pkl','rb'))


model2 = joblib.load("./models/random_forest_crop.joblib")

def Predict2(state,district,year,month,price,soil):
    y_pred = model2.predict([state,district,year,month,price,soil])
    print(y_pred)
    return y_pred

def Predict1(rainfall_year,rainfall_month):
    y_pred = model1.predict([[rainfall_year,rainfall_month]])
    print(y_pred)
    return y_pred

@app.route('/')
def home():
    return render_template('Index.html')


@app.route('/rainfall', methods=['GET', 'POST'])
def get_rainfall():
    if (request.method == 'POST'):
        rainfall_year = request.form.get('rainfall_year')
        rainfall_month = request.form.get('rainfall_month')
        return render_template('Index.html', prediction=Predict1(rainfall_year,rainfall_month) )
        

    return render_template('Index.html')


@app.route('/prediction', methods=['GET', 'POST'])
def get_val():
    if (request.method == 'POST'):
        
        state = request.form.get('state')
        district = request.form.get('district')
        year = request.form.get('year')
        month = request.form.get('month')
        price = request.form.get('price')
        soil = request.form.get('soil')  
        return render_template('Index.html', prediction=Predict2(state, district, year, month, price, soil) )

    return render_template('Index.html')


if __name__=='__main__':
    app.run()