import os
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playerdashboardbylastngames
from nba_api.stats.static import players


class Player(object):
	def __init__(self, id):
		self.id = id
		self.player_info = commonplayerinfo.CommonPlayerInfo(self.id).common_player_info.get_dict().get('data')[0]
		self.name = self.player_info[3]
		self.number = self.player_info[13]
		self.height = self.player_info[10]
		self.weight = self.player_info[11]
		self.team = self.player_info[17]
		self.birth_year = int(self.player_info[6][0:4])
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

	def getAge(self):
		return 2018 - self.birth_year

def nameToId(player_name):
	return players.find_players_by_full_name(player_name)[0].get('id')

KD = nameToId("Javale McGee")
lebronJames = Player(KD)
lebronJames.get5Performances()
lebronJames.printTester()


