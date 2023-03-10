import sqlite3
import os
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def create_tables(conn):
    conn.execute('''
              CREATE TABLE IF NOT EXISTS students
              ([student_id] INTEGER PRIMARY KEY AUTOINCREMENT, [student_name] TEXT)
              ''')

    conn.execute('''
              CREATE TABLE IF NOT EXISTS laptops
              ([student_id] INTEGER PRIMARY KEY AUTOINCREMENT, [laptop_name] TEXT)
              ''')

    conn.commit()

def populate_tables(conn, noOfEntries):
    student_names = ["Jane", "Peter", "Aisling", "Stan", "Trista"]
    laptop_names = ["abcedf", "hijk", "lmno", "pqr", "tuv"]

    for i in range(noOfEntries):
        conn.execute(f'''
                  INSERT INTO students (student_name)
                        VALUES
                        ('{student_names[i%5]}')
                  ''')

        conn.execute(f'''
                  INSERT INTO laptops (laptop_name)
                        VALUES
                        ('{laptop_names[i%5]}')
                  ''')

    conn.commit()


def close_db_connection(conn):
    conn.close()


def print_file_size(db_loc):
    print('File size is: ' + str(os.path.getsize(db_loc)/1000000) + ' mb')


if __name__ == '__main__':
    db_loc = os.getcwd() + r"/database/demo.db"
    conn = create_connection(db_loc)
    create_tables(conn)
    populate_tables(conn, 10000000)
    close_db_connection(conn)
    print_file_size(db_loc)
    # create foriegn key relationship to have a better example of 'real world'
    # create programs to do lots of transactions on db
    # then measure size
    # do a vacuum and then remeasure size
