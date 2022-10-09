#!/usr/bin/python3
"""Prints the first state obj, takes 3 args"""
from sys import argv
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(user, password, data):
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, data), pool_pre_ping=True)
    Base.metadata.create_all(engin)
    Session = sessionmaker(bind=engin)
    s = Session()
    st = s.query(state).first()
    if st:
        print("{:d}: {:s}".format(st.id, st.name))
    else:
        print("Nothing")
        

if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
