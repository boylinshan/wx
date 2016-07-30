class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kargs)
		return cls._instances[cls]
