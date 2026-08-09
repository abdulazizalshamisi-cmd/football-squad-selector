# ⚽ Football Squad Selector

A Flask web app that builds your ideal football starting XI. Pick a national team, club, or filter mode, choose a formation, and the app automatically selects the best-rated players for each position based on player power ratings.

## Features

- **5 formations**: 4-2-2, 4-5-1, 4-3-3, 3-4-3, 5-4-1
- **Team filtering**: choose from national teams (Brazil, Argentina, Portugal, Germany, England) or top clubs (Real Madrid, FC Barcelona, Manchester United, Milan, FC Bayern München)
- **Automatic best-XI selection**: players are ranked by power rating and slotted into GK / DEF / MID / FWD based on the selected formation
- **Player search**: search any player by name (case-insensitive, partial match) and add them to your personal squad
- **Per-user sessions**: added players are stored per browser session (via Flask `session`), so different users don't share the same picks
- **Large real-world dataset**: powered by a FIFA player dataset (`players_real.json`, ~19,600+ players)

## Tech Stack

- Python 3
- Flask
- Jinja2 (HTML templates)

## Project Structure

```
football/
├── app.py                # Main Flask application
├── players_real.json     # Player dataset (name, position, team, country, power, etc.)
├── templates/
│   ├── index.html        # Main page template
│   └── search.html       # Player search results page
└── README.md
```

## Setup & Run

1. Clone the repository
   ```
   git clone https://github.com/abdulazizalshamisi-cmd/football-squad-selector.git
   cd football-squad-selector
   ```
2. Install Flask
   ```
   pip install flask
   ```
3. Run the app
   ```
   python app.py
   ```
4. Open your browser at `http://127.0.0.1:5000`

## How It Works

- Select a team type (club, national, or all players)
- Select a specific team/country
- Select a formation
- The app filters players belonging to that team, then picks the top-rated player per required position slot (based on the `power` field), rendering a full starting XI
- Alternatively, search for any player by name using the search box; matching results appear with an "Add" button that saves the player to your session-based squad list, shown on the home page under "My Added Players"

## Roadmap

- 📋 Detailed position display (17 granular positions instead of 4 groups)
- ❌ Remove player from added squad
- 🎯 Place manually-added players into actual formation slots (not just a list)
- 🤖 ML-based squad recommendations (KMeans clustering)
- 🎥 Computer vision analysis on match video

## Status

**v1.1** — Live and functional. Added player search + session-based squad building on top of v1.0. Actively being extended as part of an ongoing Python/AI learning roadmap.