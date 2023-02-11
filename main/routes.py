from flask import render_template, request, jsonify
import requests
import pickle
from main import app


@app.route('/')
def inderesponse():
    """View for home page"""
    return render_template('index.html')


def predictRainfall(month, year, state):
    dict_subcode = {'andhra pradesh': 5,
                    'arunachal pradesh': 1,
                    'assam': 2,
                    'bihar': 3,
                    'chhattisgarh': 4,
                    'goa': 17,
                    'gujarat': 11,
                    'haryana': 12,
                    'himachal Pradesh': 13,
                    'jammu and Kashmir': 14,
                    'jharkhand': 15,
                    'karnataka': 6,
                    'kerala': 16,
                    'madhya pradesh': 33,
                    'maharashtra': 19,
                    'manipur': 21,
                    'meghalaya': 2,
                    'mizoram': 21,
                    'nagaland': 21,
                    'odisha': 23,
                    'punjab': 24,
                    'rajasthan': 34,
                    'sikkim': 28,
                    'tamil nadu': 29,
                    'telangana': 30,
                    'tripura': 21,
                    'uttarakhand': 31,
                    'uttar pradesh': 35,
                    'west bengal': 28,
                    'andaman and nicobar islands': 0,
                    'chandigarh': 12,
                    'dadra and dagar haveli': 11,
                    'daman and diu': 11,
                    'delhi': 12,
                    'lakshadweep': 18,
                    'puducherry': 29}

    subcode = dict_subcode[state.lower()]
    model1 = pickle.load(
        open("main/models/rainfall_RandomForest_subdivision.pkl", 'rb'))
    rainfall = model1.predict([[subcode, year, month+1]])

    return rainfall[0]


def humidity(city):
    "Fetches Weather Data from internet."

    apiKey = 'bd24ff775533424d61ed37722e8e4c38'
    baseUrl = 'http://api.openweathermap.org/data/2.5/weather?'

    url = baseUrl + "appid=" + apiKey + "&q=" + city
    response = requests.get(url).json()

    if response['cod'] != '404':

        y = response["main"]

        return y['humidity']

    return 404


def predictTemp(city, month, year):

    cityCodes = {
        "Chennai": 0,
        "Bangalore": 1,
        "Delhi": 2,
        "Lucknow": 3,
        "Mumbai": 4,
        "Rajasthan": 5,
        "Bhubhneshwar": 6,
        "Rourkela": 7,
    }
    model1 = pickle.load(open("main/models/temp_pred.pkl", 'rb'))
    temperature = model1.predict([[cityCodes[city], month+1, year]])
    return temperature[0]


def soilComp(state):
    state_NKP = {'andhra pradesh': [1, 2, 0],
                 'arunachal pradesh': [1, 0, 0],
                 'assam': [2, 2, 0],
                 'bihar': [0, 0, 2],
                 'chhattisgarh': [0, 2, 0],
                 'goa': [0, 2, 1],
                 'gujarat': [1, 2, 0],
                 'haryana': [0, 2, 1],
                 'himachal pradesh': [2, 1, 0],
                 'jammu and kashmir': [1, 2, 1],
                 'jharkhand': [0, 0, 0],
                 'karnataka': [1, 2, 0],
                 'kerala': [0, 2, 1],
                 'madhya pradesh': [1, 2, 0],
                 'maharashtra': [1, 2, 0],
                 'manipur': [0, 0, 0],
                 'meghalaya': [2, 1, 0],
                 'mizoram': [2, 1, 0],
                 'nagaland': [2, 0, 0],
                 'odisha': [1, 1, 0],
                 'punjab': [1, 2, 0],
                 'rajasthan': [0, 0, 1],
                 'sikkim': [1, 0, 0],
                 'tamil nadu': [2, 2, 1],
                 'telangana': [0, 2, 0],
                 'tripura': [1, 1, 0],
                 'uttarakhand': [2, 2, 1],
                 'uttar pradesh': [2, 1, 0],
                 'west bengal': [2, 2, 0],
                 'andaman and nicobar islands': [2, 1, 0],
                 'chandigarh': [1, 2, 0],
                 'dadra and nagar haveli': [1, 2, 1],
                 'daman and diu': [1, 2, 0],
                 'delhi': [2, 1, 0],
                 'lakshadweep': [0, 1, 1],
                 'puducherry': [2, 2, 2]}

    NKP = state_NKP[state.lower()]
    return NKP


def predictCrop(soil, temp, humid, rainfall):

    model = pickle.load(open("main/models/Crop_RandomForest_soil.pkl", 'rb'))
    crop = model.predict([soil+[temp, humid, rainfall]])

    return int(crop[0])


@ app.get('/predict')
def predict():
    """Predicts the crops which should be grown."""

    month = int(request.args.get('month'))
    year = int(request.args.get('year'))
    city = request.args.get('city')

    cityStates = {
        "Chennai": 'tamil nadu',
        "Bangalore": 'karnataka',
        "Delhi": 'delhi',
        "Lucknow": 'uttar pradesh',
        "Mumbai": 'maharashtra',
        "Rajasthan": 'rajasthan',
        "Bhubhneshwar": 'odisha',
        "Rourkela": 'west bengal',
    }

    crops_dict = {
        0: 'apple',
        1: 'banana',
        2: 'blackgram',
        3: 'chickpea',
        4: 'coconut',
        5: 'coffee',
        6: 'cotton',
        7: 'grapes',
        8: 'jute',
        9: 'kidneybeans',
        10: 'lentil',
        11: 'maize',
        12: 'mango',
        13: 'mothbeans',
        14: 'mungbean',
        15: 'muskmelon',
        16: 'orange',
        17: 'papaya',
        18: 'pigeonpeas',
        19: 'pomegranate',
        20: 'rice',
        21: 'watermelon',
    }

    state = cityStates[city]

    response = {}
    response['soilComp'] = soilComp(state)
    response['rainfall'] = round(predictRainfall(month, year, state), 2)
    response['temperature'] = round(predictTemp(city, month, year), 2)
    response['humidity'] = humidity(city)

    if response['humidity'] != 404:
        response['status'] = 200
        response['message'] = 'Api call successfull.'
        response['crop'] = crops_dict[predictCrop(
            response['soilComp'], response['temperature'], response['humidity'], response['rainfall'])]
    else:
        response['status'] = 404
        response['message'] = 'City not found.'

    print(response)

    return jsonify(response)
