# Problem 1

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()
sql = """
SELECT id,password FROM users WHERE username='Trump';
"""
cur.execute(sql)
for row in cur.fetchall():
   print('row[0]=', row[0])
   print('row[1]=', row[1])

#line ten throws an exception - no such table users 
#guessing that when FROM is put in then there must be a table to something after