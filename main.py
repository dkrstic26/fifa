tournament = {
    "player" : {
        "marko" : {
            "games_played",
            "wins",
            "draws",
            "losses",
            "goals_for",
            "goals_against",
            "goal_difference",
            "points"
        },
        "dusan" : {
            "games_played",
            "wins",
            "draws",
            "losses",
            "goals_for",
            "goals_against",
            "goal_difference",
            "points"
        },
        "dimi": {
            "games_played",
            "wins",
            "draws",
            "losses",
            "goals_for",
            "goals_against",
            "goal_difference",
            "points"
        }
    }
}

while True:
    home_name = input("Enter the home player name")
    if home_name not in tournament["player"]:
        print("Invalid input!")
        continue
    home_player = tournament["player"][home_name]

    away_name = input("Enter the away player name")
    if away_name not in tournament["player"]:
        print("Invalid input!")
        continue
    away_player = tournament["player"][away_name]

    home_goals = int(input("Enter home goals: "))
    away_goals = int(input("Enter away goals: "))

    tournament["player"][home_player]["goals_for"] += home_goals
    tournament["player"][away_player]["goals_for"] += away_goals
    tournament["player"][home_player]["goals_against"] += away_goals
    tournament["player"][away_player]["goals_against"] += home_goals

    if home_goals > away_goals:
        tournament["player"][home_player]["points"] += 3
        tournament["player"][home_player]["wins"] += 1
        tournament["player"][away_player]["losses"] += 1
    elif away_goals > home_goals:
        tournament["player"][away_player]["points"] += 3
        tournament["player"][away_player]["wins"] += 1
        tournament["player"][home_player]["losses"] += 1
    else:
        tournament["player"][home_player]["points"] += 1
        tournament["player"][home_player]["draws"] += 1
        tournament["player"][away_player]["points"] += 1
        tournament["player"][away_player]["draws"] += 1

    
    break