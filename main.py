import json
import os

file_path = "tournaments/all_time.json"

if os.path.isfile(file_path):
    with open(file_path, "r") as file:
        tournament = json.load(file)
    
else:
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


num_of_games = int(input("Please enter the total amount of games: "))

for x in range(num_of_games):
    print(f"Matchday {x + 1}")
    home_name = input("Please enter the home player's name: ").strip().lower()
    away_name = input("Please enter the away player's name: ").strip().lower()
    home_player = tournament["player"][home_name]
    away_player = tournament["player"][away_name]
    home_player["games_played"] += 1
    away_player["games_played"] += 1

    print(f"{home_player["name"]} vs {away_player["name"]}")
    home_goals = int(input("Enter home player's goals: "))
    away_goals = int(input("Enter away player's goals: "))
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


standings = dict(sorted(
    tournament["player"].items(),
    key=lambda item: (-item[1]["points"], -(item[1]["goals_for"] - item[1]["goals_against"]), -item[1]["goals_for"])
))

for player_id, stats in standings.items():
    goal_difference = int(stats["goals_for"]) - int(stats["goals_against"])

    print(f"Name: {stats["name"]} | Wins: {stats["wins"]} | Losses: {stats["losses"]} | Draws: {stats["draws"]} | Points: {stats["points"]} | Goals For: {stats["goals_for"]} | Goals Against: {stats["goals_against"]} | Goal Difference : {goal_difference}")

with open(file_path, "w") as json_file:
    json.dump(tournament, json_file, indent=4)


