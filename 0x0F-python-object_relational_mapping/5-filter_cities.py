#!/usr/bin/python3
""" This module contains a function select """

import MySQLdb
from sys import argv


def select():
    """ Takes the name of a state and lists all the cities
    of that state """

    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database_name,
            port=3306)

    curs = db.cursor()

    query = '''
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE BINARY states.name LIKE %s
    ORDER BY cities.id ASC
    '''

    curs.execute(query, (state_name,))

    results = curs.fetchall()

    cities = []
    for city in results:
            cities += city
    cities = str(set(cities))

    clean_cities = cities.replace("'", "").replace("}", "").replace("{", "")

    print(clean_cities)

    curs.close()
    db.close()


if __name__ == "__main__":
    select()
