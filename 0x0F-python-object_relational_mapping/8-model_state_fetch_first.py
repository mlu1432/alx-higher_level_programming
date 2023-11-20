#!/usr/bin/python3
"""
Write a script that prints the first State object from the
database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
        username = sys.argv[1]
            password = sys.argv[2]
                database = sys.argv[3]

                    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)
                        
                            Session = sessionmaker(bind=engine)
                                session = Session()

                                    state = session.query(State).order_by(State.id).first()
                                        if state is not None:
                                                    print(f"{state.id}: {state.name}")
                                                        else:
                                                                    print("Nothing")

                                                                        session.close()
