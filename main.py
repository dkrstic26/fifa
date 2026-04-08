import json
import os
from datetime import datetime
from pathlib import Path

def open_file(path):
    with open(path, "r") as file:
        tournament = json.load(file)

    return tournament

def create_players():
    while True:
        try:
            n_of_players = int(input("How many players are playing this tournament?\n"))
            if n_of_players < 0:
                print("Number of players cannot be negative, please enter a valid number.")
                continue
            elif n_of_players == 0:
                print("Number of players cannot be zero, please enter a valid number")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a valid amount of players.")

    player_names = []

    for i in range(n_of_players):
        while True:
            player_name = input(f"Please enter the name for player {i + 1}: ").strip().lower()
            if not player_name:
                print("The name cannot be empty, please enter a valid player name.")
                continue
            break
        player_names.append(player_name)

    return player_names


def new_tournament(player_names):
    names = player_names

    default_stats = {"games_played" : 0, "wins" : 0, "draws" : 0, "losses" : 0, "goals_for" : 0, "goals_against" : 0}

    tournament = {
        "player" : {name: default_stats.copy() for name in names},
        "matches" : []
    }

    return tournament
    

def player_input(tournament):
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

    return home_name, away_name

def score_input(home_name, away_name):

    print(f"{home_name} vs {away_name}")
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

    return home_goals, away_goals

def add_match(tournament, home_player, away_player, home_goals, away_goals):
    new_match = {
        "home_player": home_player,
        "away_player": away_player,
        "home_goals": home_goals,
        "away_goals": away_goals
    }

    tournament["matches"].append(new_match)

def apply_match_result(tournament, home_name, away_name, home_goals, away_goals):
    if home_name not in tournament["player"]:
        tournament["player"][home_name] = {"games_played" : 0, "wins" : 0, "draws" : 0, "losses" : 0, "goals_for" : 0, "goals_against" : 0}
    
    if away_name not in tournament["player"]:
        tournament["player"][away_name] = {"games_played" : 0, "wins" : 0, "draws" : 0, "losses" : 0, "goals_for" : 0, "goals_against" : 0}

    home_player = tournament["player"][home_name]
    away_player = tournament["player"][away_name]

    home_player["games_played"] += 1
    away_player["games_played"] += 1
    home_player["goals_for"] += home_goals
    home_player["goals_against"] += away_goals
    away_player["goals_for"] += away_goals
    away_player["goals_against"] += home_goals

    if home_goals > away_goals:
        home_player["wins"] += 1
        away_player["losses"] += 1

    elif away_goals > home_goals:
        away_player["wins"] += 1
        home_player["losses"] += 1

    else:
        home_player["draws"] += 1
        away_player["draws"] += 1

def get_points(player):
    return (player["wins"] * 3) + player["draws"]


def calculate_standings(tournament):
    standings = sorted(
    tournament["player"].items(),
    key=lambda item: (-(get_points(item[1])), -(item[1]["goals_for"] - item[1]["goals_against"]), -item[1]["goals_for"])
)
    
    return standings

def print_matches(tournament):
    for i, match in enumerate(tournament["matches"], start=1):
        home = match["home_player"]
        away = match["away_player"]
        h_goals = match["home_goals"]
        a_goals = match["away_goals"]

        print(f"Matchday {i}: {home} {h_goals} - {a_goals} {away}")

    print("-" * 30)

def print_standings(standings):
    for player_name, stats in standings:
        goal_difference = int(stats["goals_for"]) - int(stats["goals_against"])
        points = get_points(stats)
        print(f"{player_name.title()} | Games Played: {stats['games_played']} | Wins: {stats['wins']} | Draws: {stats['draws']} | Losses: {stats['losses']} | Goals For: {stats['goals_for']} | Goals Against: {stats['goals_against']} | Goal Difference : {goal_difference} | Points: {points}")

def date_input():
    folder = Path("tournaments")
    folder.mkdir(exist_ok=True)

    while True:
        date_text = input("Please enter the tournament date(MM-DD-YYYY): ")
        try:
            datetime.strptime(date_text, '%m-%d-%Y')
            file_path = folder/f"{date_text}.json"

            if file_path.exists():
                print("This tournament date already exists, please enter a new one!")
            else:
                return date_text
                
        except ValueError:
                print("Invalid input, please enter the date of the tournament in the correct format.")

def number_of_games(player_names):
    players = len(player_names)
    while True:
        try:
            head_to_head = int(input("How many head to head matchups betewen each of the players are there?"))
            if head_to_head <= 0:
                print("Invalid number of games, please enter 1 or more for head to head games.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a valid amount of games.")

    return (players * (players - 1) // 2) * head_to_head


current_date = date_input()
player_names = create_players()
current_tournament = new_tournament(player_names)
current_file_path = f"tournaments/{current_date}.json"

if os.path.isdir("tournaments"):
    cummulative_file_path = "tournaments/all_time.json"
else:
    os.mkdir("tournaments")
    cummulative_file_path = "tournaments/all_time.json"
    

if os.path.isfile(cummulative_file_path) and os.path.getsize(cummulative_file_path) > 0:
    all_time_tournament = open_file(cummulative_file_path)
else:
    all_time_tournament = new_tournament()
        
num_of_games = number_of_games(player_names)


for x in range(num_of_games):
    print(f"Matchday {x + 1}")
    home_name, away_name = player_input(current_tournament)
    home_goals, away_goals = score_input(home_name, away_name)
    add_match(current_tournament, home_name, away_name, home_goals, away_goals)
    apply_match_result(all_time_tournament, home_name, away_name, home_goals, away_goals)
    apply_match_result(current_tournament, home_name, away_name, home_goals, away_goals)

print("\n Tournament Standings")
current_standings = calculate_standings(current_tournament)
print_standings(current_standings)

print("\n Matches: ")
print_matches(current_tournament)

print("\n All Time Standings")
all_time_standings = calculate_standings(all_time_tournament)
print_standings(all_time_standings)



with open(cummulative_file_path, "w") as json_file:
    json.dump(all_time_tournament, json_file, indent=4)

with open(current_file_path, "w") as json_file:
    json.dump(current_tournament, json_file, indent=4)


