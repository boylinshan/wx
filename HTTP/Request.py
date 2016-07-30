import xml.etree.ElementTree as ET
import time
from flask import request

class Request(object):
	def __init__(self, request):
		super(Request, self).__init__()
		self.request = request
		self.data = ET.fromstring(self.request.data)

	def parse(self, *keys):
		values = {}
		for key in keys:
			values[key] = self.data.find(key).text

		values['curTime'] = str(int(time.time()))

		return values 
