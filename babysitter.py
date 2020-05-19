def calculate_hours(start_time, end_time, time_of_day='PM'):
    if start_time < 5 and time_of_day == 'PM':
        start_time = 5

    if end_time > 4 and time_of_day == 'AM':
        end_time = 4

    return end_time - start_time
