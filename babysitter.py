EARLIEST_START_TIME = 5
LATEST_END_TIME = 4
MIDNIGHT = 12
MILITARY_MIDNIGHT = 0


def calculate_hours(start_time, end_time, time_of_day='PM'):
    start_time = _check_start_time(start_time, time_of_day)
    end_time = _check_end_time(end_time, time_of_day)
    _end_time_before_start_time_exception(end_time, start_time)
    return end_time - start_time


def _check_start_time(start_time, time_of_day):
    if _is_before_earliest_start_time(start_time, time_of_day):
        start_time = EARLIEST_START_TIME
    return start_time


def _is_before_earliest_start_time(start_time, time_of_day):
    return start_time not in range(EARLIEST_START_TIME, MIDNIGHT + 1) and time_of_day == 'PM'


def _check_end_time(end_time, time_of_day):
    if _is_past_latest_end_time(end_time, time_of_day):
        end_time = LATEST_END_TIME

    if _is_overnight(end_time, time_of_day):
        end_time += MIDNIGHT
    return end_time


def _is_past_latest_end_time(end_time, time_of_day):
    return end_time not in range(MILITARY_MIDNIGHT, LATEST_END_TIME) and time_of_day == 'AM'


def _is_overnight(end_time, time_of_day):
    return end_time in range(MILITARY_MIDNIGHT, LATEST_END_TIME) and time_of_day == 'PM/AM'


def _end_time_before_start_time_exception(end_time, start_time):
    if start_time > end_time:
        raise Exception("Shift can't end before it starts!")
