import isholiday
import pytest

def test_xmas_2016():
    holidays = isholiday.getholidays(2016)
    assert(23,12) in holidays

test_xmas_2016()


