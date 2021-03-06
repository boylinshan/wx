from utils.tools import Singleton


class ServiceFactory(object):
	__metaclass__ = Singleton

	def __init__(self):
		self.services = {'ServiceCosts'}
		self.service_dict= {}
		self.id2name = {'1': 'Costs'}
		self.init()

	def init(self):
		for name in self.services:
			module = __import__('Service'+'.'+name)
			module = getattr(module, name, None)
			member = getattr(module, name, None)
			if member:
				self.service_dict[name] = member
			else:
				raise StandardError("can't find %s" % name)

	def getService(self, id):
		name = 'Service' + self.id2name[id]
		member = self.service_dict.get(name, None)
		if not member:
			raise StandardError("can't find %s" % name)

		return member()