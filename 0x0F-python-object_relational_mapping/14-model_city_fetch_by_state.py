#!/usr/bin/python3
""" This module contains a script that prints all City
objects from a database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
            @localhost:3306/{database_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State.name, City.id, City.name)\
        .filter(State.id == City.state_id).order_by(City.id)

    if results is not None:
        for result in results:
            print(f'{result[0]}: ({result[1]}) {result[2]}')
