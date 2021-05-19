import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_prediction(prediction_id):
    conn = get_db_connection()
    prediction = conn.execute('SELECT * FROM predictions').fetchall()
    conn.close()
    if prediction is None:
        abort(404)
    return prediction

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    predictions = conn.execute('SELECT * FROM predictions').fetchall()
    conn.close()
    if prediction is None:
       abort(404)
    return prediction

@app.route('/prediction_id')
def prediction(prediction_id):
    prediction = get_prediction(prediction_id)
    return render_template('prediction.html', prediction=predictions)
