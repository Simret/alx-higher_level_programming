#!/usr/bin/python3
"""List states in database"""


def main(user, password, data):
    from sys import argv
    import MySQLdb
    data = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    a = data.cursor()
    a.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON states.id = cities.state_id ORDER BY id ASC;")
    x = a.fetchall()
    for i in x:
        print(i)
    a.close()
    data.close()
