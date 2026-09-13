import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("Fifa.csv")

print(df.head())
print(df.describe())
print(df.dtypes)
print(df["Team"].unique())
print(df["Country"].unique())
national_teams = ["Brazil", "Argentina", "Portugal", "Germany", "England"]
clubs = ["Real Madrid", "FC Barcelona", "Manchester United", "Milan", "FC Bayern München"]

for team in national_teams:
    print(team, team in df["Country"].values)

for club in clubs:
    print(club, club in df["Team"].values)
print(df.columns)
print(df.shape)
print(df["Position"].unique())


plt.scatter(df["Age"], df["Overall_Rating"])
plt.xlabel("Age")
plt.ylabel("Overall Rating")
plt.title("Age vs Overall Rating")
plt.show()

plt.hist(df["Age"], bins=10)
plt.xlabel("Age")
plt.ylabel("Number of players")
plt.title("Age Distribution")
plt.show()
df["category"]=df["Position"].map({"GK":"GK", "CB":"DEF", "RB":"DEF", "LB":"DEF", "RWB":"DEF", "LWB":"DEF", "SW":"DEF", "CDM":"MID", "CM":"MID", "CAM":"MID", "LM":"MID", "RM":"MID", "RW":"FWD", "LW":"FWD", "ST":"FWD", "CF":"FWD", "RF":"FWD"})
df = df[["Name", "Position", "category", "Overall_Rating", "Team", "Country"]]
df = df.rename(columns={"Name": "name", "Position": "position", "Overall_Rating": "power"})
df["goals"] = 0
df["assists"] = 0

print(df.head())

df.to_json("players_real.json", orient="records")

