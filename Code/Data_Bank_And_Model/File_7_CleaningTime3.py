import pandas as pd

# Load the score data
dfscor = pd.read_csv("C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_for_model.csv")

# Drop unnecessary columns
score_game_df = dfscor.drop(columns=["player_id", "type", "position", "club_id", "position.1", "sub_position", "foot", "height_in_cm", "age", 'home_club_id', 'away_club_id', 'rating'])

# Define aggregation functions for each column
aggregation_functions = {
    'referee': 'first',
    'stadium': 'first',
    'competition_type': 'first',
    'attendance': 'mean',
    'home_club_goals': 'mean',
    'away_club_goals': 'mean'
}

# Group by game_id and aggregate using the defined functions
score_game_grouped_df = score_game_df.groupby('game_id').agg(aggregation_functions).reset_index()

# Load the player data
dfplay = pd.read_csv("C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_modv3.csv")

# Ensure game_id is a string in dfplay
dfplay['game_id'] = dfplay['game_id'].astype(str)

# Remove parentheses and comma from game_id in dfplay and convert to integer
dfplay['game_id'] = dfplay['game_id'].str.replace(r'[(),]', '', regex=True).astype(int)

# Merge the datasets on game_id
merged_df = pd.merge(score_game_grouped_df, dfplay, on='game_id')

merged_df.drop(columns=['game_id'], inplace=True)

# Save the merged dataset to a CSV file
output_file_path = "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_modv4.csv"
merged_df.to_csv(output_file_path, index=False)

# Print the columns of the merged DataFrame
print(merged_df.columns.to_list())