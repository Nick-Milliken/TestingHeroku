import requests
import json
import pickle

with open('model.pkl', 'rb') as f:
    pipe = pickle.load(f)

from newdata import newdata 

r = requests.post('http://127.0.0.1:5000/predict', data= {'newdata':newdata})
newdata = r.json()
prediction = newdata['prediction']
print(prediction)
