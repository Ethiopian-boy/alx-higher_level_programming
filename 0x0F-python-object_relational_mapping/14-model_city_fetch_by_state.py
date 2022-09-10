#!/usr/bin/python3
"""
Cities in state
parameters given to script: userename passwd database
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # create engine for database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query multiple table
    for ele in session.query(State.name, City.id, City.nmae).filter(
              State.id == City.state.id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(ele[0], ele[1], ele[2]))

    session.close()
