import csv

def csv_city_reader(path):

    with  open(path, 'r',newline='') as f:
        rows = [ line[1] for line in csv.reader(f, delimiter=',')]
    return rows[1:]


def csv_city_check(path, city):

    l = csv_city_reader(path)
    if city in l:
        return True
