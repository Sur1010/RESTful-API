import pymysql
from config import host, user, password, database, cursorclass

conn = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database,
    cursorclass = cursorclass
)

cursor = conn.cursor()
sql_query = """ CREATE TABLE book(
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""
cursor.execute(sql_query)
conn.close()