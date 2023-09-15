#!/usr/bin/python3
""" This module contains a script to select data from a database using
sqlalchemy """

from sys import argv
import MySQLdb


def select():
    """ Queries data from the states table """
    username = argv[1]
    password = argv[2]
    name = argv[3]

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=name,
            port=3306)

    curs = db.cursor()

    query = "SELECT * FROM states ORDER BY id"

    curs.execute(query)

    results = curs.fetchall()

    for state in results:
        print(state)

    curs.close()
    db.close()


if __name__ == "__main__":
    select()
