import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='library2',
    user='user2',
    password='1234',
)

cur = conn.cursor()

cur.close()
conn.close()
