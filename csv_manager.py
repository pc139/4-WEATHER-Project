import csv
import datetime

def csv_city_reader(path):

    with  open(path, 'r',newline='') as f:
        rows = [ line[1] for line in csv.reader(f, delimiter=',')]
    return rows[1:]


def csv_city_check(path, city):

    l = csv_city_reader(path)
    if city in l:
        return True


def create_csv(path):
    with open(path, "w",newline='') as my_empty_csv:
        columns = ['datetime','city','forecast']
        writer = csv.writer(my_empty_csv)
        writer.writerow(columns)
    return my_empty_csv


def write_data(path,city,temps):
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