from babysitter import *


def test_calculate_hours():
    start_time = 5
    end_time = 6
    assert calculate_hours(start_time, end_time) == 1
