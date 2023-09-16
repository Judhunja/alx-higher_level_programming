#!/usr/bin/python3
""" This module contains a script that deletes all State
objects in a database containing the letter 'a' from a database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
            @localhost:3306/{database_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State).filter(State.name.like('%a%')).all()

    if results is not None:
        for result in results:
            session.delete(result)
            session.commit()

    session.close()
