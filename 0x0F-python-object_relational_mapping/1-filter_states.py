#!/usr/bin/python3
"""Filter states by name"""
import MySQLdb as sql


if __name__ == "__main__":
    from sys import argv
    import mySQLdb
    data = sql.connect(host='localhost', user=user, password=password, db=data, port=3306)
    a = data.cursor()
    a.execute("""SELECT * FROM states where name LIKE 'N%'\ ORDER BY states.id ASC")
    x = a.fetchall()
    for i in x:
        if i[1][0] == 'N':
            print(i)
    a.close()
    data.close()
