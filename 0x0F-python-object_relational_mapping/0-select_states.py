#!/usr/bin/python3
"""List all states"""
import MySQLdb as sql 


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    data = sql.connect(user=argv[1], passwd=argv[2], db=argv[3])
    a = data.cursor()
    a.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    x = a.fetchall()
    for i in x:
        print(i)
    a.close()
    data.close()
