#encoding=utf-8
import sqlite3,os

basedir=os.path.abspath(os.path.dirname(__file__))
DATABASE=os.path.join(basedir,"data.db")

con=sqlite3.connect(DATABASE)
con.execute("create table if not exists test1(id INTEGER PRIMARY KEY ,name VARCHAR (64))")
con.execute("insert into test1 (id,name) VALUES (?,?)",(2,"TOM"))
con.commit()