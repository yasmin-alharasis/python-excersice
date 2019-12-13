import sqlite3
import os

DATABASE="stocks.db"

if not os.path.exists(DATABASE):
    conn=sqlite3.connect(DATABASE)
    cur=conn.cursor()
    cur.execute("CREATE TABLE stocks (date NUMERIC,trans TEXT,symbol TEXT,qty REAL,price REAL);")
    conn.commit()
    cur.execute("INSERT INTO stocks VALUES('2006-01-05','Buy','RHAT','10000.0','35.14');")
    cur.execute("INSERT INTO stocks VALUES('2006-01-05','SEL','RHAT','10000.0','35.25');")
    cur.execute("INSERT INTO stocks VALUES('2006-01-05','SEL','APPLE','50.0','3.23');")
    cur.execute("INSERT INTO stocks VALUES('2006-01-05','SEL','APPLE','50.0','3.23');") 
    conn.commit()
    conn.close() 