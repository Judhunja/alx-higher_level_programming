#!/usr/bin/python3
""" This module contains a script that changes the name of a state
object from a database """

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

    to_edit = session.query(State).filter_by(id=2).first()

    if to_edit is not None:
        to_edit.name = 'New Mexico'
        session.commit()

    session.close()
