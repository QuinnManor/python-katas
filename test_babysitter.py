from babysitter import calculate_hours
import pytest


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


def test_exception_when_end_time_is_before_start_time():
    with pytest.raises(Exception) as err:
        start_time = 7
        end_time = 5
        calculate_hours(start_time, end_time)
    err.match("Shift can't end before it starts!")
