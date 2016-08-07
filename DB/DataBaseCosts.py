from DataBase import DataBase

class DataBaseCosts(DataBase):
	def __init__(self):
		super(DataBaseCosts, self).__init__()

	def on_value_changed(self, obj, name, old_value, new_value):
		self.update('update costs set %s = %s where uid = "%s"' % (name, new_value, self.uid))




