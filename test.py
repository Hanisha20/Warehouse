import sqlite3 as sql
con = sql.connect('mydb.db')
cur = con.cursor()

command = '''CREATE TABLE IF NOT EXISTS emp (id INTEGER PRIMARY KEY
                                            ,name TEXT NOT NULL UNIQUE
                                            ,salary REAL)'''

cur.execute(command)
con.commit()