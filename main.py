tournament = {
    "player" : {
        "marko" : {
            "games_played" : 0,
            "wins" : 0,
            "draws" : 0,
            "losses" : 0,
            "goals_for" : 0,
            "goals_against" : 0,
            "points" : 0
        },
        "dusan" : {
            "games_played" : 0,
            "wins" : 0,
            "draws" : 0,
            "losses" : 0,
            "goals_for" : 0,
            "goals_against" : 0,
            "points" : 0
        },
        "dimi": {
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
    home_name = input("Please enter the home player's name: ")
    away_name = input("Please enter the away player's name: ")
    home_player = tournament["player"][home_name]
    away_player = tournament["player"][away_name]
    home_player["games_played"] += 1
    away_player["games_played"] += 1

    print(f"{home_player} vs {away_player}")
    home_goals = int(input("Enter home player's goals"))
    away_goals = int(input("Enter away player's goals"))
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





    