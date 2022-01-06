import sqlite3


def create_tables():
    """ create tables in the SQL Lite database"""
    commands = (
        """
        CREATE TABLE banking (
            accNumber integer PRIMARY KEY UNIQUE,
            name text,
            mail_id text,
            phoneNumber integer,
            cif integer unique,
            branchCode integer,
            ifsc text,
            fatherName text,
            dob text
            balance real
        );
        """)
    conn = None
    try:
        # connect to the SQLite File
        conn = sqlite3.connect('banking.db')
        cur = conn.cursor()
        # create table {NAMES}
        for command in commands:
            cur.execute(command)
        # close communication with the SQLite DB File
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
