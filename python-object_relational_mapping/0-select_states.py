#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute the query to get all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    states = cur.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Clean up
    cur.close()
    db.close()
