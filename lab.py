import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "insert into celebs values(?, ?, ?, ?, ?, ?, ?)"
data=((1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402021/aj.jpg", "American actress and filmmaker"),
      (2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402021/bp.jpg", "He is the recipient of numerous accolades, including an Academy Award, a British Academy Film Award, and two Golden Globe Awards"),
      (3, "Sonw", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402021/sw.jpg", "Exiled into the dangerous forest by her wicked stepmother, a princess is rescued by seven dwarf miners who make her part of their household"),
      (4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402021/dv.jpg", "a fictional character in the Star Wars franchise"),
      (5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402021/ts.jpg", " an American singer-songwriter. Her discography spans multiple genres, and her narrative songwriting, ..."),
      (6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402021/bk.jpg", "Born and raised in Houston, Texas, Beyoncé performed in various singing and dancing competitions as a child. She rose to fame in the late 1990s as the lead ..."),
      (7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402021/sg.jpg", "Selena Marie Gomez is an American singer, actress, and producer. Born and raised in Texas, Gomez began her acting career on the children's television series ..."),
      (8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402021/sc.jpg", "is an American professional basketball player for the Golden State Warriors of the National Basketball ..."))
cursor.executemany(sql,data)
conn.commit()
conn.close()
