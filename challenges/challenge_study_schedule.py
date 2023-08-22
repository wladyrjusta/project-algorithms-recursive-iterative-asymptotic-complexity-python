def study_schedule(permanence_period, target_time):
    counter: int = 0
    if (
        target_time is None or target_time == 0
        or not isinstance(permanence_period, list)
    ):
        return None
    for period in permanence_period:
        if (
            not isinstance(period, tuple)
            or len(period) != 2
            or type(period[0]) is not int or type(period[1]) is not int
        ):
            return None
        if target_time in range(period[0], period[1] + 1):
            counter += 1
    return counter

    # raise NotImplementedError
