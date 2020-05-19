from babysitter import calculate_hours


def test_calculate_hours():
    start_time = 5
    end_time = 6
    assert calculate_hours(start_time, end_time) == 1


def test_earliest_start_time():
    start_time = 4
    end_time = 6
    assert calculate_hours(start_time, end_time) == 1


def test_latest_end_time():
    start_time = 3
    end_time = 5
    time_of_day = 'AM'
    assert calculate_hours(start_time, end_time, time_of_day) == 1


def test_pm_am_hours():
    start_time = 11
    end_time = 1
    time_of_day = 'PM/AM'
    assert calculate_hours(start_time, end_time, time_of_day) == 2
