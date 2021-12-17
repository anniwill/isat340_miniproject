import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "insert into member_login values(?, ?, ?)"
data=(2, "!annie!", "asdfghjkl")
cursor.execute(sql,data)
conn.commit()
conn.close()
