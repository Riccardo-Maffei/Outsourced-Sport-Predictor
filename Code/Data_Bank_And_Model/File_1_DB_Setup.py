import pandas as pd
import sqlite3

# Load the CSV files (9)
clubs_df = pd.read_csv('../../../Data/Data_Bank_And_Model/Transfermarket/clubs.csv')
competitions_df = pd.read_csv('../../../Data/Data_Bank_And_Model/Transfermarket/competitions.csv')
club_games_df = pd.read_csv('../../../Data/Data_Bank_And_Model/Transfermarket/club_games.csv')
game_events_df = pd.read_csv('../../../Data/Data_Bank_And_Model/Transfermarket/game_events.csv')
games_df = pd.read_csv('../../../Data/Data_Bank_And_Model/Transfermarket/games.csv')
player_valuations_df = pd.read_csv('../../../Data/Data_Bank_And_Model/Transfermarket/player_valuations.csv')
players_df = pd.read_csv('../../../Data/Data_Bank_And_Model/Transfermarket/players.csv')
appearances_df = pd.read_csv('../../../Data/Data_Bank_And_Model/Transfermarket/appearances.csv')
game_lineups_df = pd.read_csv('../../../Data/Data_Bank_And_Model/Transfermarket/game_lineups.csv')

# Create a connection to the existing SQLite database
conn = sqlite3.connect('../../../Data/Data_Bank_And_Model/transfermarket.db')
cursor = conn.cursor()

# Create the new tables with appropriate schema and relationships

# Create the club_games table
cursor.execute('''
CREATE TABLE IF NOT EXISTS club_games (
    game_id INTEGER,
    club_id INTEGER,
    own_goals INTEGER,
    own_position REAL,
    own_manager_name TEXT,
    opponent_id INTEGER,
    opponent_goals INTEGER,
    opponent_position REAL,
    opponent_manager_name TEXT,
    hosting TEXT,
    is_win INTEGER,
    PRIMARY KEY (game_id, club_id),
    FOREIGN KEY (club_id) REFERENCES clubs (club_id),
    FOREIGN KEY (opponent_id) REFERENCES clubs (club_id)
)
''')

# Create the game_events table
cursor.execute('''
CREATE TABLE IF NOT EXISTS game_events (
    game_event_id TEXT PRIMARY KEY,
    date TEXT,
    game_id INTEGER,
    minute INTEGER,
    type TEXT,
    club_id INTEGER,
    player_id INTEGER,
    description TEXT,
    player_in_id INTEGER,
    player_assist_id INTEGER,
    FOREIGN KEY (game_id) REFERENCES games (game_id),
    FOREIGN KEY (club_id) REFERENCES clubs (club_id),
    FOREIGN KEY (player_id) REFERENCES players (player_id),
    FOREIGN KEY (player_in_id) REFERENCES players (player_id),
    FOREIGN KEY (player_assist_id) REFERENCES players (player_id)
)
''')

# Create the games table
cursor.execute('''
CREATE TABLE IF NOT EXISTS games (
    game_id INTEGER PRIMARY KEY,
    date TEXT,
    time TEXT,
    competition_id TEXT,
    season TEXT,
    round TEXT,
    venue TEXT,
    attendance INTEGER,
    referee TEXT,
    home_club_id INTEGER,
    away_club_id INTEGER,
    home_club_goals INTEGER,
    away_club_goals INTEGER,
    home_club_position INTEGER,
    away_club_position INTEGER,
    home_club_manager_name TEXT,
    away_club_manager_name TEXT,
    stadium TEXT,
    url TEXT,
    home_club_formation TEXT,
    away_club_formation TEXT,
    home_club_name TEXT,
    away_club_name TEXT,
    aggregate TEXT,
    competition_type TEXT,
    FOREIGN KEY (competition_id) REFERENCES competitions (competition_id),
    FOREIGN KEY (home_club_id) REFERENCES clubs (club_id),
    FOREIGN KEY (away_club_id) REFERENCES clubs (club_id)
)
''')

# Create the player_valuations table
cursor.execute('''
CREATE TABLE IF NOT EXISTS player_valuations (
    player_id INTEGER,
    date TEXT,
    market_value_in_eur REAL,
    current_club_id INTEGER,
    player_club_domestic_competition_id TEXT,
    PRIMARY KEY (player_id, date),
    FOREIGN KEY (player_id) REFERENCES players (player_id),
    FOREIGN KEY (current_club_id) REFERENCES clubs (club_id),
    FOREIGN KEY (player_club_domestic_competition_id) REFERENCES competitions (competition_id)
)
''')

