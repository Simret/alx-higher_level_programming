#!/usr/bin/python3
"""Filter states by name"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    data = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    a = data.cursor()
    a.execute("""SELECT * FROM states where name LIKE 'N%'\ ORDER BY states.id ASC")
    x = a.fetchall()
    for i in x:
        if i[1][0] == 'N':
            print(i)
    a.close()
    data.close()
