import sqlite3
from utils.tools import Singleton


class DataBase(object):
	__metaclass__ = Singleton

	def __init__(self):
		super(DataBase, self).__init__()

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

