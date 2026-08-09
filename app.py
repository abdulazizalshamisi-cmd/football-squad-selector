from flask import Flask, render_template, request, jsonify, session, redirect
import json

app = Flask(__name__)
app.secret_key = "any_random_string_here"

formations = {
    "422": {"DEF": 4, "MID": 4, "FWD": 2},
    "451": {"DEF": 4, "MID": 5, "FWD": 1},
    "433": {"DEF": 4, "MID": 3, "FWD": 3},
    "343": {"DEF": 3, "MID": 4, "FWD": 3},
    "541": {"DEF": 5, "MID": 4, "FWD": 1},
}

national_teams = ["Brazil", "Argentina", "Portugal", "Germany", "England"]
clubs = ["Real Madrid", "FC Barcelona", "Manchester United", "Milan", "FC Bayern München"]

def filter_by_team(players, selected_type, selected_name):
    if selected_type == "club":
        return [p for p in players if p["Team"] == selected_name]
    elif selected_type == "national":
        return [p for p in players if p["Country"] == selected_name]
    elif selected_type == "fm":
        return players
    else:
        return []
    

    

def best_player(players, category, count):
    group = [p for p in players if p["category"] == category]
    sorted_group = sorted(group, key=lambda x: x["power"], reverse=True)
    return sorted_group[:count]

def search_players(players, query):
    results = [p for p in players if query.lower() in p["name"].lower()]
    return results




fm =[]
@app.route("/search")
def search():
    with open("players_real.json", "r") as f:
        players = json.load(f)
    query = request.args.get("q", "")
    results = search_players(players, query)
    return render_template("search.html", results=results, query=query)

@app.route("/add")
def add_player():
    name = request.args.get("name", "")
    
    if "selected_players" not in session:
        session["selected_players"] = []
    
    if name not in session["selected_players"]:
        session["selected_players"].append(name)
        session.modified = True
    
    return redirect("/")

@app.route("/")
def home():
    with open("players_real.json", "r") as f:
        players = json.load(f)

    selected_type = request.args.get("type", "none")
    selected_name = request.args.get("name", "none")
    selected_formation = request.args.get("formation", "422")

    setup = formations[selected_formation]

    if selected_type == "none":
        team_players = []
    else:
        team_players = filter_by_team(players, selected_type, selected_name)

    GK = best_player(team_players, "GK", 1)
    DEF = best_player(team_players, "DEF", setup["DEF"])
    MID = best_player(team_players, "MID", setup["MID"])
    FWD = best_player(team_players, "FWD", setup["FWD"])

    added_players = session.get("selected_players", [])

    return render_template("index.html", GK=GK, DEF=DEF, MID=MID, FWD=FWD,
                            formations=formations, selected_formation=selected_formation,
                            national_teams=national_teams, clubs=clubs,
                            selected_type=selected_type, selected_name=selected_name,
                            added_players=added_players)

if __name__ == "__main__":
    app.run(debug=True)