import sqlite3

conn = sqlite3.connect('rfid.db')

print("Opened database successfully")
sqlite = conn.cursor()
sqlite.execute('''CREATE TABLE if not exists student
       (id    varchar(25)  PRIMARY KEY NOT NULL,
       name   varchar(50)  UNIQUE  NOT NULL,
       number varchar(15)  NOT NULL,
       sex    varchar(10),
       major  varchar(50));''')
conn.commit()


def getSQL():
    result = sqlite.execute('''select * from student;''')
    return result.fetchall()


def findSQL(ID):
    result = sqlite.execute('''SELECT COUNT(*)
        FROM student WHERE id='{}';'''.format(ID))
    if result.fetchone()[0]:
        result = sqlite.execute('''SELECT *
        FROM student WHERE id='{}';'''.format(ID))
        return result.fetchone()
    else:
        return False


def insertSQL(ID, name, number, sex='null', major='null'):
    try:
        query = '''insert into student(id,name,number,sex,major)
        values ('{0}','{1}','{2}','{3}','{4}');'''.format(ID, name, number, sex, major)
        print(query)
        sqlite.execute(query)
        conn.commit()
        return False
    except Exception as err:
        print(err)
        return err


def updateSQL(ID, name, number, sex='null', major='null'):
    try:
        sqlite.execute('''update student set  name='{}',number='{}',sex='{}',major='{}'
        where id='{}';'''.format(name, number, sex, major, ID))
        conn.commit()
        return False
    except Exception as err:
        print(err)
        return err


def removeSQL(ID):
    sqlite.execute('''delete from student
    where id='{0}';'''.format(ID))
    conn.commit()


print(getSQL())
