#!/usr/bin/python3
""" This module contains a script that prints the State
object with a specified name passed as an argument """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
                           @localhost:3306/{database_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State)\
        .order_by(State.id).filter(State.name.like(f'{state_name}')).all()

    try:
        print(f'{results[0].id}')
    except Exception:
        print("Not found")
