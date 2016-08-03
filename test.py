import sqlite3

conn = sqlite3.connect('Costs.db')
cursor = conn.cursor()

for item in cursor.execute('select * from costs'):
	print item