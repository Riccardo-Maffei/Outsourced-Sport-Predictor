BASE_PATH = '../../data_open/'

DATA_FRAMES_SUBFOLDER = 'Transfermarket/'

DATA_FRAME_PATHS = ['clubs.csv', 'club_games.csv', 'competitions.csv', 'games.csv', 'game_events.csv',
                    'game_lineups.csv', 'players.csv', 'appearances.csv', 'player_valuations.csv']

DATA_BASE_NAME = 'transfermarket.db'
PLAYER_RATING_NAME = 'player_rating.csv'


def calculate_path(parent_folder, file_name):
    return parent_folder + file_name


PATH_TO_DB = calculate_path(BASE_PATH, DATA_BASE_NAME)
PATH_TO_PLAYER_RATING = calculate_path(BASE_PATH, PLAYER_RATING_NAME)
