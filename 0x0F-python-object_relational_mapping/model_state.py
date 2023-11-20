#!/usr/bin/python3
"""Lists all cities from the state given as an argument from the database hbtn_0e_4_usa using SQLAlchemy."""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()

class State(Base):
        __tablename__ = 'states'
            id = Column(Integer, primary_key=True)
                name = Column(String(128), nullable=False)
                    cities = relationship("City", backref="state")

                    class City(Base):
                            __tablename__ = 'cities'
                                id = Column(Integer, primary_key=True)
                                    name = Column(String(128), nullable=False)
                                        state_id = Column(Integer, ForeignKey('states.id'))

                                        if __name__ == "__main__":
                                                username = sys.argv[1]
                                                    password = sys.argv[2]
                                                        database = sys.argv[3]
                                                            state_name = sys.argv[4]

                                                                engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
                                                                    Base.metadata.create_all(engine)

                                                                        Session = sessionmaker(bind=engine)
                                                                            session = Session()

                                                                                state = session.query(State).filter(State.name == state_name).one_or_none()
                                                                                    if state:
                                                                                                cities = [city.name for city in state.cities]
                                                                                                        print(", ".join(cities))
                                                                                                            else:
                                                                                                                        print("Not found")

                                                                                                                            session.close()
