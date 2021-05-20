from sklearn.pipeline import Pipeline
from flask import Flask
import requests
import pandas as pd
import numpy as np
import pickle 
from flask import render_template

app = Flask(__name__)

from newdata import newdata as newdata

with open('Probability.pkl', 'rb') as g:
       pipe = pickle.load(g)
print(pipe)        
@app.route('/')
def index():
    return '<p1>Index Page</p1>'

@app.route('/hello')
def homeview():
     
    return 'Hello, World!'

@app.route('/json_test')
def json_test():
    return {'prediction':.05}

@app.route('/predict', methods = ['GET','POST'])
def predict():
        
        prediction = pipe.predict_proba(newdata[['Stars']])
        prediction = prediction.reshape(1,-1)
        prediction = prediction.tolist() 
       # output = pd.DataFrame({'Country': newdata.Country, 'Brand':newdata.Brand, 'Probability of 5.00 Stars':prediction})
       # print(output)
        return {'prediction.html': prediction}



