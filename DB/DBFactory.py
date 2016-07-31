from utils.tools import Singleton


class DBFactory(object):
	__metaclass__ = Singleton

	def __init__(self):
		self.databases = {'DataBaseCosts'}
		self.db_dict = {}
		self.init()

	def init(self):
		for name in self.databases:
			module = __import__('DB'+'.'+name)
			module = getattr(module, name, None)
			member = getattr(module, name, None)
			if member:
				self.db_dict[name] = member
			else:
				raise StandardError("can't find %s" % name)

	def getDataBase(self, name):
		name = 'DataBase' + name
		member = self.db_dict.get(name, None)
		if not member:
			raise StandardError("can't find %s" % name)

		return member
