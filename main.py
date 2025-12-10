tournament = {
    "Dusan" : {
        "wins" : 0,
        "losses" : 0,
        "draws" : 0,
        "points" : 0
    },
    "Marko" : {
        "wins" : 0,
        "losses" : 0,
        "draws" : 0,
        "points" : 0
    },
    "Dimi" : {
        "wins" : 0,
        "losses" : 0,
        "draws" : 0,
        "points" : 0
    }
}

def score_tracker(data, home, away, home_score, away_score):
    if home_score > away_score:
        data[home]["wins"] += 1
        data[away]["losses"] += 1
        data[home]["points"] += 3
    elif away_score > home_score:
        data[away]["wins"] += 1
        data[home]["losses"] += 1
        data[away]["points"] += 3
    else:
        data[away]["draws"] += 1
        data[home]["draws"] += 1
        data[away]["points"] += 1
        data[home]["points"] += 1

while True:
    cmd = input("Add a match (add) or finish tournament input (done)? \n")

    if cmd == "done":
        break

    else:
        valid_players = ("Dusan", "Marko", "Dimi")
        hometeam = input("Enter the home team's name: ")
        awayteam = input("Enter the away team's name: ")

        if hometeam not in valid_players or awayteam not in valid_players:
            print("Not a valid player!")
            continue

        #Scores

        try:
            homescore = int(input("Enter the home score: "))
            awayscore = int(input("Enter the away score: "))
        except ValueError:
            print("Scores must be whole numbers!")
            continue

        # Validating scores
        
        if homescore < 0 or awayscore < 0:
            print("Not a valid score!")
            continue
    


        score_tracker(tournament, hometeam, awayteam, homescore, awayscore)



print("Dimi's points: ", tournament["Dimi"]["points"])
print("Dusan's points: ", tournament["Dusan"]["points"])
print("Marko's points: ", tournament["Marko"]["points"])
