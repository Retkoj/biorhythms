from datetime import datetime


def calculate_three_cycles(days_since_birth: int):
    """
    Calculate the position in the three cycles based on the days since birth:

    - physical has a cycle of 23 days
    - emotional has a cycle of 28 days
    - mental has a cycle of 33 days

    :param days_since_birth:
    :return: positions for the three cycles
    """
    physical_current_pos = days_since_birth % 23
    emotional_current_pos = days_since_birth % 28
    mental_current_pos = days_since_birth % 33
    return physical_current_pos, emotional_current_pos, mental_current_pos


def calculate_biorhythm_position(birth_date: datetime, other_date: datetime):
    """
    Calculates the time delta of birth_date and other_date and feeds that to the calculation for the three
    cycles.
    Prints out the timedelta and positions based on time delta

    :param birth_date: Date of birth
    :param other_date: Date to check cycles for
    :return physical_current_pos, emotional_current_pos, mental_current_pos
    """
    time_delta_days = (other_date - birth_date).days

    # TODO: calculate for timeframe to get direction of cycle
    return calculate_three_cycles(time_delta_days)
