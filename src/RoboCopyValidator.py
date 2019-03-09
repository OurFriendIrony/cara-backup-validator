import sys, os, re, webbrowser, time
from datetime import datetime as dt
from src.RoboCopyReport import *

DATE_FMT = "%d/%m/%y"

# DEFAULT_PATH = os.path.dirname(os.path.realpath(__file__))
DEFAULT_PATH = "/home/steve/git/ourfriendirony/cara-backup-validator/tst/_test_files/GPOROBOFiles"
DEFAULT_DATE = dt.now().strftime(DATE_FMT)

FILES_MATCHING = r'GPOSQL2.*.txt'


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
        if os.path.isdir(in_path):
            is_valid = True
        else:
            print "** Invalid Path **\n"
    return in_path


def write_html_page(path):
    output_file = open(path, 'w')
    output_file.write(html_body)
    output_file.flush()
    output_file.close()


try:
    report_date = input_date()
    report_path = input_path()

    reports = []
    for file_name in os.listdir(report_path):
        file_path = os.path.join(report_path, file_name)
        file_created = dt.fromtimestamp(os.path.getmtime(file_path))

        if re.match(FILES_MATCHING, file_name) and file_created.date() == report_date.date():
            file_body = open(file_path, 'r').read()
            reports.append(
                {'name': file_name, 'report': RoboCopyReport(file_body)}
            )

    html_table = ""
    for report in reports:
        html_table += '<tr><td bgcolor="#FFB3B3">{failed}</td><td><a href="file://{path}">{name}</a></td></tr>'.format(
            failed=report.get('report').has_failed(),
            path=os.path.join(report_path, report.get('name')),
            name=report.get('name')
        )
        # print report.get('name')

    css = "table, th, td {border: 1px solid black;} {margin-left:10%;}"
    html_body = """
    <html><body>
    <style>{style}</style>
    <b>Date:</b> {date}<br/>
    <b>Path:</b> <a href="file://{url}">{url}</a><br/><br/>
    <b>Issues<b>
    <table>
    <tr><th>Issue?</th><th>Filename</th></tr>
    {table}
    </table>
    </body></html>
    """.format(
        style=css,
        date=report_date.date(),
        url=report_path,
        table=html_table
    )

    output_location = os.path.join(report_path, "index.html")
    write_html_page(output_location)
    webbrowser.open("file://" + os.path.realpath(output_location))

except KeyboardInterrupt:
    print "\n** Aborted **"
    sys.exit(0)
