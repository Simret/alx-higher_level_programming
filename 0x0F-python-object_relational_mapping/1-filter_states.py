#!/usr/bin/python3
"""Filter states by name"""
import MySQLdb as sql
from sys import argv


def main(user, password, data):
    """print states"""
    data = sql.connect(host='localhost', user=user, password=password, db=data, port=3306)
    a = data.cursor()
    a.execute("""SELECT * FROM states where name LIKE 'N%'\ ORDER BY states.id ASC")
    x = a.fetchall()
    for i in x:
        if i[1][0] == 'N':
            print(i)


if __name__ == '__main__':
main(argv[1], argv[2], argv[3])
