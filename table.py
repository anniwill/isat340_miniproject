import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()
sql="create table member_login(memberID integer PRIMARY KEY, username text, password text)"
cursor.execute(sql)
conn.commit()
conn.close()
