import unpacker


def get_very_painful_parameters():
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

    referee = "Andre Marriner"
    stadium = "St Mary's Stadium"
    competition_type = "domestic_league"
    attendance = "30510.0"
    pain_parameters = unpacker.get_pain_parameters()

    # Create a list and append the variables
    result_list = [referee, stadium, competition_type, attendance]
    result_list.extend(pain_parameters)

    # If needed, convert the list to a tuple
    result_tuple = tuple(result_list)

    return result_tuple
