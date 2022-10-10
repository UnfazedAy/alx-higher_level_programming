#!/usr/bin/python3
"""Display name argument of states table"""
import MySQLdb
from sys import argv


def filter_names():
    """Takes arguments argv to list from database
    Only lists with states that start with  N
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: name searched
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8"
                         )

    # Getting a cursor in MySQLdb python
    cur = db.cursor()

    # Executing db queries
    cur.execute("SELECT * FROM states WHERE name = '{}'\
                ORDER BY id ASC".format(argv[4]))

    # fetches all the rows of a query result
    query_row = cur.fetchall()

    # Printing the result one in one
    for row in query_row:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_names()
