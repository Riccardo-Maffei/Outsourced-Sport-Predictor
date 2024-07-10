import streamlit as st

EMPTY_FIELD = "Type here..."
TEAM_LIST = ("Team_1", "Team_2", "Team_3", "Team_4", "Team_5")


def predict_match(team1, team2):
    # Replace this with your actual model's prediction logic
    # For now, it's a dummy prediction
    return f"{team1} vs {team2}: 1-0"


def predict_result(team1, team2):
    if (team1 and team2) and (team1 != EMPTY_FIELD and team2 != EMPTY_FIELD):
        result = predict_match(team1, team2)
    else:
        result = "Please enter both team names."
    return result


def generate_tuple_list(this_input, other_input, possible_inputs):
    print("Generating tuple list for " + str(this_input))
    print("Other input: " + str(other_input))
    print("Possible inputs: " + str(possible_inputs))

    input_list = list(possible_inputs)

    if other_input in input_list:
        input_list.remove(other_input)

    input_list.insert(0, None)

    print("Output: " + str(input_list))
    print()

    return tuple(input_list)


# Title of the app
st.title('Sports Predictor 3000')

# Initialize session state for team selections
if 'team_1_input' not in st.session_state:
    st.session_state.team_1_input = None
if 'team_2_input' not in st.session_state:
    st.session_state.team_2_input = None



# Select Team 1
st.write("Select Team 1")
team_1_input = st.selectbox("Select first Team",
                            generate_tuple_list("Team 1", st.session_state.team_2_input, TEAM_LIST),
                            key="team_1")

# Update session state if selection changes

# Select Team 2
st.write("Select Team 2")

team_2_input = st.selectbox("Select second Team",
                            generate_tuple_list("Team 2", st.session_state.team_1_input, TEAM_LIST),
                            key="team_2")

# Display the match result
st.write(f'Match result: {predict_result(st.session_state.team_1_input, st.session_state.team_2_input)}')


# Refresh info
update_required = False

if st.session_state.team_1_input != team_1_input:
    st.session_state.team_1_input = team_1_input
    update_required = True
if st.session_state.team_2_input != team_2_input:
    st.session_state.team_2_input = team_2_input
    update_required = True
if update_required:
    st.rerun()