# Create the players table
cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY,
    player_code TEXT,
    name TEXT,
    position TEXT,
    date_of_birth TEXT,
    height REAL,
    weight REAL,
    nationality TEXT,
    current_club_id INTEGER,
    joined_date TEXT,
    contract_until TEXT,
    agent_name TEXT,
    image_url TEXT,
    url TEXT,
    current_club_domestic_competition_id TEXT,
    current_club_name TEXT,
    market_value_in_eur REAL,
    highest_market_value_in_eur REAL,
    first_name TEXT,
    last_name TEXT,
    last_season INTEGER,
    country_of_birth TEXT,
    city_of_birth TEXT,
    country_of_citizenship TEXT,
    sub_position TEXT,
    foot TEXT,
    height_in_cm INTEGER,
    contract_expiration_date TEXT,
    FOREIGN KEY (current_club_id) REFERENCES clubs (club_id),
    FOREIGN KEY (current_club_domestic_competition_id) REFERENCES competitions (competition_id)
)
''')

# Create the appearances table
cursor.execute('''
CREATE TABLE IF NOT EXISTS appearances (
    appearance_id TEXT PRIMARY KEY,
    player_id INTEGER,
    game_id INTEGER,
    player_club_id INTEGER,
    player_current_club_id INTEGER,
    date TEXT,
    player_name TEXT,
    competition_id TEXT,
    yellow_cards INTEGER,
    red_cards INTEGER, 
    goals INTEGER,
    assists INTEGER,
    minutes_played INTEGER,
    FOREIGN KEY (player_id) REFERENCES players (player_id),
    FOREIGN KEY (game_id) REFERENCES games (game_id),
    FOREIGN KEY (player_club_id) REFERENCES clubs (club_id),
    FOREIGN KEY (player_current_club_id) REFERENCES clubs (club_id),
    FOREIGN KEY (competition_id) REFERENCES competitions (competition_id)
)
''')

# Create the game_lineups table
cursor.execute('''
CREATE TABLE IF NOT EXISTS game_lineups (
    game_lineups_id TEXT PRIMARY KEY,
    date TEXT,
    game_id INTEGER,
    club_id INTEGER,
    player_id INTEGER,
    player_name TEXT,
    position TEXT,
    type TEXT,
    number INTEGER,
    team_captain INTEGER,
    FOREIGN KEY (game_id) REFERENCES games (game_id),
    FOREIGN KEY (club_id) REFERENCES clubs (club_id),
    FOREIGN KEY (player_id) REFERENCES players (player_id)
)
''')

# Create the competitions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS competitions (
    competition_id TEXT PRIMARY KEY,
    competition_code TEXT, 
    name TEXT, 
    sub_type TEXT, 
    type TEXT, 
    country_id INTEGER, 
    country_name TEXT, 
    domestic_league_code TEXT, 
    confederation TEXT, 
    url TEXT, 
    is_major_national_league TEXT
)
''')

# Create the clubs table
cursor.execute('''
CREATE TABLE IF NOT EXISTS clubs (
    club_id INTEGER PRIMARY KEY,
    club_code TEXT, 
    name TEXT, 
    domestic_competition_id TEXT, 
    total_market_value INTEGER, 
    squad_size INTEGER, 
    average_age REAL, 
    foreigners_number INTEGER, 
    foreigners_percentage REAL, 
    national_team_players INTEGER, 
    stadium_name TEXT, 
    stadium_seats INTEGER, 
    net_transfer_record TEXT, 
    coach_name TEXT, 
    last_season INTEGER, 
    filename TEXT, 
    url TEXT,
    FOREIGN KEY (domestic_competition_id) REFERENCES competitions (competition_id)
)
''')

# Insert data into the new tables
club_games_df.to_sql('club_games', conn, if_exists='append', index=False)
game_events_df.to_sql('game_events', conn, if_exists='append', index=False)
games_df.to_sql('games', conn, if_exists='append', index=False)
player_valuations_df.to_sql('player_valuations', conn, if_exists='append', index=False)
players_df.to_sql('players', conn, if_exists='append', index=False)
appearances_df.to_sql('appearances', conn, if_exists='append', index=False)
game_lineups_df.to_sql('game_lineups', conn, if_exists='append', index=False)
clubs_df.to_sql('clubs', conn, if_exists='append', index=False)
competitions_df.to_sql('competitions', conn, if_exists='append', index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()
