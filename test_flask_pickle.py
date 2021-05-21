import numpy as np
import pandas as pd
import pickle
from newdata import newdata

X = newdata.Stars
X = pd.to_numeric(X)
X = np.nan_to_num(X)
X = X.reshape(-1,1)

with open('model.pkl', 'rb') as f:
    pipe = pickle.load(f)

print(pipe)

predictions = pipe.predict(X)
print(predictions)
