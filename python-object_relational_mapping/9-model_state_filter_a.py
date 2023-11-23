#!/usr/bin/python3
"""lists all state objects contain the letter a"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    """lists all state objects contain the letter a"""
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]),
                       pool_pre_ping=True)

Session = sessionmaker(bind=engine)

session = Session()

for state in session.query(State).filter(State.name.like('%a%')) \
        .oder_by(State.id):
    print("{}: {}".format(state.id, state.name))

session.close()
