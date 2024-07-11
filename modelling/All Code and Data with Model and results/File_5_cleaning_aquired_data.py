import pandas as pd

df = pd.read_csv("C:\\Users\\conno\\OneDrive\\Desktop\\Swiss Stuff\\Swiss Project\\data_for_model.csv")

player_counts = df.groupby('game_id')['player_id'].count().reset_index()

player_counts.columns = ['game_id', 'num_players']

under_36 = player_counts[player_counts['num_players'] < 36]

filtered_df = df[~df['game_id'].isin(under_36['game_id'])]

output_file_path = "C:\\Users\\conno\\OneDrive\\Desktop\\Swiss Stuff\\Swiss Project\\data_for_model.csv"
filtered_df.to_csv(output_file_path, index=False)