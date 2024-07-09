import pandas as pd

# List of CSV file paths
csv_files = [
    "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\Transfermarket\\clubs.csv",
    "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\Transfermarket\\competitions.csv",
    "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\Transfermarket\\game_events.csv",
    "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\Transfermarket\\game_lineups.csv",
    "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\Transfermarket\\games.csv",
    "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\Transfermarket\\player_valuations.csv",
    "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\Transfermarket\\players.csv",
    "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\Transfermarket\\appearances.csv",
    "C:\\Users\\pd\\Documents\\ZHAW\\summer_school_data_science\\Project\\data_open\\Transfermarket\\club_games.csv"
]

def display_column_names(file_paths):
    for file_path in file_paths:
        try:
            df = pd.read_csv(file_path)
            print(f"Columns in {file_path}:")
            print(df.columns.tolist())
            print("\n")
            #print(df.head())
            #print("\n")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Call the function with the list of CSV file paths
display_column_names(csv_files)
