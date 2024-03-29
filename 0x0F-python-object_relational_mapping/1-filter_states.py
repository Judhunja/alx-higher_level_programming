#!/usr/bin/python3
""" This module contains a function select """

import MySQLdb
from sys import argv
from re import match


def select():
    """ This function lists all states with a name that starts
    with 'N' """
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database_name,
                         port=3306)

    curs = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"

    curs.execute(query)

    results = curs.fetchall()

    for state in results:
        if match(r'^N', state[1]):
            print(state)

    curs.close()
    db.close()


if __name__ == "__main__":
    select()
