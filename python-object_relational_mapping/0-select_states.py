#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    """Lists all states from database hbtn_0e_0_usa"""
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
