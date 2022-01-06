import sqlite3


def accInfo(accNo, name, branchCode, cif, ifsc, mail_id, phoneNumber, dob, fatherName, balance):
    # insert a new account into the banking table

    sql = """INSERT INTO banking VALUES (:accNumber, :name, :branchCode, :cif, :ifsc, :mail_id, :phoneNumber, :dob, :fatherName, :balance);"""

    conn = None
    updated_rows = None
    try:
        # connect to the SQLite database
        conn = sqlite3.connect('banking.db')
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, {'accNumber': accNo, 'name': name, 'branchCode': branchCode, 'cif': cif, 'ifsc': ifsc,
                    'mail_id': mail_id, 'phoneNumber': phoneNumber, 'dob': dob, 'fatherName': fatherName, 'balance': balance})
        # get the generated ID back
        updated_rows = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the SQLite database
        cur.close()
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows
