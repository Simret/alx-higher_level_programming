#!/usr/bin/python3
"""List all state objects"""
if__name__ == "__main__":
        from sys import argv
        from model_state import Base, State
        from sqlalchemy import (create_engine)
        from sqlalchemy.orm import sessionmaker


        engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engin)
        Session = sessionmaker(bind=engin)
        s = Session()
        for st in s.query(State).order_by(State.id):
            print("{:d}: {:s}".format(st.id, st.name))
        session().close()
