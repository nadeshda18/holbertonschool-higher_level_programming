#!/usr/bin/python3
"""take in the name of a state as an argument and lists
all cities of that state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
