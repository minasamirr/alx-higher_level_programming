#!/usr/bin/python3
"""Script to get the State object with the given name"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State object with the given name
    state = session.query(State).filter_by(name=state_name).first()

    # Print the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
