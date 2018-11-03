from nba_api.stats.endpoints import commonplayerinfo
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
lebron_dict = player_info.common_player_info.get_dict()
print("Player:" + lebron_dict.get('data')[0][3] + ", Number: " + lebron_dict.get('data')[0][13])