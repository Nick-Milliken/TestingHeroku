from flask import Flask, request
import requests
import pickle

app = Flask(__name__)

#with open('model.pkl', 'rb') as f:
 #   pipe = pickle.load(f)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/json_test')
def json_test():
    return  {'key': 'value'}

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        the_data = request.get_json(force=True)
        newdata = the_data['newdata']
        prediction = pipe.predict([newdata])
        return {'prediction': prediction.tolist()}
