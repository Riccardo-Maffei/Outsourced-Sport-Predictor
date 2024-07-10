import pandas as pd
import sqlite3


# Connect to the SQLite database
DB_PATH = "../data_open/transfermarket.db"


def get_clubs_as_tuple():
    conn = sqlite3.connect(DB_PATH)

    team_query = '''
    SELECT
    name
    FROM
    clubs
    '''

    data = pd.read_sql_query(team_query, conn)

    conn.close()

    return tuple(data['name'].tolist())


def get_players():
    conn = sqlite3.connect(DB_PATH)

    team_query = '''
    SELECT
    player_id,
    name,
    rating
    FROM
    players
    '''

    data = pd.read_sql_query(team_query, conn)

    conn.close()

    data_structure = {
        player_id: {'name': name, 'rating': rating}
        for player_id, name, rating in zip(data['player_id'], data['name'], data['rating'])
    }

    return data_structure
