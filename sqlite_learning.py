import sqlite3

# makes a file to store db
conn = sqlite3.connect('employee.db')

# stores db in RAM. used only for testing
conn = sqlite3.connect(':memory:')

cur = conn.cursor()

cur.execute('''CREATE TABLE employees ( 
                firstName text,
                lastName text,
                pay integer,
            )''')

first1 = 'archin'
last1 = 'deepak'
pay1 = 60000

with conn:
    cur.execute('INSERT INTO employees VALUES (?,?,?)', (first1, last1, pay1))

conn.commit()

cur.execute('INSERT INTO employees VALUES (:first,:last,:pay)',
            {'first': first1, 'last': last1, 'pay': pay1})

conn.commit()

cur.execute('SELECT * FROM employees WHERE last=?', ('deepak',))

cur.execute('SELECT * FROM employees WHERE last=:last', {'last': 'deepak'})

conn.commit()

conn.close()
