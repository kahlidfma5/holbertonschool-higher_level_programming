#!/usr/bin/python3
import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        return
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC;")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()

if _name_ == "_main_":
    main()
