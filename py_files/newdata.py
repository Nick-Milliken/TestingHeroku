import pandas as pd
import json
import numpy as np

data = pd.read_csv("https://github.com/Nick-Milliken/deploy-ml/raw/main/ramen/ramen-ratings.csv")
newdata = data.tail(516)
newdata = newdata.iloc[5]
newdata = pd.DataFrame(newdata)
print(newdata)

