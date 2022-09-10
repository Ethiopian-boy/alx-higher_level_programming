#!/usr/bin/python3
"""
return all table value of cities by states
parameters give to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # create connection with database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to execute queries using SQl
    cur = db.cursor()
    sql_exc = """SELECT cities.id, cities.name, states.name
                FROM states
                INNER JOIN cities ON states.id = cities.state_id
                ORDER BY cities.id"""
    cur.execute(sql_exc)

    for rows in cur.fetchall():
        print(rows)
    cur.close()
    db.close()
