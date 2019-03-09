from src.RoboCopyReport import *
from os import path
from datetime import datetime as dt

dir_path = path.dirname(path.realpath(__file__))


class TestRoboCopyReport:
    def test_can_parse_report_start_time(self):
        raw_report = open(path.join(dir_path, "_test_files", "no_fault")).read()
        actual = RoboCopyReport(raw_report).get_start_time()
        expected = dt(2019, 3, 8, 0, 5, 0)
        assert actual.ctime() == expected.ctime()

    def test_can_parse_report_end_time(self):
        raw_report = open(path.join(dir_path, "_test_files", "no_fault")).read()
        actual = RoboCopyReport(raw_report).get_end_time()
        expected = dt(2019, 3, 8, 0, 5, 1)
        assert actual.ctime() == expected.ctime()
