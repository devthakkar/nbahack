from flask import Flask
from nba_api.stats.endpoints import commonplayerinfo
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome! Here are your investment options:"
    

@app.route('/LebronJames')

@app.route('/StephenCurry')

@app.route('/Giannis')

@app.route('/AnthonyDavis')

@app.route('/Kevin Durant')