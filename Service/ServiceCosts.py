from Service import Service

class ServiceCosts(Service):
	def __init__(self):
		super(ServiceCosts, self).__init__()

	def parse(self, uid, content):
		print type(self.database)
		result = self.database.query()
		if not result:
			self.database.insert('insert into costs values("%s", 300)' % uid)
			return 300
		else:
			return 200