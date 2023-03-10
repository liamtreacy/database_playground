import sqlite3
import os
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        print(db_file)
        conn = sqlite3.connect(db_file)

        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    db_loc = os. getcwd() + r"/database/demo.db"
    create_connection(db_loc)

