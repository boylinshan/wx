class Observer(object):
	def __init__(self):
		super(Observer, self).__init__()

	def on_value_changed(self):
		raise NotImplementedError

class Observable(object):
	def __init__(self):
		super(Observable, self).__init__()
		self.__dict__['_observes_dict'] = {}

	def addObserver(self, obj, *names):
		for name in names:
			if name not in self._observes_dict:
				self._observes_dict[name] = set()

			self._observes_dict[name].add(obj)

	def clearObserver(self):
		self._observes_dict.clear()

	def __setattr__(self, name, new_value):
		observers = self._observes_dict.get(name, None)
		old_value = self.__dict__.get(name, None)
		super(Observable, self).__setattr__(name, new_value)

		if not observers or old_value == new_value:
			return

		for observer in observers:
			observer.on_value_changed(self, name, old_value, new_value)


