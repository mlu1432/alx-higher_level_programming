#!/usr/bin/python3
"""
Script that fetches all cities by state from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch cities with corresponding state names
    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
