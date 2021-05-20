from sklearn.linear_model import LogisticRegression 
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pickle 
import pandas as pd
import numpy as np
import json

from newdata import newdata 

print(newdata.head())

with open('model.pkl', 'rb') as g:
    pipe = pickle.load(g)

Probability = pipe.predict_proba(newdata['Stars'])


predictions = pd.DataFrame({'Country':newdata.Country, 'Brand':newdata.Brand, 'Probability of 5.00':Probability})
print(predictions)

with open('Probability.pkl', 'wb') as p:
    pickle.dump(Probability,p)

with open('Probability.pkl', 'rb') as prob:
    pickle.load(prob)

