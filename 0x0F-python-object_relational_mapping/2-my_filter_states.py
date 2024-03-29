#!/usr/bin/python3
""" This module contains a function select """

from sys import argv
import MySQLdb


def select():
    """ This function selects states from a database that
    match a certain parameter """

    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database_name,
                         port=3306)

    curs = db.cursor()

    query = "SELECT * FROM states \
            WHERE BINARY name LIKE '{}' ORDER BY id".format(state_name)

    curs.execute(query)

    results = curs.fetchall()

    for state in results:
        print(state)

    curs.close()
    db.close()


if __name__ == "__main__":
    select()
