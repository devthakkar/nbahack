from nba_api.stats.endpoints import commonplayerinfo
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
print(player_info.common_player_info.get_dict())