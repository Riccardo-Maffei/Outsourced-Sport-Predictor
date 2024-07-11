import pandas as pd

# Load the score data
dfscor = pd.read_csv("C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_modv4.csv")

dfscor.drop(columns=['home_home_club_id_1', 'away_home_club_id_1', 'home_away_club_id_1', 'away_away_club_id_1'], inplace=True)

# Assuming df is your DataFrame
# List of the columns in the original DataFrame
columns = ['home_type_1', 'away_type_1', 'home_position_1', 'away_position_1', 'home_position.1_1',
           'away_position.1_1', 'home_sub_position_1', 'away_sub_position_1', 'home_foot_1', 'away_foot_1',
           'home_height_in_cm_1', 'away_height_in_cm_1', 'home_rating_1', 'away_rating_1', 'home_age_1',
           'away_age_1', 'home_type_2', 'away_type_2', 'home_position_2', 'away_position_2', 'home_position.1_2',
           'away_position.1_2', 'home_sub_position_2', 'away_sub_position_2', 'home_foot_2', 'away_foot_2',
           'home_height_in_cm_2', 'away_height_in_cm_2', 'home_rating_2', 'away_rating_2', 'home_age_2',
           'away_age_2', 'home_type_3', 'away_type_3', 'home_position_3', 'away_position_3', 'home_position.1_3',
           'away_position.1_3', 'home_sub_position_3', 'away_sub_position_3', 'home_foot_3', 'away_foot_3',
           'home_height_in_cm_3', 'away_height_in_cm_3', 'home_rating_3', 'away_rating_3', 'home_age_3',
           'away_age_3', 'home_type_4', 'away_type_4', 'home_position_4', 'away_position_4', 'home_position.1_4',
           'away_position.1_4', 'home_sub_position_4', 'away_sub_position_4', 'home_foot_4', 'away_foot_4',
           'home_height_in_cm_4', 'away_height_in_cm_4', 'home_rating_4', 'away_rating_4', 'home_age_4',
           'away_age_4', 'home_type_5', 'away_type_5', 'home_position_5', 'away_position_5', 'home_position.1_5',
           'away_position.1_5', 'home_sub_position_5', 'away_sub_position_5', 'home_foot_5', 'away_foot_5',
           'home_height_in_cm_5', 'away_height_in_cm_5', 'home_rating_5', 'away_rating_5', 'home_age_5',
           'away_age_5', 'home_type_6', 'away_type_6', 'home_position_6', 'away_position_6', 'home_position.1_6',
           'away_position.1_6', 'home_sub_position_6', 'away_sub_position_6', 'home_foot_6', 'away_foot_6',
           'home_height_in_cm_6', 'away_height_in_cm_6', 'home_rating_6', 'away_rating_6', 'home_age_6',
           'away_age_6', 'home_type_7', 'away_type_7', 'home_position_7', 'away_position_7', 'home_position.1_7',
           'away_position.1_7', 'home_sub_position_7', 'away_sub_position_7', 'home_foot_7', 'away_foot_7',
           'home_height_in_cm_7', 'away_height_in_cm_7', 'home_rating_7', 'away_rating_7', 'home_age_7',
           'away_age_7', 'home_type_8', 'away_type_8', 'home_position_8', 'away_position_8', 'home_position.1_8',
           'away_position.1_8', 'home_sub_position_8', 'away_sub_position_8', 'home_foot_8', 'away_foot_8',
           'home_height_in_cm_8', 'away_height_in_cm_8', 'home_rating_8', 'away_rating_8', 'home_age_8',
           'away_age_8', 'home_type_9', 'away_type_9', 'home_position_9', 'away_position_9', 'home_position.1_9',
           'away_position.1_9', 'home_sub_position_9', 'away_sub_position_9', 'home_foot_9', 'away_foot_9',
           'home_height_in_cm_9', 'away_height_in_cm_9', 'home_rating_9', 'away_rating_9', 'home_age_9',
           'away_age_9', 'home_type_10', 'away_type_10', 'home_position_10', 'away_position_10', 'home_position.1_10',
           'away_position.1_10', 'home_sub_position_10', 'away_sub_position_10', 'home_foot_10', 'away_foot_10',
           'home_height_in_cm_10', 'away_height_in_cm_10', 'home_rating_10', 'away_rating_10', 'home_age_10',
           'away_age_10', 'home_type_11', 'away_type_11', 'home_position_11', 'away_position_11', 'home_position.1_11',
           'away_position.1_11', 'home_sub_position_11', 'away_sub_position_11', 'home_foot_11', 'away_foot_11',
           'home_height_in_cm_11', 'away_height_in_cm_11', 'home_rating_11', 'away_rating_11', 'home_age_11',
           'away_age_11', 'home_type_12', 'away_type_12', 'home_position_12', 'away_position_12', 'home_position.1_12',
           'away_position.1_12', 'home_sub_position_12', 'away_sub_position_12', 'home_foot_12', 'away_foot_12',
           'home_height_in_cm_12', 'away_height_in_cm_12', 'home_rating_12', 'away_rating_12', 'home_age_12',
           'away_age_12', 'home_type_13', 'away_type_13', 'home_position_13', 'away_position_13', 'home_position.1_13',
           'away_position.1_13', 'home_sub_position_13', 'away_sub_position_13', 'home_foot_13', 'away_foot_13',
           'home_height_in_cm_13', 'away_height_in_cm_13', 'home_rating_13', 'away_rating_13', 'home_age_13',
           'away_age_13', 'home_type_14', 'away_type_14', 'home_position_14', 'away_position_14', 'home_position.1_14',
           'away_position.1_14', 'home_sub_position_14', 'away_sub_position_14', 'home_foot_14', 'away_foot_14',
           'home_height_in_cm_14', 'away_height_in_cm_14', 'home_rating_14', 'away_rating_14', 'home_age_14',
           'away_age_14', 'home_type_15', 'away_type_15', 'home_position_15', 'away_position_15', 'home_position.1_15',
           'away_position.1_15', 'home_sub_position_15', 'away_sub_position_15', 'home_foot_15', 'away_foot_15',
           'home_height_in_cm_15', 'away_height_in_cm_15', 'home_rating_15', 'away_rating_15', 'home_age_15',
           'away_age_15', 'home_type_16', 'away_type_16', 'home_position_16', 'away_position_16', 'home_position.1_16',
           'away_position.1_16', 'home_sub_position_16', 'away_sub_position_16', 'home_foot_16', 'away_foot_16',
           'home_height_in_cm_16', 'away_height_in_cm_16', 'home_rating_16', 'away_rating_16', 'home_age_16',
           'away_age_16', 'home_type_17', 'away_type_17', 'home_position_17', 'away_position_17', 'home_position.1_17',
           'away_position.1_17', 'home_sub_position_17', 'away_sub_position_17', 'home_foot_17', 'away_foot_17',
           'home_height_in_cm_17', 'away_height_in_cm_17', 'home_rating_17', 'away_rating_17', 'home_age_17',
           'away_age_17', 'home_type_18', 'away_type_18', 'home_position_18', 'away_position_18', 'home_position.1_18',
           'away_position.1_18', 'home_sub_position_18', 'away_sub_position_18', 'home_foot_18', 'away_foot_18',
           'home_height_in_cm_18', 'away_height_in_cm_18', 'home_rating_18', 'away_rating_18', 'home_age_18',
           'away_age_18']

# Manually setting the reordered columns
ordered_columns = [
    'home_club_goals', 'away_club_goals', 
    'referee', 'stadium', 'competition_type', 'attendance'
]

home_columns = sorted([col for col in columns if col.startswith('home_')], key=lambda x: int(x.split('_')[-1]))
away_columns = sorted([col for col in columns if col.startswith('away_')], key=lambda x: int(x.split('_')[-1]))

ordered_columns.extend(home_columns)
ordered_columns.extend(away_columns)

# Reordering the DataFrame columns
df = dfscor[ordered_columns]

# Save the merged dataset to a CSV file
output_file_path = "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\data_modv5.csv"
df.to_csv(output_file_path, index=False)

# Print the columns of the merged DataFrame
print(df.columns.to_list())
print(df.head())