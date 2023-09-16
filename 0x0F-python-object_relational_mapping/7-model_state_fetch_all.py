#!/usr/bin/python3
""" Lists all states using sqlalchemy """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}\
            @localhost:3306/{database_name}")

    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State).order_by(State.id).all()

    for obj in results:
        print(f"{obj.id}: {obj.name}")

    session.close()
