#!/usr/bin/python3
"""Script to delete State objects with name containing the letter 'a'"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the State objects
    for state in states_with_a:
        session.delete(state)

    # Commit the session to save the changes to the database
    session.commit()

    # Close the session
    session.close()
