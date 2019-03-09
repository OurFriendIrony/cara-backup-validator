import re
from datetime import datetime as dt

R_STARTED = r'.*Started : (.*)'
R_ENDED = r'.*Ended : (.*)'
R_DIRS = r'Dirs : \s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)'
R_FILES = r'Files : \s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)'

FMT_DT = '%a %b %d %H:%M:%S %Y'


def _regex_it(string, regex, group=1):
    print regex
    print string
    return re.search(regex, string) \
        .group(group) \
        .lstrip().rstrip()


def _regex_it_datetime(raw_report, regex):
    start_str = _regex_it(raw_report, regex)
    return dt.strptime(start_str, FMT_DT)


class RoboCopyReport(object):
    def __init__(self, raw_report):
        self.datetime_start = _regex_it_datetime(raw_report, R_STARTED)
        self.datetime_end = _regex_it_datetime(raw_report, R_ENDED)
        self.failed_dirs = int(_regex_it(raw_report, R_DIRS, group=5))
        self.failed_files = int(_regex_it(raw_report, R_FILES, group=5))

    def get_start_time(self):
        return self.datetime_start

    def get_end_time(self):
        return self.datetime_end

    def get_failed_dirs(self):
        return self.failed_dirs

    def get_failed_files(self):
        return self.failed_files
