# ==========================================
# football.py
# ==========================================

# --- deitl ---
import json

try:
    with open("players.json", "r") as f:
        players = json.load(f)
except FileNotFoundError:
    players = []

# --- function---


def best_player(players,position,power):
    
    gruop = []

    for player in players : 
        if player["position"] == position:
            gruop.append(player)

    sorted_data = sorted(gruop, key=lambda x: x["power"] + x["goals"]*0.5+ x["assists"]*0.3,  reverse=True)
    top_player = sorted_data[:power]

    for pp in top_player : 
        print(f"{pp['name']} - {pp['position']} = score:{pp['power'] + pp['goals']*0.5+ pp['assists']*0.3:.2f}")

print("choose a 1-formation or 2-Add a new player or 3-Delete player: ")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Choose your formation:")
    print("1 - 4-4-2")
    print("2 - 4-3-3")
    print("3 - 3-4-3")
    print("4 - 4-5-1")
    print("5 - 5-3-2")



    choice = int(input("Enter your choice: "))
    if choice == 1:    # 4-4-2
        best_player(players, "GK", 1)
        best_player(players, "DEF", 4)
        best_player(players, "MID", 4)
        best_player(players, "FWD", 2)

    elif choice == 2:    # 4-3-3
        best_player(players, "GK", 1)
        best_player(players, "DEF", 4)
        best_player(players, "MID", 3)
        best_player(players, "FWD", 3)

    elif choice == 3:    # 3-4-3
        best_player(players, "GK", 1)
        best_player(players, "DEF", 3)
        best_player(players, "MID", 4)
        best_player(players, "FWD", 3)

    elif choice == 4:    # 4-5-1
        best_player(players, "GK", 1)
        best_player(players, "DEF", 4)
        best_player(players, "MID", 5)
        best_player(players, "FWD", 1)

    elif choice == 5:    # 5-3-2
        best_player(players, "GK", 1)
        best_player(players, "DEF", 5)
        best_player(players, "MID", 3)
        best_player(players, "FWD", 2)

elif choice == 2:
    name = input("player name:")
    print("1 - GK")
    print("2 - DEF")
    print("3 - MID")
    print("4 - FWD")
    position_choice = int(input("player position:"))
    if position_choice == 1:
        position = "GK"
    elif position_choice == 2:
        position = "DEF"
    elif position_choice == 3:
        position = "MID"
    elif position_choice == 4:
        position = "FWD"
    power = int(input("player power:"))
    
    goals = int(input("player goals:"))
    assists = int(input("player assists:"))
    if power > 99:
        print("error: power cannot exceed 99")
    else:
        new_player = {"name":name, "position":position, "power":power, "goals":goals, "assists":assists}
        players.append(new_player)
        with open("players.json", "w") as f:
            json.dump(players, f)

elif choice == 3:
    for player in players:
        print(player['name'])
    delete_name = input("write the name of the player: ")
    for player in players:
        if player['name'] == delete_name:
            players.remove(player)
            break
    with open("players.json", "w") as f:
        json.dump(players, f)