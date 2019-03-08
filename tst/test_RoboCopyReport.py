from src.RoboCopyReport import *
from os import path
from datetime import datetime as dt


class TestRoboCopyReport:
    def __init__(self):
        pass

    def test_can_parse_report_start_time(self):
        raw_report = open(path.join("_test_files", "no_fault")).read()
        actual = RoboCopyReport(raw_report).get_start_time()
        expected = dt(2019, 3, 8, 0, 5, 0)
        assert actual.ctime() == expected.ctime()
