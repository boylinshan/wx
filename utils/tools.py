def singleton(cls):
	singleton = cls()
	singleton.__call__ = lambda : singleton
	return singleton