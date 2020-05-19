def calculate_hours(start_time, end_time, time_of_day='PM'):
    start_time = _check_earliest_start_time(start_time, time_of_day)
    end_time = _check_latest_end_time(end_time, time_of_day)
    return end_time - start_time


def _check_earliest_start_time(start_time, time_of_day):
    if start_time not in range(5, 13) and time_of_day == 'PM':
        start_time = 5

    if start_time in range(5, 13) and time_of_day == 'PM/AM':
        start_time += 12
    return start_time


def _check_latest_end_time(end_time, time_of_day):
    if end_time not in range(0, 4) and time_of_day == 'AM':
        end_time = 4

    if end_time in range(0, 4) and time_of_day == 'PM/AM':
            end_time += 24
    return end_time