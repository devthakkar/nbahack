from flask import Flask
from nba_api.stats.endpoints import commonplayerinfo
app = Flask(__name__)

@app.route('/')
def hello_world():
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
    lebron_dict = player_info.common_player_info.get_dict()
    return "Name:" + lebron_dict.get('data')[0][3] + " , Age: " + lebron_dict.get('data')[0][13]