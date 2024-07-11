import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Create a connection to the existing SQLite database
conn = sqlite3.connect('C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\transfermarket.db')
cursor = conn.cursor()

# SQL query to join the tables and get the required data
query = '''
SELECT
    player_id,
    COUNT(player_id) as game_count,
    SUM(yellow_cards) as yellow_card,
    SUM(red_cards) as red_card,
    SUM(goals) as goal,
    SUM(assists) as assist,
    SUM(minutes_played) as minutes_played
FROM
    appearances
GROUP BY
    player_id
'''

# Load the data into a DataFrame
data = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

def avreger(name):
    avname = "ave_"+name

    data[avname] = round(data[name] / data['game_count'], 4)

    # Normalize the average play time per game to the range [0, 1]
    min_value = data[avname].min()
    max_value = data[avname].max()

    nro_name = "normalized_" +name
    data[nro_name] = (data[avname] - min_value) / (max_value - min_value)
    data.drop(columns=[avname, name], inplace=True)


collist = ["yellow_card", "red_card", "goal", "assist", "minutes_played"]

for col in collist:
    avreger(col)
    datname = "normalized_"+col
    #plt.hist(data[datname])
    #plt.title(datname)
    #plt.show() 

data.drop(columns=["game_count"], inplace=True)

# Rating
data["rating"] = - data["normalized_yellow_card"] - 2 * data["normalized_red_card"] + 2 * data["normalized_goal"] + data["normalized_assist"] + data["normalized_minutes_played"]

plt.hist(data['rating'])
plt.show() 

data.drop(columns=["normalized_yellow_card","normalized_red_card", "normalized_goal", "normalized_assist", "normalized_minutes_played"], inplace=True)

output_file = "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\player_rating.csv"

data.to_csv(output_file, index=False)

