from DataBase import DataBase

def OperateWrap(operate):
	def operateWrap(self):
		self.conn = sqlite3.connect(self.database)
		operate(self)
		self.conn.commit()
		self.conn.close()

	return operateWrap

class DataBaseCosts(DataBase):
	def __init__(self):
		super(DataBaseCosts, self).__init__()

	def query(self):
		print '****'




