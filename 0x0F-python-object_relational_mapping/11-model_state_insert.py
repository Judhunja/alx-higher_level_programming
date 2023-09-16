#!/usr/bin/python3
""" This module contains a script that adds a state object to a
database """

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

    new_state = State(name='Louisiana')

    session.add(new_state)

    session.commit()

    print(f'{new_state.id}')

    session.close()
