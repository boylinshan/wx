import sqlite3
#from utils.tools import singleton

def singleton(cls):
	singleton = cls()
	singleton.__call__ = lambda : singleton
	return singleton

@singleton
class DataBase:
	def __init__(self):
		self._conn = sqlite3.connect('wx.db')

	def init(self):
		cursor = self._conn.cursor()
		cursor.execute('create table if not exists costs(uid text, money real)')
		self._conn.commit()

	def execute(self, sql):
		cursor = self._conn.cursor()
		cursor.execute(sql)

		return cursor.fetchone()

