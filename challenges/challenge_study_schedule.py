def study_schedule(permanence_period, target_time):
    counter: int = 0
    if (
        target_time is None or target_time == 0
        or not isinstance(permanence_period, list)
        or any(
            not isinstance(period, tuple)
            or len(period) != 2
            or any(not isinstance(elemento, int) for elemento in period)
            for period in permanence_period
        )
    ):
        return None
    for period in permanence_period:
        if target_time in range(period[0], period[1] + 1):
            counter += 1
    return counter

    # raise NotImplementedError

