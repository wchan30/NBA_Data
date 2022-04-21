from nba_api.stats.endpoints import playercareerstats
import pandas as pd

#gets the dataframe for the career of the player
def lifespan(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career.get_data_frames()[0]
#gets the total points of the player
def Total_Points(player_id):
    total_points = playercareerstats.PlayerCareerStats(player_id=player_id)
    return sum(total_points.get_data_frames()[0]["PTS"])
#gets the total assists of the player
def Total_Ast(player_id):
    total_ast = playercareerstats.PlayerCareerStats(player_id=player_id)
    return sum(total_ast.get_data_frames()[0]["AST"])
#gets the total rebound of the player
def Total_Reb(player_id):
    total_reb = playercareerstats.PlayerCareerStats(player_id=player_id)
    return sum(total_reb.get_data_frames()[0]["REB"])

#gets the season_id  
def year_to_season(year):
    return f'{year}-{(year % 100)+1}'



