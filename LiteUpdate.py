import sqlite3


def update_balance(accNo, balance):
    # update customer name based on the account number

    sql = """ UPDATE banking
                SET balance = :balance
                WHERE accNumber = :accNo;"""
    conn = None
    updated_rows = 0
    try:
        # connect to the SQLite database
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE statement
        cur.execute(sql, {'balance': balance, 'accNo': accNo})
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the SQLite database
        cur.close()
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def update_phoneNumber(accNo, phoneNo):
    # update customer name based on the account number

    sql = """ UPDATE banking
                SET phoneNumber = :phone
                WHERE accNumber = :accNo;"""
    conn = None
    updated_rows = 0
    try:
        # connect to the SQLite database
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE statement
        cur.execute(sql, {'phone': phoneNo, 'accNo': accNo})
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the SQLite database
        cur.close()
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def update_mailID(accNo, mail_id):
    # update customer name based on the account number

    sql = """ UPDATE banking
                SET mail_id = :mail
                WHERE accNumber = :accNo;"""
    conn = None
    updated_rows = 0
    try:
        # connect to the SQLite database
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE statement
        cur.execute(sql, {'mail': mail_id, 'accNo': accNo})
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the SQLite database
        cur.close()
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows
