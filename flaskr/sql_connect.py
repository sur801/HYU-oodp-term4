import pymysql

# Us 4 spaces as indent

conn = pymysql.connect('addressbook.db')

conn.execute('CREATE TABLE addressbook (id INT UNSIGNED NOT NULL AUTO_INCREMENT, name TEXT, number TEXT, email TEXT')

conn.close()

#pymysql.connect('addressbook.db')

# MySQL Connection 연결
def getConnection():
    return pymysql.connect(host='localhost', user='testuser', password='0000',
                	       db='addressbook', charset='utf8')



def getPerson():
    # Connection 으로부터 Cursor 생성
    conn = getConnection()

    curs = conn.cursor()

    # SQL문 실행
    sql = "select * from addressbook.addressbook"
    curs.execute(sql)

    # 데이타 Fetch
    row = curs.fetchall()

    # Connection 닫기
    conn.close()

    return row


def getCall():
    conn = getConnection()

    curs = conn.cursor()

    sql = "select * from addressbook.call"
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

"""
def printTest():
    rows  = getPerson()

    for p in rows:
    	print(p[1])

    #print(rows)     # 전체 rows
    #print(rows[0][1])  # 첫번째 row: (1, '김정수', 1, '서울')
    #print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

printTest()
"""