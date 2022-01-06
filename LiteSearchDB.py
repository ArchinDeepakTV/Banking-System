import sqlite3


def id_extraction(rs):
    l = []
    for i in rs:
        # converting set to list
        k = list(i)
        # taking the first element from the list and append it to the list
        l.append(k[0])
    # Converting integer list to string list
    s = [str(i) for i in l]

    # Join list items using join()
    res = int("".join(s))
    return res


def readAccNumber(accNo):
    # read account number existance in db
    sql = """SELECT accNumber FROM banking WHERE accNumber = :accNo;"""
    conn = None
    updated_rows = 0
    try:
        # connect to the SQLite File
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, {'accNo': accNo})
        result = cur.fetchall()
        res = id_extraction(result)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # close communication with the SQLite DB File
        cur.close()
        if res == accNo:
            return -1
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def readCIF(accNo, cif):
    # read cif existance in db
    sql = """SELECT cif FROM banking WHERE accNumber = :accNo AND cif = :cif;"""
    conn = None
    updated_rows = 0
    try:
        # connect to the SQLite File
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, {'accNo': accNo, 'cif': cif})
        result = cur.fetchall()
        res = id_extraction(result)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # close communication with the SQLite DB File
        cur.close()
        if res == accNo:
            return -1
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def readMailID(accNo):
    # read mail ID from db
    sql = """SELECT mail_id FROM banking WHERE accNumber = :accNo;"""
    conn = None
    updated_rows = 0
    try:
        # connect to the SQLite File
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, {'accNo': accNo})
        res = cur.fetchall()
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # close communication with the SQLite DB File
        cur.close()
        return res
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def readName(accNo):
    # read name from db
    sql = """SELECT name FROM banking WHERE accNumber = :accNo;"""
    conn = None
    updated_rows = 0
    try:
        # connect to the SQLite File
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, {'accNo': accNo})
        res = cur.fetchall()
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # close communication with the SQLite DB File
        cur.close()
        return res
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def readBalance(accNo):
    # read balance from db
    sql = """SELECT balance FROM banking WHERE accNumber = :accNo;"""
    conn = None
    updated_rows = 0
    try:
        # connect to the SQLite File
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, {'accNo': accNo})
        result = cur.fetchall()
        res = id_extraction(result)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # close communication with the SQLite DB File
        cur.close()
        return res
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def readPhoneNumber(accNo):
    # read old Phone Number from db
    sql = """SELECT phoneNumber FROM banking WHERE accNumber = :accNo;"""
    conn = None
    updated_rows = 0
    try:
        # connect to the SQLite File
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, {'accNo': accNo})
        result = cur.fetchall()
        res = id_extraction(result)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # close communication with the SQLite DB File
        cur.close()
        return res
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows
