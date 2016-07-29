# -----------------------------------------------
# Python Examples
#
# Databases - SQLite3
# -----------------------------------------------

import sqlite3

def main():
    db = sqlite3.connect('test.db')
    #db.row_factory = sqlite3.Row
    db.execute('drop table if exists test')
    db.execute('create table test (f_name text, l_name text, dept_no int)')
    db.execute('insert into test (f_name, l_name, dept_no) values (?, ?, ?)', ('John', 'Smith', 1))
    db.execute('insert into test (f_name, l_name, dept_no) values (?, ?, ?)', ('Lisa', 'Jones', 2))
    db.commit()
    cursor = db.execute('select l_name, f_name, dept_no from test order by l_name')
    for row in cursor:
        #print(dict(row))
        print(row)

if __name__ == "__main__": main()
