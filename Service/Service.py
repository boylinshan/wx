from DB.DBFactory import DBFactory

class Service(object):
	def __init__(self):
		super(Service, self).__init__()
		self.database = DBFactory().getDataBase(self.__class__.__name__[6:])

	def parse(self, content):
		raise NotImplementedError("No Parse Function!")


