#!/usr/bin/python3
"""
Change the name of the State object with id=2 to 'New Mexico'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
        engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')
            Base.metadata.create_all(engine)
                Session = sessionmaker(bind=engine)
                    session = Session()
                        
                            state_to_update = session.query(State).get(2)
                                if state_to_update:
                                            state_to_update.name = 'New Mexico'
                                                    session.commit()
                                                        
                                                            session.close()
