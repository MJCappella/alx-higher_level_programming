#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    connec = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = connec.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    values = cur.fetchall()
    for value in values:
        print(value)
    cur.close()
    connec.close()
