from sklearn.linear_model import LogisticRegression 
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

import pandas as pd
import numpy as np

newdata = pd.read_csv("newdata.py")


pipe = with open('model.pkl', 'wb') as f: model = pickle.load(f)

predictions = pipe.predict_proba(newdata)
print(predictions)



