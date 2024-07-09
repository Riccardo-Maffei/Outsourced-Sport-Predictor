import sqlite3
import pandas as pd

from utils import DirectoryHandler
from utils.DirectoryHandler import calculate_path
from utils.DataFramesHandler import *


BASE_PATH = DirectoryHandler.BASE_PATH
DATA_BASE_SUBFOLDER = DirectoryHandler.DATA_FRAMES_SUBFOLDER

DATA_FRAME_PATHS = DirectoryHandler.DATA_FRAME_PATHS

# Create a dictionary to hold the DataFrames
data_frames = {}

# Load the CSV files (9)
for name, path in zip(DATA_FRAME_NAMES, DATA_FRAME_PATHS):
    data_frames[name] = pd.read_csv(calculate_path(BASE_PATH + DATA_BASE_SUBFOLDER, path))

clubs_df = data_frames[CLUBS_DF]
games_df = data_frames[GAMES_DF]
players_df = data_frames[PLAYERS_DF]
club_games_df = data_frames[CLUB_GAMES_DF]
appearances_df = data_frames[APPEARANCES_DF]
game_events_df = data_frames[GAME_EVENTS_DF]
competitions_df = data_frames[COMPETITIONS_DF]
game_lineups_df = data_frames[GAME_LINEUPS_DF]
player_valuations_df = data_frames[PLAYER_VALUATIONS_DF]

# Create a connection to the existing SQLite database
conn = sqlite3.connect(DirectoryHandler.PATH_TO_DB)
cursor = conn.cursor()

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
    date DATE,
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
    date DATE,
    competition_id TEXT,
    season TEXT,
    round TEXT,
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
    date DATE,
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
    date_of_birth DATE,
    current_club_id INTEGER,
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
    contract_expiration_date DATE,
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
    date DATE,
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
    date DATE,
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


def insert_data_in_tables(data_frame, sql_name):
    data_frame.to_sql(sql_name, conn, if_exists='replace', index=False)


# Insert data into the new tables
insert_data_in_tables(games_df, GAMES_DF)
insert_data_in_tables(clubs_df, CLUBS_DF)
insert_data_in_tables(players_df, PLAYERS_DF)
insert_data_in_tables(club_games_df, CLUB_GAMES_DF)
insert_data_in_tables(appearances_df, APPEARANCES_DF)
insert_data_in_tables(game_events_df, GAME_EVENTS_DF)
insert_data_in_tables(competitions_df, COMPETITIONS_DF)
insert_data_in_tables(game_lineups_df, GAME_LINEUPS_DF)
insert_data_in_tables(player_valuations_df, PLAYER_VALUATIONS_DF)

# Commit the changes and close the connection
conn.commit()
conn.close()
