import sqlite3

# Use 4 spaces as indent


def getConnection():
    return sqlite3.connect('addressbook.db')

def getPerson():
    # Connection 으로부터 Cursor 생성
    conn = getConnection()

    curs = conn.cursor()

    # SQL문 실행
    sql = "SELECT * FROM addressbook ORDER BY name"
    curs.execute(sql)

    # 데이타 Fetch
    row = curs.fetchall()

    # Connection 닫기
    conn.close()

    return row


def setPerson(name, number, email):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("INSERT INTO ADDRESSBOOK VALUES(?, ?, ?, ?)", (None, name, number, email))

    conn.commit()

    conn.close()

def searchPerson(key):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE name LIKE ?", ('%{}%'.format(key),))
    row1 = curs.fetchall()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE number LIKE ?", ('%{}%'.format(key),))
    row2 = curs.fetchall()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE email LIKE ?", ('%{}%'.format(key),))
    row3 = curs.fetchall()

    conn.close()


    if key == "":
        return row1

    else:
        return row1 + row2 + row3

def searchById(id):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE id=?", (id,))
    row = curs.fetchall()

    conn.close()

    return row

def deletePerson(key):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute('''DELETE FROM ADDRESSBOOK WHERE id = ?''', (key,))

    conn.commit()

    conn.close()

def writePerson(name, number, email):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("UPDATE ADDRESSBOOK SET name = ? , number = ?, email = ? WHERE name= ?", (name,number,email,name))

    conn.commit()

    conn.close()

def searchName(num):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT * FROM ADDRESSBOOK WHERE number=?", (num,))
    row = curs.fetchall()

    conn.close()

    return row

def getCall():
    conn = getConnection()

    curs = conn.cursor()

    sql = "select * from call"
    curs.execute(sql)

    row = curs.fetchall()

    conn.close()

    return row

def setCall():
    conn = getConnection()

    cur = conn.cursor()

    # TODO : query

    conn.commit()

    conn.close()

    return; # maybe TODO



def getMsg():
    conn = getConnection()

    curs = conn.cursor()

    sql = "select * from sms"
    curs.execute(sql)

    row = curs.fetchall()

    conn.close()

    return row

def changePerson(name, number, email, id):
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("""UPDATE ADDRESSBOOK SET name = ? ,number = ?,email = ? WHERE id= ? """,
  (name,number,email,id))

    conn.commit()

    conn.close()
