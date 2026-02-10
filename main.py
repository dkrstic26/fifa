tournament = {
    "player" : {
        "marko" : {
            "games_played" : 0,
            "wins" : 0,
            "draws" : 0,
            "losses" : 0,
            "goals_for" : 0,
            "goals_against" : 0,
            "goal_difference" : 0,
            "points" : 0
        },
        "dusan" : {
            "games_played" : 0,
            "wins" : 0,
            "draws" : 0,
            "losses" : 0,
            "goals_for" : 0,
            "goals_against" : 0,
            "goal_difference" : 0,
            "points" : 0
        },
        "dimi": {
            "games_played" : 0,
            "wins" : 0,
            "draws" : 0,
            "losses" : 0,
            "goals_for" : 0,
            "goals_against" : 0,
            "goal_difference" : 0,
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

    if home_goals > away_goals:
        home_player["points"] += 3

    