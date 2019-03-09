import re
from datetime import datetime as dt

fmt_datetime = '%a %b %d %H:%M:%S %Y'


def _regex_it(string, regex):
    return re.search(regex, string) \
        .group(1) \
        .lstrip().rstrip()


def _regex_it_datetime(raw_report, regex):
    start_str = _regex_it(raw_report, regex)
    return dt.strptime(start_str, fmt_datetime)


class RoboCopyReport(object):
    def __init__(self, raw_report):
        self.datetime_start = _regex_it_datetime(raw_report, r'.*Started : (.*)')
        self.datetime_end = _regex_it_datetime(raw_report, r'.*Ended : (.*)')

    def get_start_time(self):
        return self.datetime_start

    def get_end_time(self):
        return self.datetime_end
