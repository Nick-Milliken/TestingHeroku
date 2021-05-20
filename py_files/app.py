#import sqlite3
from flask import Flask, render_template
#from werkzeug.exceptions import abort

app = Flask(__name__)

#def get_db_connection():
#    conn = sqlite3.connect('database.db')
#    conn.row_factory = sqlite3.Row
#    return conn

#def get_prediction(prediction_id):
#    conn = get_db_connection()
#    prediction = conn.execute('SELECT * FROM prediction').fetchall()
#    conn.close()
#    if prediction is None:
#        abort(404)
#    return prediction

#app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()


