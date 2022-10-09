#!/usr/bin/python3
"""List state name based on passed argument"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    data = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    a = data.cursor()
    a.execute("SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(argv[4]))
    x = a.fetchall()
    for i in x:
        if i[1] == argv[4]:
            print(i)
    a.close()
    db.close()
