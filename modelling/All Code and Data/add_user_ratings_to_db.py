import pandas as pd
import sqlite3
from utils import DirectoryHandler

# Load the CSV file
file_path = DirectoryHandler.PATH_TO_PLAYER_RATING
player_ratings = pd.read_csv(file_path)

# Connect to the SQLite database
db_path = DirectoryHandler.PATH_TO_DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Check if the 'players' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='players';")
    table_exists = cursor.fetchone()

    if not table_exists:
        raise Exception("The 'players' table does not exist in the database.")

    # Check if the 'rating' column exists, and add it if it doesn't
    cursor.execute("PRAGMA table_info(players);")
    columns = [col[1] for col in cursor.fetchall()]

    if 'rating' not in columns:
        cursor.execute("ALTER TABLE players ADD COLUMN rating REAL;")
        conn.commit()

    # Update the players table with the ratings from the CSV file
    for index, row in player_ratings.iterrows():
        cursor.execute("UPDATE players SET rating = ? WHERE player_id = ?;", (row['normalized_rating'], row['player_id']))
    
    conn.commit()

    # Verify the updates
    cursor.execute("SELECT player_id, rating FROM players WHERE rating IS NOT NULL LIMIT 10;")
    updated_rows = cursor.fetchall()
    print("Updated rows:", updated_rows)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the connection
    conn.close()
