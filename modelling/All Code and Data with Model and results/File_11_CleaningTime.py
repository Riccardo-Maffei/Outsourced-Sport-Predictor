import pandas as pd

df = pd.read_csv("C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_for_model.csv")

player_counts = df.groupby('game_id')['player_id'].count().reset_index()

player_counts.columns = ['game_id', 'num_players']

under_36 = player_counts[player_counts['num_players'] < 36]

filtered_df = df[~df['game_id'].isin(under_36['game_id'])]

output_file_path = "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_for_model.csv"
filtered_df.to_csv(output_file_path, index=False)