import argparse
import sys
import pandas as pd

from util import lifespan
from util import Total_Points
from util import Total_Ast
from util import Total_Reb
from util import year_to_season



import pprint

from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

from shotchart import get_player_shotchartdetail
from shotchart import plot



#arguments users can input
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', nargs='*', help="name of the player")
    parser.add_argument('-y','--year',type=int,help="year for the statistics")
      
    args = parser.parse_args()


    name = args.name
    year = args.year
    

    #Finds matching players
    if name is not None:
        full_name = " ".join(name)

        matching_players = players.find_players_by_full_name(full_name)
        active_list = [x for x in matching_players if x['is_active']]
        if len(active_list) > 1:
            more_doods = [x['full_name'] for x in active_list ]
            print('Here is what we found')
            print(more_doods)
            sys.exit('Please be more specific')
        if len(active_list) == 0:
            sys.exit('We could not find such player. Try again')
        dood= active_list[0]
        dood_full_name = dood['full_name']
        dood_id = dood['id']
        dood_stats = lifespan(dood_id)
        #prints player career dataframe
        pprint.pprint(dood_stats)
        
        #prints the player's total stats
        print(full_name,"has",Total_Points(dood_id),"points.")
        print(full_name,"has",Total_Ast(dood_id),"assists.")
        print(full_name,"has",Total_Reb(dood_id),"rebounds.")
        
        #takes the year and turns to season_id
        season = year_to_season(year)  
        get_player_shotchartdetail(dood_full_name,season)
        
        #plots the shot chart of player given the season
        plot(dood_full_name,season)

        
