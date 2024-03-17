#!/usr/bin/python3
"""  a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections! """
import MySQLdb
import sys


if __name__ == "__main__":
    connec = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = connec.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    values = cur.fetchall()
    for value in values:
        print(value)
    cur.close()
    connec.close()
