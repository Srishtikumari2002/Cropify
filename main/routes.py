from flask import render_template

from main import app

@app.route('/')
def index():
    """View for home page"""
    return render_template('index.html')

@app.get('/predict')
def predict():
    response = {
        'status': 200,
        'text': 'The API request was successfull.'
    }
    return response