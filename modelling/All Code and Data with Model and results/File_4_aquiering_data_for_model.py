import pandas as pd
import sqlite3

# Load the CSV file
file_path = "C:\\Users\\conno\\OneDrive\\Desktop\\Swiss Stuff\\Swiss Project\\archive\\player_rating.csv"  
player_ratings = pd.read_csv(file_path)

# Connect to the SQLite database
db_path = "C:\\Users\\conno\\OneDrive\\Desktop\\Swiss Stuff\\Swiss Project\\transfermarket.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = '''
SELECT 
    g.date, 
    g.referee,
    g.stadium, 
    g.competition_type, 
    g.attendance, 
    g.game_id,
    g.home_club_id,
    g.away_club_id,
    g.home_club_goals,
    g.away_club_goals,
    gl.player_id,
    gl.type,
    gl.position,
    gl.club_id,
    p.position,
    p.date_of_birth,
    p.sub_position,
    p.foot,
    p.height_in_cm,
    p.current_club_id
FROM 
    games g
JOIN
    game_lineups gl
ON 
    g.game_id = gl.game_id
JOIN
    players p
ON
    gl.player_id = p.player_id   
'''

data = pd.read_sql_query(query, conn)

output_file = "C:\\Users\\conno\\OneDrive\\Desktop\\Swiss Stuff\\Swiss Project\\data_for_model.csv"

data.to_csv(output_file, index=False)

# Close the connection
conn.close()
