app = Flask(__name__)


data = pd.read_csv("https://github.com/Nick-Milliken/deploy-ml/raw/main/ramen/ramen-ratings.csv")

@app.route('/')
def homeview():
    return "<h1>Welcome to my NightMare</h1>"

@app.route('/prediction')
def table():
    with open('test_pickled_model.py', 'rb') as g:
	 model = pickle.load(g)
	 model = model.head()
	 return model
