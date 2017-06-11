import sqlite3

# Use 4 spaces as indent

"""
conn = sqlite3.connect('addressbook.db')

conn.execute('CREATE TABLE addressbook (id INT UNSIGNED NOT NULL AUTO_INCREMENT, name TEXT, number TEXT, email TEXT')

connn.close()
"""

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