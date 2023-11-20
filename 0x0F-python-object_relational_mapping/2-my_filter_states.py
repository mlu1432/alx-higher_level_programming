#!/usr/bin/python3
""" takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. """
import MySQLdb
import sys

if __name__ == "__main__":
        if len(sys.argv) != 5:
                    print("Usage: {} <username> <password> <database> <state name>".format(sys.argv[0]))
                            sys.exit(1)
                                
                                    username, password, database, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

                                        db = MySQLdb.connect(host="localhost", user=username,
                                                                         passwd=password, db=database, port=3306)

                                            cur = db.cursor()

                                                cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC", (search_name,))

                                                    rows = cur.fetchall()

                                                        for row in rows:
                                                                    print(row)

                                                                        cur.close()
                                                                            db.close()
