import streamlit as st
import pandas as pd

EMPTY_FIELD = "Type here..."
TEAM_LIST = ("Team_1", "Team_2", "Team_3", "Team_4", "Team_5")
PLAYERS_DATA = {
    'Player ID': range(1, 12),
    'First Name': [''] * 11,
    'Family Name': [''] * 11,
    'Player Score': [''] * 11
}


def predict_match(team1, team2):
    # Replace this with your actual model's prediction logic
    # For now, it's a dummy prediction
    return f"{team1} vs {team2}: 1 - 0"


def predict_result(team1, team2):
    if (team1 and team2) and (team1 != EMPTY_FIELD and team2 != EMPTY_FIELD):
        result = predict_match(team1, team2)
    else:
        result = "Please enter both team names."
    return result


def generate_tuple_list(other_input, possible_inputs):
    input_list = list(possible_inputs)

    if other_input in input_list:
        input_list.remove(other_input)

    input_list.insert(0, None)

    return tuple(input_list)


# Title of the app
st.title('Sports Predictor 3000')

# Select Team 1
team_1_input = st.selectbox("Select first Team",
                            TEAM_LIST,
                            key="team_1")

with st.expander("Select players for first Team", expanded=False):
    st.data_editor(pd.DataFrame(PLAYERS_DATA), key='player_list_team_1',
                   use_container_width=True,
                   hide_index=True)


# Select Team 2
team_2_input = st.selectbox("Select second Team",
                            generate_tuple_list(team_1_input, TEAM_LIST),
                            key="team_2")

with st.expander("Select players for second Team", expanded=False):
    st.data_editor(pd.DataFrame(PLAYERS_DATA), key='player_list_team_2',
                   use_container_width=True,
                   hide_index=True)

# Display the match result
st.write(f'Match result: {predict_result(team_1_input, team_2_input)}')
