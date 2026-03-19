import json
import os

def open_file(path):
    with open(path, "r") as file:
        tournament = json.load(file)

    return tournament

def new_tournament():
    tournament = {
        "player" : {
            "marko" : {
                "name" : "Marko",
                "games_played" : 0,
                "wins" : 0,
                "draws" : 0,
                "losses" : 0,
                "goals_for" : 0,
                "goals_against" : 0,
                "points" : 0
            },
            "dusan" : {
                "name" : "Dusan",
                "games_played" : 0,
                "wins" : 0,
                "draws" : 0,
                "losses" : 0,
                "goals_for" : 0,
                "goals_against" : 0,
                "points" : 0
            },
            "dimi": {
                "name" : "Dimi",
                "games_played" : 0,
                "wins" : 0,
                "draws" : 0,
                "losses" : 0,
                "goals_for" : 0,
                "goals_against" : 0,
                "points" : 0
            }
        }
    }

    return tournament

def score_input(tournament):
    while True:
        home_name = input("Please enter the home player's name: ").strip().lower()
        if home_name in tournament["player"]:
            break
        print("Invalid input, please enter valid player.")

    while True:
        away_name = input("Please enter the away player's name: ").strip().lower()
        if away_name not in tournament["player"]:
            print("Invalid input, please enter valid player.")
        elif away_name == home_name:
            print("Cannot have a player play themselves, please enter a different player.")
        else:
            break
        
        
    home_player = tournament["player"][home_name]
    away_player = tournament["player"][away_name]
    home_player["games_played"] += 1
    away_player["games_played"] += 1

    print(f"{home_player['name']} vs {away_player['name']}")
    while True:
        try:
            home_goals = int(input("Enter home player's goals: "))
            if home_goals < 0:
                print("Goals scored cannot be a negative number!")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a valid goal amount for the home team.")
    
    while True:
        try:
            away_goals = int(input("Enter away player's goals: "))
            if away_goals < 0:
                print("Away goals cannot be a negative number!")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a valid goal amount for the away team.")

    home_player["goals_for"] += home_goals
    home_player["goals_against"] += away_goals
    away_player["goals_for"] += away_goals
    away_player["goals_against"] += home_goals

    if home_goals > away_goals:
        home_player["points"] += 3
        home_player["wins"] += 1
        away_player["losses"] += 1

    elif away_goals > home_goals:
        away_player["points"] += 3
        away_player["wins"] += 1
        home_player["losses"] += 1

    else:
        home_player["points"] += 1
        away_player["points"] += 1
        home_player["draws"] += 1
        away_player["draws"] += 1

def calculate_standings(tournament):
    standings = dict(sorted(
    tournament["player"].items(),
    key=lambda item: (-item[1]["points"], -(item[1]["goals_for"] - item[1]["goals_against"]), -item[1]["goals_for"])
))
    
    return standings

def print_standings(standings):
    for _, stats in standings.items():
        goal_difference = int(stats["goals_for"]) - int(stats["goals_against"])
        print(f"Name: {stats['name']} | Wins: {stats['wins']} | Losses: {stats['losses']} | Draws: {stats['draws']} | Points: {stats['points']} | Goals For: {stats['goals_for']} | Goals Against: {stats['goals_against']} | Goal Difference : {goal_difference}")

if os.path.isdir("tournaments"):
    file_path = "tournaments/all_time.json"
else:
    os.mkdir("tournaments")
    file_path = "tournaments/all_time.json"
    

if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
    tournament = open_file(file_path)
else:
    tournament = new_tournament()
        
while True:
    try:
        num_of_games = int(input("Please enter the total amount of games: "))
        if num_of_games < 0:
            print("Number of games cannot be a negative number!")
            continue
        break
    except ValueError:
        print("Invalid number of games, please enter a numerical value for the games played.")

for x in range(num_of_games):
    print(f"Matchday {x + 1}")
    score_input(tournament)

standings = calculate_standings(tournament)
print_standings(standings)

with open(file_path, "w") as json_file:
    json.dump(tournament, json_file, indent=4)


