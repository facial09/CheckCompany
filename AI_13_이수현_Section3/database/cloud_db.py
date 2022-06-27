import psycopg2
import json

str_1 = None

with open('data.json','r') as f:
    str_1 = json.load(f)


collist = list(str_1[0].keys())
print(str_1[1]['name'])


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
# print(str(test).strip("[]"))

conn = psycopg2.connect(
    host = 'jelani.db.elephantsql.com',
    database ='gesuiwzd',
    user='gesuiwzd',
    password='DwmwKQz8jfjlkKD7_krWutT7olrOpDI9'
)

cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS all_data''')
cur.execute(f'''CREATE TABLE all_data (
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
    cur.execute(f'INSERT INTO all_data ({col0},{col1},{col2},{col3},{col4},{col5},{col6},{col7},{col8},{col9}) VALUES ({str(test).strip("[]")})')

conn.commit()
conn.close()