#!/usr/bin/python3
"""  Script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb;
import sys



if __name__ == "__main__":
    connec = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = connec.cursor()
    cur.execute("SELECT * FROM states")
    values = cur.fetchall()
    for value in values:
        print(value)
    cur.close()
    connec.close()
