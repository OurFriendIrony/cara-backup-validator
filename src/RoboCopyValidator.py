import sys
import os
import webbrowser
from src.RoboCopyReport import *

COLOUR_FAILED = "#FFB3B3"
COLOUR_OK = ""

HTML_BODY = """
<!DOCTYPE html>
<html>
  <body>
    <style>{style}</style>
    <b>Date:</b> {date}<br/>
    <b>Path:</b> <a href="file://{url}">{url}</a><br/>
    <b>Number of Issues:</b> {issue_count}<br/><br/>
    <b>Reports</b>
    <table>
      <tr>
        <th>Failed<br/>Dirs</th>
        <th>Failed<br/>Files</th>
        <th>Filename</th>
      </tr>
      {table}
    </table>
  </body>
</html>
"""

HTML_TABLE_ROW = """
<tr bgcolor="{colour}">
  <td>{failed_dirs}</td>
  <td>{failed_files}</td>
  <td><a href="file://{path}">{name}</a></td>
</tr>
"""

HTML_TABLE_CSS = "table, th, td {border: 0.2px solid black;}"

DATE_FMT = "%d/%m/%y"

DEFAULT_PATH = os.path.dirname(__file__).rsplit('/', 1)[0]
DEFAULT_DATE = dt.now().strftime(DATE_FMT)

FILES_MATCHING = r'.*.txt'


def input_date():
    is_valid = False
    d = ""
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
    in_path = ""
    while not is_valid:
        in_path = raw_input("Enter Path [%s]: " % DEFAULT_PATH) or DEFAULT_PATH
        if os.path.isdir(in_path):
            is_valid = True
        else:
            print "** Invalid Path **\n"
    return in_path


def write_html_page(path, html_body):
    output_file = open(path, 'w')
    output_file.write(html_body)
    output_file.flush()
    output_file.close()


def get_reports(report_path, report_date):
    reports = []
    for file_name in os.listdir(report_path):
        file_path = os.path.join(report_path, file_name)
        file_created = dt.fromtimestamp(os.path.getmtime(file_path))

        if re.match(FILES_MATCHING, file_name) and file_created.date() == report_date.date():
            file_body = open(file_path, 'r').read()
            reports.append(RoboCopyReport(file_body, file_name))

    return reports


def main():
    report_date = input_date()
    report_path = input_path()
    all_reports = get_reports(report_path, report_date)

    html_table = ""
    for report in all_reports:
        colour = COLOUR_FAILED if report.has_failed() else COLOUR_OK

        html_table += HTML_TABLE_ROW.format(
            colour=colour,
            failed_dirs=report.get_failed_dirs(),
            failed_files=report.get_failed_files(),
            path=os.path.join(report_path, report.get_name()),
            name=report.get_name()
        )

    body = HTML_BODY.format(
        style=HTML_TABLE_CSS,
        date=report_date.date(),
        issue_count="{} / {}".format(sum(r.has_failed() for r in all_reports), len(all_reports)),
        url=report_path,
        table=html_table
    )

    output_location = os.path.realpath("index.html")
    write_html_page(output_location, body)
    webbrowser.open("file://" + output_location)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\n** Aborted **"
        sys.exit(0)
