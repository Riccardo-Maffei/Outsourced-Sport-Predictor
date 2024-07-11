import pandas as pd

df = pd.read_csv("C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_for_model.csv")

score_game_df = df.drop(columns=["player_id","type","position","club_id","position.1","sub_position","foot","height_in_cm","age"])

player_df = df.drop(columns=["referee","stadium","competition_type","attendance","home_club_goals","away_club_goals"])

teams = player_df.groupby(['club_id', 'game_id'])

# Create a DataFrame to hold the size of each group
group_sizes = teams.size().reset_index(name='count')

# Filter out groups with less than 18 players
valid_teams = group_sizes[group_sizes['count'] >= 18]

# Identify invalid game_ids (games with at least one group having less than 18 players)
invalid_game_ids = group_sizes[group_sizes['count'] < 18]['game_id'].unique()

# Filter out games with invalid game_ids from the original DataFrame
valid_games_df = player_df[~player_df['game_id'].isin(invalid_game_ids)]

# Group by 'club_id' and 'game_id'
teams2 = valid_games_df.groupby(['club_id', 'game_id'])

# Create an empty list to hold the new rows
rows = []

# Iterate over each group
for (club_id, game_id), group in teams2:
    # Sort the group by 'rating'
    sorted_group = group.sort_values(by='rating', ascending=False).head(18)
    
    # Flatten the group into a single row
    flattened_row = {
        'club_id': club_id,
        'game_id': game_id
    }
    for i, (_, player) in enumerate(sorted_group.iterrows(), 1):
        for col in valid_games_df.columns:
            if col not in ['club_id', 'game_id']:
                flattened_row[f'{col}_{i}'] = player[col]
    
    # Append the flattened row to the list
    rows.append(flattened_row)

# Create a new DataFrame from the list of rows
flattened_df = pd.DataFrame(rows)

output_file_path = "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_modv1.csv"
flattened_df.to_csv(output_file_path, index=False)


columns = flattened_df.columns.to_list()

# Columns to retain
columns_to_keep = [col for col in columns if not col.startswith(('home_club_id', 'away_club_id', 'player_id')) or col.endswith('_1')]

# Dropping the unwanted columns
flattened_df_r = flattened_df[columns_to_keep]
flattened_df_r.drop(columns=['player_id_1'], inplace=True)

output_file_path = "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_modv2.csv"
flattened_df_r.to_csv(output_file_path, index=False)

# Displaying the reduced DataFrame
#print(flattened_df_r)
#print(flattened_df_r.columns.to_list())

games = flattened_df_r.groupby(['game_id'])

# Initialize a list to collect the transformed rows
rows2 = []

# Process each game group
for (game_id), game in games:
    # Identify home and away rows
    home_row = game[game['club_id'] == game['home_club_id_1']].iloc[0]
    away_row = game[game['club_id'] == game['away_club_id_1']].iloc[0]
    
    # Flatten the group into a single row
    flattened_row2 = {
        'game_id': game_id
    }
    for col in flattened_df_r.columns:
        if col not in ['club_id', 'game_id']:
            flattened_row2[f'home_{col}'] = home_row[col]
            flattened_row2[f'away_{col}'] = away_row[col]
    
    # Append the combined row to the list
    rows2.append(flattened_row2)

# Create a new DataFrame from the combined rows
new_df = pd.DataFrame(rows2)

output_file_path = "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_modv3.csv"
new_df.to_csv(output_file_path, index=False)

# Display the new DataFrame
print(new_df.head())
print(new_df.columns.to_list())