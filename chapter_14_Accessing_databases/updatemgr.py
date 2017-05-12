import sqlite3
import sys

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()
newmgr = sys.argv[2]
employee = sys.argv[1]

query = """
select e.empid
from USER u, employee e
WHERE username = ? AND u.employeeid = e.empid
"""

cursor.execute(query, (newmgr,))
for row in cursor.fetchone():
    if (row != None):
        mgrid = row

cursor.execute(query, (employee,))
for row in cursor.fetchone():
    if (row != None):
        empid = row

cursor.execute("update employee set manager = ? WHERE empid = ?", (mgrid, empid))
conn.commit()
cursor.close()
conn.close()
