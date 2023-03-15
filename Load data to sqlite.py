import csv
import sqlite3
from frictionless import describe

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

resource = describe('Kalandra.items.csv')
print(resource)

con = create_connection('poe.sqlite3')

with open('Kalandra.items.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ';')
    for row in reader:
        if reader.line_num == 1: #header
            print(row)
        else:
            print (row)





























