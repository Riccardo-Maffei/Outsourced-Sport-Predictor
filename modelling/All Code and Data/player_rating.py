import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from utils import DirectoryHandler
from utils.LabelsHandler import *

PLOTTING_ENABLED = False
DECIMAL_PLACES = 5


def plot_data(data_to_plot, data_label):
    plt.hist(data_to_plot)
    plt.title(data_label)
    plt.show()


def calculate_player_ratings(data_frame):
    return (
            + 2 * data_frame[NORMALIZED_GOAL_LABEL]
            + data_frame[NORMALIZED_ASSIST_LABEL]
            + data_frame[NORMALIZED_MINUTES_PLAYED]
            - data_frame[NORMALIZED_YELLOW_CARD]
            - 2 * data_frame[NORMALIZED_RED_CARD]
    )


def normalize_array(normalization_target):
    min_value = normalization_target.min()
    max_value = normalization_target.max()

    return round((normalization_target - min_value) / (max_value - min_value), DECIMAL_PLACES)


def calculate_column_average_and_normalize(column_name):
    average_column = AVERAGE_LABEL_BUILDING_BLOCK + column_name
    normalized_column = NORMALIZED_LABEL_BUILDING_BLOCK + column_name

    temp_data[average_column] = round(data[column_name] / data[GAME_COUNT_LABEL], DECIMAL_PLACES)

    # Normalize the average play time per game to the range [0, 1]
    final_data[normalized_column] = normalize_array(temp_data[average_column])


# Create a connection to the existing SQLite database
conn = sqlite3.connect(DirectoryHandler.PATH_TO_DB)

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
temp_data = pd.DataFrame()

final_data = pd.DataFrame()
final_data[PLAYER_ID_LABEL] = data[PLAYER_ID_LABEL]

# Close the database connection
conn.close()

columns_list = RELEVANT_QUERY_LABELS

for column in columns_list:
    calculate_column_average_and_normalize(column)

    if PLOTTING_ENABLED:
        column_label = NORMALIZED_LABEL_BUILDING_BLOCK + column
        plot_data(temp_data[column_label], column_label)

# Rating
data[RATING_LABEL] = calculate_player_ratings(final_data)

# Normalized rating
final_data[NORMALIZED_RATING_LABEL] = normalize_array(data[RATING_LABEL])


# Save the DataFrame to CSV with all floating-point numbers formatted to 4 decimal places
float_format = '%.4f'
final_data.to_csv(DirectoryHandler.PATH_TO_PLAYER_RATING, index=False, float_format=float_format)
