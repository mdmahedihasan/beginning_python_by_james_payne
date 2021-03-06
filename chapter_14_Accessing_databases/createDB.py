import os
import sqlite3

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()

cursor.execute("""
create table employee(
empid integer,
firstname varchar,
lastname varchar,
dept integer,
manager integer,
phone varchar
)
""")

cursor.execute("""
create table department(
departmentid integer,
name varchar,
manager integer
)
""")

cursor.execute("""
create table user(
userid integer,
username varchar,
employeeid integer
)
""")

cursor.execute("""create index userid on user (userid)""")
cursor.execute("""create index empid on employee (empid)""")
cursor.execute("""create index deptid on department (deptid)""")
cursor.execute("""create index deptfk on employee (dept)""")
cursor.execute("""create index mgr on employee (manager)""")
cursor.execute("""create index emplid on user (employeeid)""")
cursor.execute("""create index deptmgr on department (manager)""")

conn.commit()
cursor.close()
conn.close()
