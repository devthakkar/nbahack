from flask import Flask, send_from_directory
from flask import jsonify
import os
from nba_api.stats.endpoints import commonplayerinfo

app = Flask(__name__)

@app.route('/test')
def hello_world():
    return "Welcome! Here are your investment options:"
    

@app.route('/LebronJames')
def lb():
    ret = {}
    ret["name"] = "Lebron James"
    ret["image"] = "./img/player-img/kevin-durant.png"
    return jsonify(ret)

@app.route('/StephenCurry')

@app.route('/Giannis')

@app.route('/AnthonyDavis')

@app.route('/KevinDurant')
def kd():
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
    lebron_dict = player_info.common_player_info.get_dict()
    return "Name:" + lebron_dict.get('data')[0][3] + " , Age: " + lebron_dict.get('data')[0][13]

@app.route('/player', methods=['GET'])
def get_player():
    return 'hello' 
    
@app.route('/', methods=['GET'], defaults={'path': 'index.html'})

@app.route('/<path:path>', methods=['GET'])
def static_file(path):
    return send_from_directory('.', path)
