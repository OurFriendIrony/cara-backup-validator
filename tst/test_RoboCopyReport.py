from src.RoboCopyReport import *
from os import path
from datetime import datetime as dt

dir_path = path.dirname(path.realpath(__file__))


def _get_test_file(file_name):
    return open(path.join(dir_path, "_test_files", file_name)).read()


class TestRoboCopyReport:
    def test_can_parse_report_start_time(self):
        raw_report = _get_test_file("failed_false")

        actual = RoboCopyReport(raw_report).get_start_time()
        expected = dt(2019, 3, 8, 0, 5, 0)

        assert actual.ctime() == expected.ctime()

    def test_can_parse_report_end_time(self):
        raw_report = _get_test_file("failed_false")

        actual = RoboCopyReport(raw_report).get_end_time()
        expected = dt(2019, 3, 8, 0, 5, 1)

        assert actual.ctime() == expected.ctime()

    def test_can_get_failed_dirs(self):
        raw_report = _get_test_file("failed_true")

        actual = RoboCopyReport(raw_report).get_failed_dirs()
        expected = 2

        assert actual == expected

    def test_can_get_failed_files(self):
        raw_report = _get_test_file("failed_true")

        actual = RoboCopyReport(raw_report).get_failed_files()
        expected = 5

        assert actual == expected

    def test_can_get_failed_true(self):
        raw_report = _get_test_file("failed_true")

        actual = RoboCopyReport(raw_report)

        assert actual.has_failed() == True

    def test_can_get_failed_false(self):
        raw_report = _get_test_file("failed_false")

        actual = RoboCopyReport(raw_report)

        assert actual.has_failed() == False
