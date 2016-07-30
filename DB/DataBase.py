import sqlite3
from utils.tools import singleton

@singleton
class DataBase(object):
	def __init__(self, db):
		self._conn = sqlite3.connect('db')

	def init(self):
		cursor = self._conn.cursor()
		cursor.execute('create table if not exists costs(uid text, money real)')
		self._conn.commit()

	def execute(self, sql):
		cursor = self._conn.cursor()
		cursor.execute(sql)

		return cursor.fetchone()

