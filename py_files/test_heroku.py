from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from flask import Flask, request
from sklearn.linear_model import LogisticRegression
import requests
import pandas as pd
import numpy as np
import pickle 
from flask import render_template

app = Flask(__name__)

from newdata import newdata 
newdata = newdata.rename({newdata.columns[0]:'Value'})
#print(newdata)

with open('model.pkl', 'rb') as g:
       pipe = pickle.load(g)


X = newdata.iloc[5]
X = pd.to_numeric(X)
X = np.nan_to_num(X)
X = X.reshape(-1,1)
#X = int(X)
y = newdata.iloc[4]
#X = np.array(X, dtype=int, ndmin=2)
print('xtest',type(X))
print('ytest',type(y))
       

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/json_test')
def json_test():
    return '<p1>test_flask.py</p1>'


@app.route('/predict', methods = ['GET','POST'])
def predict():
    
    prediction = pipe.predict(X)
     
    output = pd.DataFrame({'Country': newdata.iloc[4], 'Brand':newdata.iloc[1], 'Predicted Country':prediction})
    print(output)
    return render_template('prediction.html')



