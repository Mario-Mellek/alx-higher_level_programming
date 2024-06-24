#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

def get_states(username, password, database):
    """A function that lists all states from the database hbtn_0e_0_usa"""
    try:

        db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        results = cursor.fetchall()

        for row in results:
            print(row)

        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    get_states(username, password, database)
