from Service import Service

class ServiceCosts(Service):
	def __init__(self):
		super(ServiceCosts, self).__init__()
		self.money = 0
		self.uid = None
		self.init()
		self.addObserver(self.database, 'money')

	def init(self):
		result = self.database.query('select money from costs where uid = "%s"' % self.uid)
		if not result:
			self.money = 300
			self.database.insert('insert into costs values("%s", %s)' % (uid, self.money))
		else:
			self.money = result[0]

	def parse(self, uid, cost):
		self.uid = uid
		try:
			cost = eval(cost)
		except Exception as e:
			print e
			cost = 0

		self.money = result[0] - cost

		return self.money 