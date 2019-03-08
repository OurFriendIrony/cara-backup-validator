import re
from datetime import datetime as dt

fmt_datetime = '%a %b %d %H:%M:%S %Y'

r_started = r'.*Started : (.*)'


def _regex_it(string, regex):
    return re.search(regex, string) \
        .group(1) \
        .lstrip().rstrip()


class RoboCopyReport(object):
    def __init__(self, raw_report):
        self.raw_report = raw_report
        self._parse_raw_report(raw_report)

    def _parse_raw_report(self, raw_report):
        start_str = _regex_it(raw_report, r_started)
        self.datetime_start = dt.strptime(start_str, fmt_datetime)

    def get_start_time(self):
        return self.datetime_start
