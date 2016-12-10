import sqlite3
import sys

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()
employee = sys.argv[1]

query = """
select e.empid
from user u, employee e
WHERE username = ? AND u.employeeid = e.empid
"""

cursor.execute(query, (employee,));
for row in cursor.fetchone():
    if (row != None):
        empid = row

cursor.execute("delete from employee WHERE empid = ?", (empid,))
conn.commit()
cursor.close()
conn.close()
