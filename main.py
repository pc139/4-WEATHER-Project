import weather_functions
import csv_manager
import argparse

city_list_path="data/comuni_italiani.csv"

def parse_arguments():
    parser=argparse.ArgumentParser(
            description="Weather Forecast")
    parser.add_argument ("city", type=str,
                         help= "Insert an Italian city",
                         default=None)
    parser.add_argument("country", type=str,
                        help="Input allowed: Italy",
                        choices = ["Italy"],
                         default=None)
    parser.add_argument("day", type=int,
                        help="Allowed an integer number between 1 and 16",
                        choices = range(1,17),
                         default=None)

    group=parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet", action="store_true", help ="print quiet")
    group.add_argument("-v", "--verbose", action="store_true", help="print verbose")
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = parse_arguments()
    if csv_manager.csv_city_check(city_list_path, args.city):
        temps, lat, lon = weather_functions.min_max_day(args.city, args.country, args.day)
        if args.quiet:
            print(temps)
        elif args.verbose:
            print("Weather information: ", temps)
        else:
            print("Weather info: ", temps)
    else:
        print("The chosen city does not exist")
