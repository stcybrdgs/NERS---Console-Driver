#!/usr/bin/python
import sqlite3, sys, os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'testDB.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

con = db_connect()
cur = con.cursor()

cur.execute('SELECT * FROM tester')
#print(cur.fetchall())
formatted_result = [f"{id:<5}{name:<25}{age:>5}" for id, name, age in cur.fetchall()]
id, product, age = "Id", "Product", "Age"
print('\n'.join([f"{id:<5}{product:<25}{age:>5}"] + formatted_result))
con.close()
sys.exit()
# -----------------------------------------------------
print('Opened database succesfully.')

create_table_sql = """
    CREATE TABLE tester(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL
    )
    """
cur.execute(create_table_sql)

insert_records_sql = "INSERT INTO tester (ID, NAME, AGE) VALUES (?, ?, ?)"
names = ['Jo','Ann','Bo','Dee','Ra']
ages = [12,13,14,15,16]
i = 0
for name in names:
    cur.execute(insert_records_sql, (i, names[i], ages[i]))
    i += 1

con.commit()
con.close()

print('Done.')
