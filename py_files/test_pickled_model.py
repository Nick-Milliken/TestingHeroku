from sklearn.linear_model import LogisticRegression 
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pickle 
import pandas as pd
import numpy as np

data = pd.read_csv("https://github.com/Nick-Milliken/deploy-ml/raw/main/ramen/ramen-ratings.csv")
origin_data = data.head(2064)
newdata = data.tail(516)

with open('model.pkl', 'rb') as g:
    pipe = pickle.load(g)
#print(pipe)
Probability = list(pipe)

predictions = pd.DataFrame({'Country':newdata.Country, 'Brand':newdata.Brand, 'Probability of 5.00':Probability})
print(predictions)



