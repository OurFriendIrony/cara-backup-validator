#!/usr/bin/python

import re
import datetime


class RoboCopyReport(object):
    def __init__(self, raw_report):
        self.raw_report
        self._parse_raw_report(raw_report)

    def _parse_raw_report(self, raw_report):
        self.datetime_start = datetime.now()

    def get_start_time(self):
        return self.datetime_start
