import sqlite3
#from utils.tools import singleton

def singleton(cls):
	singleton = cls()
	singleton.__call__ = lambda : singleton
	return singleton

@singleton
class DataBase:
	def __init__(self):
		return

	def init(self):
		conn = sqlite3.connect('wx.db')
		cursor = conn.cursor()
		cursor.execute('create table if not exists costs(uid text, money real)')
		conn.commit()
		conn.close()

	def query(self, sql):
		conn = sqlite3.connect('wx.db')
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchone()

		return result

	def insert(self, sql):
		conn = sqlite3.connect('wx.db')
		cursor = conn.cursor()
		cursor.execute(sql)
		conn.commit()
		conn.close()


