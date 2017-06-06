import pymysql


# MySQL Connection 연결
def getConnection():
    return pymysql.connect(host='localhost', user='testuser', password='0000',
                	       db='addressbook', charset='utf8')



def getPerson():
    # Connection 으로부터 Cursor 생성
    conn = getConnection()

    curs = conn.cursor()

    # SQL문 실행
    sql = "select * from addressbook"
    curs.execute(sql)

    # 데이타 Fetch
    row = curs.fetchall()

    # Connection 닫기
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