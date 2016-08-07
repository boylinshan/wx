from DB.DBFactory import DBFactory
from utils.Observer import Observable

class Service(Observable):
	def __init__(self):
		super(Service, self).__init__()
		self.database = DBFactory().getDataBase(self.__class__.__name__[7:])

	def parse(self, content):
		raise NotImplementedError("No Parse Function!")


