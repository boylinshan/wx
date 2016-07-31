import sqlite3
from utils.tools import Singleton

def OperateWrap(operate):
	def operateWrap(self, param):
		self.conn = sqlite3.connect(self.database)
		return operate(self, param)
		#self.conn.commit()
		#self.conn.close()

	return operateWrap


class DataBase(object):
	def __init__(self):
		super(DataBase, self).__init__()
		self.database = self.__class__.__name__[7:] + '.db'
		self.conn = None
		print '**'
		self.init()
		print self

	@OperateWrap
	def init(self, sql=None):
		cursor = self.conn.cursor()
		cursor.execute('create table if not exists costs(uid text, money real)')

	@OperateWrap
	def query(self, sql):
		cursor = conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchone()

		return result

	@OperateWrap
	def insert(self, sql):
		cursor = conn.cursor()
		cursor.execute(sql)

