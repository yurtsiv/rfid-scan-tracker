"""
Report generation functionality
"""

import csv
import datetime

from api.data_handlers import filter_scans, find_person
from api.list_utils import group_into_pairs

def str_to_date_time(str):
    return datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S.%f')

def write_to_csv(person_name, scans_groups):
    """
    Helper function for saving generated
    report into a CSV file
    """
    with open(person_name.replace(" ", "_") + '_report.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow([
            'Enter Terminal',
            'Enter Card',
            'Enter Time',
            'Exit Terminal',
            'Exit Card',
            'Exit Time',
            'Period (hours)'
        ])

        for scan_group in scans_groups:
            enter_scan = scan_group[0]
            row = [
                enter_scan['terminal_id'],
                enter_scan['card_id'],
                enter_scan['time']
            ]


            if len(scan_group) == 2:
                exit_scan = scan_group[1]

                period_hours = round((
                    str_to_date_time(exit_scan['time']) -
                    str_to_date_time(enter_scan['time'])
                ).seconds / 3600, 2)

                row = row + [
                    exit_scan['terminal_id'],
                    exit_scan['card_id'],
                    exit_scan['time'],
                    period_hours
                ]

            writer.writerow(row)

def generate_report(person_id):
    """
    Generate the report for a particular person
    """

    person = find_person('id', person_id)
    if person is None:
        raise Exception(f"No person wtih ID {person_id} registered in the system")

    scans = filter_scans(lambda r: r.get('person_id') == person_id)
    sorted_scans = sorted(scans, key=lambda r: r['time'])
    scans_groups = group_into_pairs(sorted_scans)

    write_to_csv(person['full_name'], scans_groups)
