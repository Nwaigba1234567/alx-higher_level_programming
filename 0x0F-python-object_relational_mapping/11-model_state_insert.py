#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""


import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306

    Session = sessionmaker()
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}/{db_name}',pool_pre_ping=True,)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    new_state = session.query(State).filter_by(name='Louisiana').first()
    print(new_state.id)
