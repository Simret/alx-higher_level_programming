#!/usr/bin/python3
"""Filter cities"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    data = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    a = data.cursor()
    check = (argv[4], )
    a.execute("SELECT * FROM cities JOIN states s ON states.id = cities.state_id WHERE states.name = %s ORDER BY cities.id ASC", check)
    x = a.fetchall()
    cities = []
    for i in x:
        if r[4] == check[0]:
            cities.append(r[2])
    print(', '.join(cities))
    a.close()
    data.close()
