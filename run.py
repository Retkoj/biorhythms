import argparse
import re
from argparse import Namespace
from datetime import datetime

from biorhytms_calculation import calculate_biorhythm_position


def parse_date(date_string: str):
    """"Parse 'yyyy-mm-dd' string to datetime"""
    return datetime.strptime(date_string, "%Y-%m-%d")


def check_date_format(date_string: str):
    """Validate datetime format of 'yyyy-mm-dd'"""
    if re.match('^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}', date_string):
        return True
    print('Date should be in format "yyyy-mm-dd", e.g. "2011-11-02"')
    return False


def process_input(args: Namespace) -> (datetime, datetime):
    """
    Validate command line input and parse dates to datetime if valid

    :param args: commandline arguments
    :return: tuple of birth_date, other_date
    """
    if check_date_format(args.birth_date):
        birth_date = parse_date(args.birth_date)
        if args.specific_date and check_date_format(args.specific_date):
            other_date = parse_date(args.specific_date)
        else:
            print('Defaulting to date of today')
            other_date = datetime.today()

        if birth_date >= other_date:
            print(f'Birth date ({birth_date}) should be before the date to check ({other_date})')
        else:
            return birth_date, other_date
    else:
        return None, None


def run(args: Namespace):
    birth_date, other_date = process_input(args)
    if birth_date and other_date:
        time_delta_days = (other_date - birth_date).days
        print(f'{time_delta_days} days between birth date and specified date')
        physical_current_pos, emotional_current_pos, mental_current_pos = \
            calculate_biorhythm_position(birth_date, other_date)
        print(f'Physical currently at: {physical_current_pos}')
        print(f'Emotional currently at: {emotional_current_pos}')
        print(f'Physical currently at: {mental_current_pos}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Calculate biorhythm status")
    parser.add_argument('--birth-date', type=str, required=True,
                        help="Birth date in format yyyy-mm-dd, e.g. 2011-11-02")
    parser.add_argument('--specific-date', type=str,
                        help="Optionally enter a date for which to calculate the biorhythm. "
                             "Date should be later than birth date. "
                             "Format yyyy-mm-dd, e.g. 2021-12-02")
    args = parser.parse_args()
    run(args)
