import random

import tensorflow as tf
import streamlit as st
import DB_Calls

import Hard_Coded_Parameters


def pack_in_object():
    return referee, stadium, competition_type, attendance, players[0], players[1]


EMPTY_FIELD = "Type here..."
MODEL_PATH = "../models/test_model.keras"

PLAYER_COUNT = 18

TEST_TEAM_LIST = ("Team_A", "Team_B", "Team_C", "Team_D", "Team_E")
TEST_PLAYERS = {
    1: {'name': 'Loreum Ipsum', 'rating': 5},
    2: {'name': 'Ipsum Loreum', 'rating': 4},
    3: {'name': 'Asdf Jklö', 'rating': 3},
    4: {'name': 'Qwert Zuiop', 'rating': 2},
    5: {'name': 'Yxcv Bnm', 'rating': 1}
}

TEAM_LIST = DB_Calls.get_clubs_as_tuple()
PLAYERS = DB_Calls.get_players()


def predict_match_dummy(team1, team2):
    # Replace this with your actual model's prediction logic
    # For now, it's a dummy prediction

    score_team_1 = random.randint(0, 3)
    score_team_2 = random.randint(0, 3)

    return f"{team1} vs {team2}: {score_team_1} - {score_team_2}"


def predict_match():
    model = tf.keras.models.load_model(MODEL_PATH)

    parameters = Hard_Coded_Parameters.get_very_painful_parameters()

    """
    MODEL PARAMETERS:
    referee,
    stadium,
    competition_type,
    attendance,

    18 times:
    home_type_1,
    home_position_1,
    home_position.1_1,
    home_sub_position_1,
    home_foot_1,
    home_height_in_cm_1,
    home_rating_1,
    home_age_1,

    18 times:
    away_type_1,
    away_position_1,
    away_position.1_1,
    away_sub_position_1,
    away_foot_1,
    away_height_in_cm_1,
    away_rating_1,
    away_age_1,

    MODEL RESULTS:
    home_club_goals, away_club_goals
    """

    score_home, score_away = model.Predict(parameters)

    return str(score_home) + ' - ' + str(score_away)


def predict_result(team1, team2):
    if (team1 and team2) and (team1 != EMPTY_FIELD and team2 != EMPTY_FIELD):
        result = predict_match_dummy(team1, team2)
    else:
        result = "Please enter both team names."
    return result


def generate_tuple_list(other_input, possible_inputs):
    input_list = list(possible_inputs)
    if other_input in input_list:
        input_list.remove(other_input)
    input_list.insert(0, None)
    return tuple(input_list)


def find_player_object_with_key(key):
    return PLAYERS.get(key)


def find_key_with_player_name(value):
    for key, player in PLAYERS.items():
        if player['name'] == value:
            return key
    return None


def synchronize_data(team_number, player_number, source):
    player_id_key = 'player_id_team' + str(team_number) + '_player' + str(player_number)
    player_name_key = 'player_name_team' + str(team_number) + '_player' + str(player_number)
    player_rating_key = 'player_rating_team' + str(team_number) + '_player' + str(player_number)

    print(st.session_state)

    if source == 'id':
        player_id = st.session_state[player_id_key]
        player_object = find_player_object_with_key(player_id)
        if player_object:
            st.session_state[player_name_key] = player_object['name']
            st.session_state[player_rating_key] = player_object['rating']
    elif source == 'name':
        selected_name = st.session_state[player_name_key]
        player_id = find_key_with_player_name(selected_name)
        if player_id:
            st.session_state[player_id_key] = player_id
            player_object = find_player_object_with_key(player_id)
            if player_object:
                st.session_state[player_rating_key] = player_object['rating']


def generate_player_input_field(team_number, player_number):
    player_id_col, player_name_col, player_rating_col = st.columns(3)

    with player_id_col:
        player_id = st.selectbox(
            "Player ID",
            PLAYERS.keys(),
            key='player_id_team' + str(team_number) + '_player' + str(player_number),
            on_change=synchronize_data,
            args=(team_number, player_number, 'id')
        )

    with player_name_col:
        player_name = st.selectbox(
            "Player Name",
            [player['name'] for player in PLAYERS.values()],
            key='player_name_team' + str(team_number) + '_player' + str(player_number),
            on_change=synchronize_data,
            args=(team_number, player_number, 'name')
        )

    with player_rating_col:
        player_rating_key = 'player_rating_team' + str(team_number) + '_player' + str(player_number)
        if player_rating_key in st.session_state:
            st.write(f"Player Rating: {st.session_state[player_rating_key]}")
        else:
            st.write("Player Rating: -")

    if player_id is not None:
        return player_id
    elif player_name is not None:
        return find_key_with_player_name(player_name)
    else:
        return 0


# Title of the app
st.title('Sports Predictor 3000')

referee = st.selectbox("Select referee", DB_Calls.get_referees(), key='referee')

stadium = st.selectbox("Select stadium", DB_Calls.get_stadiums(), key='stadium')

competition_type = st.selectbox("Select competition type", DB_Calls.get_competition_types(), key='competition_type')

attendance = st.number_input("Select attendance")

# Select Team 1
team_1_input = st.selectbox("Select first Team", TEAM_LIST, key="team_1")

players = [[0 for _ in range(PLAYER_COUNT)] for _ in range(2)]

with st.expander("Select players for first Team", expanded=False):
    team_index = 0

    for player_index in range(PLAYER_COUNT):
        players[team_index][player_index] = generate_player_input_field(team_index, player_index)

# Select Team 2
team_2_input = st.selectbox("Select second Team",
                            generate_tuple_list(team_1_input, TEAM_LIST),
                            key="team_2")

with st.expander("Select players for second Team", expanded=False):
    team_index = 1

    for player_index in range(11):
        players[team_index][player_index] = generate_player_input_field(2, player_index)

# Display the match result
st.write(f'Match result: {predict_result(team_1_input, team_2_input)}')
