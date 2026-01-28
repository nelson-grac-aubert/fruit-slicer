import json 
import os
from game_classes import GameState
from game_assets import resource_path

def get_scores() : 
    """ Get scores from scores.json """

    # Use path function
    path = resource_path('scores.json')

    # Read the scores and return them as a list of dictionnaries
    if os.path.exists(path) :                       # If file exists
        with open(path, 'r', encoding='utf-8') as f:
            try : 
                scores = json.load(f)
            except json.JSONDecodeError :           # Error management
                scores = []
            
    else : 
        scores = []

    return scores


def get_best_scores() :
    """ Get 10 highest scores for display in leaderboard """

    scores = get_scores()
    return scores[:10]


def save_score(game_state, player_name) : 
    """ Save score at the end of the game"""

    path = resource_path('scores.json')     # Use path function
    scores = get_scores()                   # Get scores if they exist

    # Add current entry to scores
    scores.append({"player" : player_name , "score" : game_state.score}) 

    # Sort scores from highest to lowest before writing them in json
    scores.sort(key=lambda x: x["score"], reverse=True)

    # Dump updated scores into scores.json
    with open(path, 'w', encoding="utf-8") as f : 
        json.dump(scores, f, ensure_ascii=False, indent=4)  # Dont convert special characters into unicode

    return scores