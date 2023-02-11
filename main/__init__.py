from flask import Flask
import pandas as pd
import numpy as np
import joblib
import pickle

app = Flask(__name__)

from main import routes