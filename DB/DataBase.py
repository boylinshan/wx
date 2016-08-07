import sqlite3
from utils.tools import Singleton
from utils.Observer import Observer

def Session(func):
	def wrap_func(self, param=None):
		self.conn = sqlite3.connect(self.database)
		if param:
			result = func(self, param)
		else:
			result = func(self)
		self.conn.commit()
		self.conn.close()

		return result

	return wrap_func

class DataBase(Observer):
	__metaclass__ = Singleton
	def __init__(self):
		super(DataBase, self).__init__()
		self.database = self.__class__.__name__[8:] + '.db'
		self.conn = None
		self.init()
		print 'init-----'

	@Session
	def init(self):
		cursor = self.conn.cursor()
		cursor.execute('create table if not exists costs(uid text, money real)')

	@Session
	def query(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)
		result = cursor.fetchone()

		return result

	@Session
	def insert(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)

	@Session
	def update(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)
