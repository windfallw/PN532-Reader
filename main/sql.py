import sqlite3

conn = sqlite3.connect('rfid.db')

print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE if not exists student
       (id    text      PRIMARY KEY NOT NULL,
       name   text(10)  NOT NULL,
       number char(10)  NOT NULL,
       sex    text(10),
       major  text(10));''')
conn.commit()
conn.close()


def insertSQL():
    ...


def removeSQL():
    ...


def updateSQL():
    ...
