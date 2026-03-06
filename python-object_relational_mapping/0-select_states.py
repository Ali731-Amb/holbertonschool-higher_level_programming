
#!/usr/bin/python3
"""
0-select_states.py

Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
Connects to a MySQL server running on localhost at port 3306.
Prints all states in the 'states' table, sorted by id in ascending order.
"""

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and lists all states in the 'states' table.
    Prints each row as a tuple.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
