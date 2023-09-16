#!/usr/bin/python3
""" This module contains a script that lists all State objects
that contain letter 'a' from a database """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
            @localhost:3306/{database_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State)\
        .order_by(State.id).filter(State.name.like('%a%')).all()

    for result in results:
        print(f'{result.id}: {result.name}')
