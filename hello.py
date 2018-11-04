from flask import Flask, send_from_directory
from flask import jsonify
import os
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playerdashboardbylastngames
from nba_api.stats.static import players


app = Flask(__name__)


class Player(object):
    def __init__(self, id):
        self.id = id
        self.player_info = commonplayerinfo.CommonPlayerInfo(self.id).common_player_info.get_dict().get('data')[0]
        self.name = self.player_info[3]
        self.number = self.player_info[13]
        self.height = self.player_info[10]
        self.weight = self.player_info[11]
        self.team = self.player_info[17]
        self.age = 2018 - int(self.player_info[6][0:4])
        #self.stock_value = #get stock value
        self.performances = []

    def get5Performances(self):
        self.performances.append(playerdashboardbylastngames.PlayerDashboardByLastNGames(self.id, 0, "Base", 0, 0, "N", "PerGame", 0, "N", "N", "2014-15", "Regular Season").last5_player_dashboard.get_dict().get('data')[0][28])
        self.performances.append(playerdashboardbylastngames.PlayerDashboardByLastNGames(self.id, 0, "Base", 0, 0, "N", "PerGame", 0, "N", "N", "2015-16", "Regular Season").last5_player_dashboard.get_dict().get('data')[0][28])
        self.performances.append(playerdashboardbylastngames.PlayerDashboardByLastNGames(self.id, 0, "Base", 0, 0, "N", "PerGame", 0, "N", "N", "2016-17", "Regular Season").last5_player_dashboard.get_dict().get('data')[0][28])
        self.performances.append(playerdashboardbylastngames.PlayerDashboardByLastNGames(self.id, 0, "Base", 0, 0, "N", "PerGame", 0, "N", "N", "2017-18", "Regular Season").last5_player_dashboard.get_dict().get('data')[0][28])
        self.performances.append(playerdashboardbylastngames.PlayerDashboardByLastNGames(self.id, 0, "Base", 0, 0, "N", "PerGame", 0, "N", "N", "2018-19", "Regular Season").last5_player_dashboard.get_dict().get('data')[0][28])

    def printTester(self):
        for item in self.performances:
            print(item)

    def getName(self):
        return self.name

    def returnValues(self):
        return {"Values": performances, "Number": self.number, "Height:" self.height, "Weight": self.weight, "Team": self.team, "Age": self.age}

def nameToId(player_name):
    return players.find_players_by_full_name(player_name)[0].get('id')

@app.route('/test')
def hello_world():
    return "Welcome! Here are your investment options:"
    

# @app.route('/LebronJames')
# def lb():
#     ret = {}
#     ret["name"] = "Lebron James"
#     ret["image"] = "./img/player-img/kevin-durant.png"
#     return jsonify(ret)

# @app.route('/StephenCurry')

# @app.route('/Giannis')

# @app.route('/AnthonyDavis')

# @app.route('/KevinDurant')
# def kd():
#     durantID = nameToID("Kevin Durant")
#     durant = Player(durantID)
#     durant.get5Performances
#     return jsonify(durant.returnValues())


    # player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
    # lebron_dict = player_info.common_player_info.get_dict()
    # return "Name:" + lebron_dict.get('data')[0][3] + " , Age: " + lebron_dict.get('data')[0][13]

@app.route('/player', methods=['GET'])
def get_player(player_name):
    return 'hello' 
    
@app.route('/', methods=['GET'], defaults={'path': 'index.html'})

@app.route('/<path:path>', methods=['GET'])
def static_file(path):
    return send_from_directory('.', path)
