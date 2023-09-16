#!/usr/bin/python3
""" prints the first State object from a database """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}\
            @localhost:3306/{database_name}")

    Session = sessionmaker(bind=engine)

    session = Session()

    a = 'a'

    result = session.query(State).order_by(State.id).first()

    if result is None:
        print("Nothing")
    else:
        print(f"{result.id}: {result.name}")
