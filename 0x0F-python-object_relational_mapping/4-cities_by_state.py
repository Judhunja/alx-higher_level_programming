#!/usr/bin/python3
""" This module contains a function select """

from sys import argv
import MySQLdb


def select():
    """ Lists all cities from a database """
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database_name,
            port=3306)

    curs = db.cursor()

    query = 'SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states \
            WHERE states.id = cities.state_id \
            GROUP BY cities.id \
            ORDER BY cities.id ASC'

    curs.execute(query)

    results = curs.fetchall()

    for city in results:
        print(city)

    curs.close()
    db.close()


if __name__ == "__main__":
    select()
