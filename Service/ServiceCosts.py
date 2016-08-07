from Service import Service

class ServiceCosts(Service):
	def __init__(self):
		super(ServiceCosts, self).__init__()

	def parse(self, uid, content):
		result = self.database.query('select money from costs where uid = "%s"' % uid)
		if not result:
			self.database.insert('insert into costs values("%s", 300)' % uid)
			return 300
		else:
			print result
			print type(result)
			print content
			print type(content)
			return 200