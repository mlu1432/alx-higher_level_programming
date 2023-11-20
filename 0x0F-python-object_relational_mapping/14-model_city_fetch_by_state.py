#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
sorted in ascending order by cities.id
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
            Base.metadata.create_all(engine)
                Session = sessionmaker(bind=engine)
                    session = Session()

                        cities = session.query(City, State).join(State).order_by(City.id).all()
                            for city, state in cities:
                                        print(f"{state.name}: ({city.id}) {city.name}")

                                            session.close()
