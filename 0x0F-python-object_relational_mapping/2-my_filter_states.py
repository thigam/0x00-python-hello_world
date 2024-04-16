#!/usr/bin/python3
"""
Contains a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

def main():
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    search_word = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name=%s", (search_word,))
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            print("%s",col)
        print("\n")

if __name__=="__main__":
    main()
