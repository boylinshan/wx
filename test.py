import sqlite3

conn = sqlite3.connect('Costs.db')
cursur = conn.cursur()

for item in cursur.execute('select * from costs'):
	print item