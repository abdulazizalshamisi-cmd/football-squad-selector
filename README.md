# ⚽ Football Squad Selector

A Flask web app that builds your ideal football starting XI. Pick a national team, club, or filter mode, choose a formation, and the app automatically selects the best-rated players for each position based on player power ratings.

## Features

- **5 formations**: 4-2-2, 4-5-1, 4-3-3, 3-4-3, 5-4-1
- **Team filtering**: choose from national teams (Brazil, Argentina, Portugal, Germany, England) or top clubs (Real Madrid, FC Barcelona, Manchester United, Milan, FC Bayern München)
- **Automatic best-XI selection**: players are ranked by power rating and slotted into GK / DEF / MID / FWD based on the selected formation
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
│   └── index.html        # Main page template
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

## Roadmap

- 🔍 Search player by name + manually add to formation
- 📋 Detailed position display (17 granular positions instead of 4 groups)
- 🤖 ML-based squad recommendations (KMeans clustering)
- 🎥 Computer vision analysis on match video

## Status

**v1.0** — Live and functional. Actively being extended as part of an ongoing Python/AI learning roadmap.