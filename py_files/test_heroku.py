#from sklearn.linear_model import LogisticRegression 
#from sklearn.preprocessing import StandardScaler
#from sklearn.datasets import make_classification
#from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle 
app = Flask(__name__)

with open('model.pkl', 'rb') as g:
        pipe = pickle.load(g)
        

data = pd.read_csv("https://github.com/Nick-Milliken/deploy-ml/raw/main/ramen/ramen-ratings.csv") 

newdata = data.tail(516)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def homeview():
    return "<h1>Welcome to my NightMare</h1>"

#@app.route('/json_test')
#def json_test():
#    return {'prediction':.05}

@app.route('/predict')
def predict():
    if request.method == 'POST':
       # the_data = request.get_json(force=True)
       # newdata = the_data['newdata']
        prediction = pipe.predict([newdata])
        return{'prediction': prediction.tolist()}   




