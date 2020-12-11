from weather_package.scripts import weather_functions
from weather_package.scripts import csv_manager
import argparse
import dbmanager as db

city_list_path = 'weather_package/data/comuni_italiani.csv'
db_path = 'weather_package/data/database.db'
results_path = 'weather_package/data/outputs.csv'


def parse_arguments():
    """Parses all the arguments passed by the user"""

    parser = argparse.ArgumentParser(description='Weather Forecast')
    parser.add_argument('city', type=str, help='Insert an Italian city'
                        , default=None)
    parser.add_argument('country', type=str, help='Input allowed: Italy'
                        , choices=['Italy'], default=None)
    parser.add_argument('day', type=int,
                        help='Allowed an integer number between 1 and 16'
                        , choices=range(1, 17), default=None)
    parser.add_argument('-u', help='username name (requires -p)',
                        default=None)
    parser.add_argument('-p', help='username password', default=None)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true',
                       help='print quiet')
    group.add_argument('-v', '--verbose', action='store_true',
                       help='print verbose')
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    # open the connection and (IF NECESSARY) create the users table
    db.open_and_create(db_path)
    args = parse_arguments()
    # If the user is authenticated proceed:
    try:
        if db.check_for_username(args.u, args.p):
            api_key = db.get_api_key(args.u, args.p)
            if csv_manager.csv_city_check(city_list_path, args.city):
                (temps, lat, lon) = \
                    weather_functions.min_max_day(api_key, args.city,
                        args.country, args.day)
                csv_manager.write_data(results_path, args.city, temps)
                if args.quiet:
                    print (temps)
                elif args.verbose:
                    print ('Weather information: ', temps)
                else:
                    print ('Weather info: ', temps)
            else:
                print ('The city you have chosen does not exist!')
    except:
        print ('Username does not exist or password is incorrect!')
