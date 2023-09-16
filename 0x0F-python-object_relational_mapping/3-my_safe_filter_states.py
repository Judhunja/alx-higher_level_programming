#!/usr/bin/python3
""" This module contains a function select """

from sys import argv
from re import match
import MySQLdb


def select():
    """ Queries data from a database using parametized values to
    prevent SQL injection """
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

    query = 'SELECT * FROM states WHERE BINARY name LIKE %s ORDER BY id ASC'

    curs.execute(query, (state_name,))

    results = curs.fetchall()

    for state in results:
        print(state)

    curs.close()
    db.close()


if __name__ == "__main__":
    select()
