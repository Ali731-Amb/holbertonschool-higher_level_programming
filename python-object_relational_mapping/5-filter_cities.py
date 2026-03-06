#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    # Utilisation d'une seule chaîne avec des espaces clairs
    query = """SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name =%s
                ORDER BY cities.id ASC"""
    cur.execute(query)
    rows = cur.fetchall()
    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))
    cur.close()
    db.close()
