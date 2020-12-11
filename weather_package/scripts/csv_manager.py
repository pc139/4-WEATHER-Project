import csv
import datetime

def csv_city_reader(path):
    """Open a csv reader, starting from the second row, as the first one
    is the header row.
    """

    with  open(path, 'r',newline='') as f:
        rows = [ line[1] for line in csv.reader(f, delimiter=',')]
    return rows[1:]


def csv_city_check(path, city):
    """This function checks whether the queried city belongs to the list of
    Italian cities, opened in the previous csv reader.

    Keyword arguments:
    path – the path of the csv file with the list of Italian cities
    city -- the city queried by the user
    """

    l = csv_city_reader(path)
    if city in l:
        return True


def create_csv(path):
    """This function creates an empty csv with three columns, namely:
    datetime, city and forecast.
    """

    with open(path, "w",newline='') as my_empty_csv:
        columns = ['datetime','city','forecast']
        writer = csv.writer(my_empty_csv)
        writer.writerow(columns)
    return my_empty_csv


def write_data(path,city,temps):
    """Check whether there exists already a csv file located in path.
    If yes it opens the file, otherwise it creates a new csv file
    located in path. Then, it populates the csv file with the
    information provided through the user query by running the main program
    plus the datetime in which the user launched the program.

    Keyword arguments:
    path – the path of the csv file with the list of Italian cities
    city -- the city queried by the user
    temps --- output string containing weather information, which appears
    to the user after they launch the main program
    """

    try:
        open(path)
    except FileNotFoundError:
        create_csv(path)

    date = datetime.datetime.now()
    fields=[date, city, temps]
    with open(path, 'r',newline='') as f:
        rows = [ line for line in csv.reader(f, delimiter=',')]
        if fields not in rows:
            with open(path, 'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
