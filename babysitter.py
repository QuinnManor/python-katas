def calculate_hours(start_time, end_time):
    if start_time < 5:
        start_time = 5
    return end_time - start_time
