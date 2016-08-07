from Service import Service

class ServiceCosts(Service):
	def __init__(self):
		super(ServiceCosts, self).__init__()
		self.money = 300
		self.uid = uid
		self.addObserver(self.database, 'money')

	def parse(self, uid, cost):
		self.uid = uid
		result = self.database.query('select money from costs where uid = "%s"' % self.uid)
		if not result:
			self.database.insert('insert into costs values("%s", %s)' % (uid, self.money))
			return self.money
		else:
			try:
				cost = eval(cost)
			except Exception as e:
				print e
				cost = 0

			self.money = result[0] - cost

			return self.money 