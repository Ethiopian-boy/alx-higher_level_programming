#!/usr/bin/python3
"""
a script that lists all City objects from the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Create an engine for database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    table = session.query(City).order_by(City.id).all()
    for city in table:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
