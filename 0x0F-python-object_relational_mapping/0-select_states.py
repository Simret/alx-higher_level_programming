#!/usr/bin/python3
"""List all states"""
import MySQLdb as sql
from sys import argv


def main(user, password, data):
    """print states"""
    data = sql.connect(host='localhost', user=user, password=password, db=data, port=3306)
            a = data.cursor()
            a.execute("""SELECT id, name FROM states ORDER BY id;""")
            x = a.fetchall()
            for i in x:
                print(i)


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
