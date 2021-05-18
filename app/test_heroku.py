from sklearn.linear_model import LogisticRegression 
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from flask import Flask
import pandas as pd
import numpy as np

app = Flask(__name__)


data = pd.read_csv("https://github.com/Nick-Milliken/deploy-ml/raw/main/ramen/ramen-ratings.csv")

@app.route('/')
def homeview():
    return "<h1>Welcome to my NightMare</h1>"

@app.route('/prediction')
def prediction():
    with open('test_pickled_model.py', 'rb') as g:
        model = pickle.load(g)
        return model
