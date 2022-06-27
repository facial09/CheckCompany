# STEP 1
import pymysql
import json

str_1 = None

with open('data.json','r') as f:
    str_1 = json.load(f)


collist = list(str_1[0].keys())



col0 = collist[0].replace(" ","")
col1 = collist[1].replace(" ","")
col2 = collist[2].replace(" ","")
col3 = collist[3].replace(" ","")
col4 = collist[4].replace(" ","")
col5 = collist[5].replace(" ","")
col6 = collist[6].replace(" ","")
col7 = collist[7].replace(" ","")
col8 = collist[8].replace(" ","")
col9 = collist[9].replace(" ","")

collist = [col0,col1,col2,col3,col4,col5,col6,col7,col8,col9]
# STEP 2: MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='facial09', password='1420',
                    db='section3', charset='utf8') # 한글처리 (charset = 'utf8')

# STEP 3: Connection 으로부터 Cursor 생성
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS company''')
cur.execute(f'''CREATE TABLE company (
            {col0} TEXT,
            {col1} FLOAT,
            {col2} FLOAT,
            {col3} FLOAT,
            {col4} FLOAT,
            {col5} FLOAT,
            {col6} INT,
            {col7} INT,
            {col8} INT,
            {col9} FLOAT);'''
            )
conn.commit()



for i in range(0,len(str_1)):
    test = list(str_1[i].values())
    cur.execute(f'INSERT INTO company ({col0},{col1},{col2},{col3},{col4},{col5},{col6},{col7},{col8},{col9}) VALUES ({str(test).strip("[]")})')

conn.commit()
conn.close()