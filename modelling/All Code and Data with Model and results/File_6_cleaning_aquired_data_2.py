import pandas as pd

df = pd.read_csv("C:\\Users\\conno\\OneDrive\\Desktop\\Swiss Stuff\\Swiss Project\\data_for_model.csv")

score_game_df = df.drop(columns=["player_id","type","position","club_id","position.1","sub_position","foot","height_in_cm","current_club_id","age"])

player_df = df.drop(columns=["referee","stadium","competition_type","attendance","home_club_goals","away_club_goals"])

teams = player_df.groupby(['club_id', 'game_id'])

for (club_id, game_id), group in teams:
    print(f"Club ID: {club_id}, Game ID: {game_id}")
    print(group)
    print()