import pandas as pd
import sqlite3


# Connect to the SQLite database
DB_PATH = "../Data/Data_Bank/transfermarket.db"


def execute_SQLite_query(query_string):
    conn = sqlite3.connect(DB_PATH)

    data = pd.read_sql_query(query_string, conn)
    conn.close()

    return data


def execute_SQLite_query_and_return_tuple(query_string, tuple_name):
    data = execute_SQLite_query(query_string)

    return tuple(data[tuple_name].tolist())


def get_referees():
    query = '''
    SELECT DISTINCT 
    referee
    FROM
    games
    '''

    return execute_SQLite_query_and_return_tuple(query, 'referee')


def get_stadiums():
    query = '''
    SELECT DISTINCT 
    stadium
    FROM
    games
    '''

    return execute_SQLite_query_and_return_tuple(query, 'stadium')


def get_competition_types():
    query = '''
    SELECT DISTINCT 
    competition_type
    FROM
    games
    '''

    return execute_SQLite_query_and_return_tuple(query, 'competition_type')


def get_clubs_as_tuple():
    query = '''
    SELECT
    name
    FROM
    clubs
    '''

    return execute_SQLite_query_and_return_tuple(query, 'name')


def get_players():
    query = '''
    SELECT
    player_id,
    name,
    rating
    FROM
    players
    '''

    data = execute_SQLite_query(query)

    data_structure = {
        player_id: {'name': name, 'rating': rating}
        for player_id, name, rating in zip(data['player_id'], data['name'], data['rating'])
    }

    return data_structure


def retrieve_player_data(player_id):
    query = '''
    SELECT 
    
    FROM players
    '''
