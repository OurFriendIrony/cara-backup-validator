import sys
from os import path
from datetime import datetime as dt

DATE_FMT = "%d/%m/%y"

DEFAULT_PATH = path.dirname(path.realpath(__file__))
DEFAULT_DATE = dt.now().strftime(DATE_FMT)


def input_date():
    is_valid = False
    while not is_valid:
        in_date = raw_input("Enter Date [%s]: " % DEFAULT_DATE) or DEFAULT_DATE
        try:
            d = dt.strptime(in_date, DATE_FMT)
            is_valid = True
        except ValueError:
            print "** Incorrect Date Format **\n"
    return d


def input_path():
    is_valid = False
    while not is_valid:
        in_path = raw_input("Enter Path [%s]: " % DEFAULT_PATH) or DEFAULT_PATH
        if path.isdir(in_path):
            is_valid = True
        else:
            print "** Invalid Path **\n"
    return in_path


try:
    report_date = input_date()
    report_path = input_path()


except KeyboardInterrupt:
    print "\n** Aborted **"
    sys.exit(0)
