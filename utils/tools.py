class Singleton(type):
	def __init__(cls, name, base, dict):
		super(Singleton, cls).__init__(name, base, dict)
		cls._instances = {}

	def __call__(cls, *args, **kargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kargs)
		return cls._instances[cls]
