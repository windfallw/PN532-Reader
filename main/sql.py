import sqlite3

conn = sqlite3.connect('rfid.db')

print("Opened database successfully")
sqlite = conn.cursor()
sqlite.execute('''CREATE TABLE if not exists student
       (id    text      PRIMARY KEY NOT NULL,
       name   text(10)  UNIQUE  NOT NULL,
       number char(10)  NOT NULL,
       sex    text(10),
       major  text(10));''')
conn.commit()


def getSQL():
    result = sqlite.execute('''select * from student;''')
    print(result.fetchall())
    return result


def findSQL(id):
    result = sqlite.execute('''SELECT COUNT(*)
        FROM student WHERE id='{}';'''.format(id))
    return result.fetchone()[0]


def insertSQL(ID, name, number, sex='null', major='null'):
    query = '''insert into student(id,name,number,sex,major)
    values ({0},{1},{2},{3},{4});'''.format(ID, name, number, sex, major)
    print(query)
    sqlite.execute(query)
    conn.commit()


def updateSQL(ID, name, number, sex='null', major='null'):
    sqlite.execute('''update student set  name={0},number={1},sex={2},major={3}
    where id='{4}';'''.format(name, number, sex, major, ID))
    conn.commit()


def removeSQL(ID):
    sqlite.execute('''delete from student
    where id='{0}';'''.format(ID))
    conn.commit()


getSQL()
