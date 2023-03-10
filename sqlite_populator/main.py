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
              ([laptop_id] INTEGER PRIMARY KEY, [laptop_name] TEXT)
              ''')

    conn.execute('''
              CREATE TABLE IF NOT EXISTS chargers
              ([charger_id] INTEGER PRIMARY KEY AUTOINCREMENT, [laptop_id] TEXT,
              FOREIGN KEY(laptop_id) REFERENCES laptops(laptop_id))
              ''')

    conn.commit()

def populate_tables(conn, noOfEntries):
    student_names = ["Jane", "Peter", "Aisling", "Stan", "Trista"]
    laptop_names = ["acer", "hp", "lenovo", "dell", "mac"]

    for i in range(noOfEntries):
        conn.execute(f'''
                  INSERT INTO students (student_name)
                        VALUES
                        ('{student_names[i%5]}')
                  ''')

        conn.execute(f'''
                  INSERT INTO laptops (laptop_id, laptop_name)
                        VALUES
                        ('{i}','{laptop_names[i%5]}')
                  ''')

        conn.execute(f'''
                  INSERT INTO chargers (laptop_id)
                        VALUES
                        ('{i}')
                  ''')

    conn.commit()


def close_db_connection(conn):
    conn.close()


def print_file_size(db_loc):
    print('File size is: ' + str(os.path.getsize(db_loc)/1000000) + ' mb')


def create_and_populate_db(db_loc, noOfEntriesPerTable):
    conn = create_connection(db_loc)
    create_tables(conn)
    populate_tables(conn, noOfEntriesPerTable)
    return conn


def update_macs(conn):
    conn.execute('''
        UPDATE laptops
        SET laptop_name = 'macOS'
        WHERE laptop_name = 'mac';
        ''')
    conn.commit()


def update_aisling(conn):
    conn.execute('''
        UPDATE students
        SET student_name = 'aishling'
        WHERE student_name = 'aishling';
        ''')
    conn.commit()



def delete_some_students(conn):
    conn.execute('''
        DELETE FROM students
        WHERE student_name = 'aishling';
        ''')
    conn.commit()



def delete_chargers(conn):
    conn.execute('''
        DELETE FROM chargers
        ''')
    conn.commit()


def delete_laptops(conn):
    conn.execute('''
        DELETE FROM laptops
        ''')
    conn.commit()


def vacuum(conn):
    conn.execute('''
        VACUUM;
    ''')
    conn.commit()


if __name__ == '__main__':
    db_loc = os.getcwd() + r"/database/demo.db"
    conn = create_and_populate_db(db_loc, 10000000)
    close_db_connection(conn)
    print("#####\nDatabase file created\n")
    print_file_size(db_loc)
    print("#####\n")


    print("\nUpdating Macs...\n")
    conn = create_connection(db_loc)
    update_macs(conn)
    close_db_connection(conn)

    print("\nUpdating Student names...\n")
    conn = create_connection(db_loc)
    update_aisling(conn)
    close_db_connection(conn)

    print_file_size(db_loc)
    print("#####\n")

    print("\nDeleting students")
    conn = create_connection(db_loc)
    delete_some_students(conn)
    close_db_connection(conn)

    print("\nDelete all chargers")
    conn = create_connection(db_loc)
    delete_chargers(conn)
    close_db_connection(conn)

    print("\nDelete all chargers")
    conn = create_connection(db_loc)
    delete_laptops(conn)
    close_db_connection(conn)

    print("\nPRE-VACUUM SIZE")
    print_file_size(db_loc)
    print("#####\n")

    conn = create_connection(db_loc)
    vacuum(conn)
    close_db_connection(conn)

    print("\nPOST-VACUUM SIZE")
    print_file_size(db_loc)
    print("#####\n")

