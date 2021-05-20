from sklearn.linear_model import LogisticRegression 
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
import pickle
import pandas as pd
import numpy as np

data = pd.read_csv("https://github.com/Nick-Milliken/deploy-ml/raw/main/ramen/ramen-ratings.csv")
#newdata = data.tail(516)
origin_data = data.head(2064)


X = origin_data.Stars


X = X.replace('Unrated', np.NaN)
X = pd.to_numeric(X)
X = np.nan_to_num(X)
X = X.reshape(-1, 1)

y = origin_data.Country

X, y = X, y
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    random_state = 42)
pipe = Pipeline(steps=[('scaler', StandardScaler()), ('lr', LogisticRegression())])
# The pipeline can be used as any other estimator
# and avoids leaking the test set into the train set
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
pred = pipe.predict(X_train)
model = pipe
Country = pipe.predict(X)
Probability = list(pipe.predict_proba(X)[:,36])
Output = pd.DataFrame({'Country':origin_data.Country, 'Brand':origin_data.Brand,'Probability of 5.00 Stars':Probability})
Output.head()

model = Probability

with open('model.pkl', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)

#with open('model.pkl', 'rb') as g:
#    pickle.load(g)
