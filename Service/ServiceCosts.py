from Service import Service

class ServiceCosts(Service):
	def __init__(self):
		super(ServiceCosts, self).__init__()

	def parse(self, uid, cost):
		result = self.database.query('select money from costs where uid = "%s"' % uid)
		if not result:
			self.database.insert('insert into costs values("%s", 300)' % uid)
			return 300
		else:
			try:
				cost = eval(cost)
			except Exception as e:
				print e
				cost = 0

			result = result[0] - cost

			return result 