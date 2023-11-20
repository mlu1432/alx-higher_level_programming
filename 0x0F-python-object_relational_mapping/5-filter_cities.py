#!/usr/bin/python3
"""Lists all cities from the state given as an argument from the database hbtn_0e_4_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
        username = sys.argv[1]
            password = sys.argv[2]
                database = sys.argv[3]
                    state_name = sys.argv[4]

                        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
                            cur = db.cursor()

                                cur.execute("""SELECT cities.name FROM
                                                    cities INNER JOIN states ON states.id=cities.state_id
                                                                        WHERE BINARY states.name = %s ORDER BY cities.id""", (state_name,))
                                    rows = cur.fetchall()
                                        print(", ".join(city[0] for city in rows))

                                            cur.close()
                                                db.close()
