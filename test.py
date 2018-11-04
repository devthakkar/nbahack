from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playerdashboardbylastngames
from nba_api.stats.static import players

player_info = commonplayerinfo.CommonPlayerInfo(2544, "00")
lebron_dict = player_info.common_player_info.get_dict()
# lebron_log = playergamelog.PlayerGameLog(2544, 2017-18, "Regular Season")
# print(lebron_log)
lebron_last_5_games = playerdashboardbylastngames.PlayerDashboardByLastNGames(2544, 0, "Base", 0, 0, "N", "PerGame", 0, "N", "N", "2017-18", "Regular Season")
#lebron_last_5_games_2 = playerdashboardbylastngames.PlayerDashboardByLastNGames(2544, 0, "Base", 0, 0, "N", "PerGame", 0, "N", "N", "2017-18", "Regular Season", "03-20-2018", "03-10-2018")
lebron_5_game_dict = lebron_last_5_games.last5_player_dashboard.get_dict()
#lebron_5_game_dict_2 = lebron_last_5_games_2.last5_player_dashboard.get_dict()
print("Player:" + lebron_dict.get('data')[0][3] + ", Number: " + lebron_dict.get('data')[0][13] + "\n")
print(lebron_5_game_dict.get('data')[0][28])
print(players.find_players_by_full_name('LeBron James')[0].get('id'))
#print(lebron_5_game_dict_2.get('data')[0][28])
#print(lebron_5_game_dict_2)
