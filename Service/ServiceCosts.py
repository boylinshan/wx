from Service import Service

class ServiceCosts(Service):
	def __init__(self):
		super(ServiceCosts, self).__init__()
		self.money = 0
		self.uid = 0

	def init(self, uid):
		self.uid = uid
		result = self.database.query('select money from costs where uid = "%s"' % self.uid)
		if not result:
			self.money = 300
			self.database.insert('insert into costs values("%s", %s)' % (self.uid, self.money))
		else:
			self.money = result[0]

		self.addObserver(self.database, 'money')

	def parse(self, cost):
		try:
			cost = eval(cost)
		except Exception as e:
			print e
			cost = 0

		self.money = result[0] - cost

		return self.money 